# Import necessary modules
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory
from langchain_aws.chat_models.bedrock import ChatBedrock

# Set the model ID for the Nova Lite LLM
modelId = "amazon.nova-lite-v1:0"

# Create an instance of ChatBedrock
# Stop sequence prevents LLM from continuing conversation with itself
nova_chat = ChatBedrock(model_id=modelId,
                            model_kwargs = {
                                "max_tokens": 300,
                                "stop": ["User", "human"]
                            })

# Prompt template format for using ConversationBufferMemory. Allowing the {history} variable
# to be injected with past prompts and responses
prompt_template = PromptTemplate(
    input_variables=['history', 'input'],
    template="""You are an assistant for a bar trivia night.
chat_history : {history}
User: {input}
AI: """)

# Use LLMChain to pass an input and conversation history to the chat model
# Set memory to ConversationBufferMemory()
# Set verbose as true to see inputs and output for each runnable of the chain
chain = ConversationChain(llm = nova_chat, memory = ConversationBufferWindowMemory(k = 5), verbose = True)

def buffer_chat(input):
    """
    Interact with an in-memory chat bot.

    Args:
        input (string): Prompt.

    Returns:
        string: LLM response.
    """
    # Index the response for the response text, print and return it
    response = chain.invoke(input)
    print(response)
    return(response['text'])

# If the script is being run as the main program, invoke in_memory_chat
if __name__ == "__main__":
    print("Write a question about the oceans of Europa.")
    buffer_chat("Write a question about the oceans of Europa.")
    print("Talk more about that")
    buffer_chat("Talk more about that")

