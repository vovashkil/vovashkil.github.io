# Import necessary modules
from langchain_core.prompts import PromptTemplate
from langchain_aws.chat_models.bedrock import ChatBedrock
from langchain_aws.chat_models.bedrock import ChatBedrock
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory

# Set the model ID for the Nova Lite LLM
modelId = "amazon.nova-lite-v1:0"

# Create an instance of ChatBedrock
# Stop sequence prevents LLM from continuing conversation with itself
nova_chat = ChatBedrock(model_id=modelId,
                            model_kwargs = {
                                "max_tokens": 300,
                                "stop": ["User", "human"]
                            })

# A second model is created, this is used to summarize the conversation
nova_llm = ChatBedrock(model_id = modelId)

# A ConversationChain does not need to leverage a prompt template
# ConversationSummaryMemory takes the LLM as an input. It uses that model to summarize the conversation with GenAI
# Set verbose as true to see inputs and output for each runnable of the chain
chain = ConversationChain(llm = nova_chat, memory = ConversationSummaryMemory(llm = nova_llm), verbose = True)

def summary_chat(input):
    """
    Interact with an in-memory chat bot with a summary memory.

    Args:
        input (string): Prompt.

    Returns:
        string: LLM response.
    """
    # Index the response for the response text, print and return it
    response = chain.invoke(input)
    print(response)
    return(response['response'])

# If the script is being run as the main program, invoke summary_memory_chat
if __name__ == "__main__":
    print("Someone said Pluto is a planet. Should I give them points?")
    summary_chat("Someone said Pluto is a planet. Should I give them points?")
    print("What do you mean?")
    summary_chat("What do you mean?")
    print("What if I think Pluto is a planet?")
    summary_chat("What if I think Pluto is a planet?")