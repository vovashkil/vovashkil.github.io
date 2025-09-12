# Import necessary modules
from langchain_core.prompts import PromptTemplate
from langchain_aws.chat_models.bedrock import ChatBedrock
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.runnables.base import RunnableParallel
from langchain_core.runnables.passthrough import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain_core.callbacks import BaseCallbackHandler
from typing import Any, Dict, List
from langchain.globals import set_debug
from langchain_core.outputs.llm_result import LLMResult

# Set the model ID for Nova Lite
modelId = "amazon.nova-lite-v1:0"

############################# model creation #############################

# Create an instance of ChatBedrock
# Chosen model parameters promote the correct amount of freedom for the LLM to
# provide both correct and incorrect answers
# Stop sequence "User" prevents LLM from continuing conversation with itself
nova_llm = ChatBedrock(model_id = modelId,
                        model_kwargs = {
                            "max_tokens": 200,
                            "temperature": .5,
                            "top_p": .5,
                            "top_k": 50,
                            "stop": ["User"]
                        })

############################# question #############################

# The hosts initial question
host_question_template = PromptTemplate(
    input_variables =["topic"],
    template = """User: Write a simple trivia question about {topic}. Make it a direct question that can be answered in a few words. Do not include multiple choice options. Do not provide the answer.

Assistant: """)

# Takes an input, forms a prompt from the prompt template, sends
# that prompt to the ChatBedrock model, and outputs the response into a string
host_question_chain = host_question_template | nova_llm | StrOutputParser()

############################# good answer #############################

# Prompt LLM to give a correct answer
contestant1_template = PromptTemplate(
    input_variables =["question"],
    template = """User: Answer this trivia question correctly in as few words as possible: {question}

Assistant: """)

# Takes an input, forms a prompt from the prompt template, sends
# that prompt to the ChatBedrock model, and outputs the response into a string
contestant1_chain = contestant1_template | nova_llm | StrOutputParser()

############################# bad answer #############################

# Prompt LLM to give an incorrect answer
contestant2_template = PromptTemplate(
    input_variables =["question"],
    template = """User: Answer the following question incorrectly and in one sentence. Do not say you answered incorrectly: {question}

Assistant: """)

# Takes an input, forms a prompt from the prompt template, sends
# that prompt to the ChatBedrock model, and outputs the response into a string
contestant2_chain = contestant2_template | nova_llm | StrOutputParser()

############################# host judgement #############################

# Prompt LLM to judge the answers submitted
# Prompt template will take 3 inputs
## ADD HOST JUDGING TEMPLATE HERE
host_judge_template = PromptTemplate(
    input_variables =["question", "answer1", "answer2"],
    template = """User: You're the judge of a contest. Given a question and two answers: Answer 1 and Answer 2, you should pick the correct answer in 3 sentences and be funny about it.
The question is "{question}".
Marissa's answer is "{answer1}".
Diego's answer is "{answer2}".

Assistant: """)

# Takes inputs, forms a prompt from the prompt template, sends
# that prompt to the ChatBedrock model, and outputs the response into a string
## ADD HOST JUDGING CHAIN HERE
host_judge_chain = host_judge_template | nova_llm | StrOutputParser()

############################# master chain #############################

# 1. host_question_chain: Create the trivia question from the topic
# 2. RunnableParallel({"answer1" : contestant1_chain, "answer2" : contestant2_chain,
# "question": RunnablePassthrough()}): Pass the question to contestant 1's chain, contestant 2's chain, and judge's host chain. RunnablePassthrough passes the input unchanged
# https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.passthrough.RunnablePassthrough.html
# https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.base.RunnableParallel.html
# 3. RunnableParallel({"host" : host_judge_chain, "passthrough":RunnablePassthrough()}): The Host Judge chain judges the responses based on the question. The RunnableParallel passes through the question, answer1, and answer2 so that they can be indexed and returned.
## TO EXTEND THE MASTER CHAIN, PIPE ANOTHER RUNNABLEPARALLEL CONTAINING HOST_JUDGE_CHAIN AND A RUNNABLEPASSTHROUGH
master_chain = (
    host_question_chain | 
    RunnableParallel({"answer1" : contestant1_chain, "answer2" : contestant2_chain, "question": RunnablePassthrough()}) |
    RunnableParallel({"host" : host_judge_chain, "passthrough":RunnablePassthrough()})
)

############################# function invocation #############################

def trivia_simulator(topic):
    """
    Simulate a trivia question, its answers, and judge a winner.

    Args:
        topic (string): The topic for the trivia question.

    Returns:
        list[question(string), answer1(string), answer2(string), judgement(string)]:
            The responses from each persona.
    """
    # Invoke the master chain
    response = master_chain.invoke({"topic" : topic})

    # Index the host question, answer1, and answer2 from the passthrough and the host judgement from the host key
    response_list = [response['passthrough']['question'], response['passthrough']['answer1'], response['passthrough']['answer2'], response.get('host', 'key not found')]
    # Print each response
    for response_item in response_list:
        print(response_item, "\n")

    # Return the response of each LLM invocation, 3 in total, as a list
    return(response_list)

# If the script is being run as the main program, invoke trivia_simulator
if __name__ == "__main__":
    trivia_simulator(topic = "The planets of the Milky Way")