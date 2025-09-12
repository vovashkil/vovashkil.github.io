# Import necessary modules
from langchain_aws.chat_models.bedrock import ChatBedrock
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain

# Set the model ID for the Nova Lite LLM
modelId = "amazon.nova-lite-v1:0"

# Create an instance of ChatBedrock
# Stop sequence prevents LLM from continuing conversation with itself
nova_chat = ChatBedrock(model_id=modelId,
                            model_kwargs = {
                                "max_tokens": 300,
                                "stop": ["User", "human"]
                            })

# A ConversationChain does not need to leverage a prompt template
# ConversationBufferWindowMemory is set to k = 1, meaning it will only recall its response to your last prompt, giving it a short memory
# Set verbose as true to see inputs and output for each runnable of the chain
chain = ConversationChain(llm = nova_chat, memory = ConversationBufferWindowMemory(k = 1), verbose = True)

def window_chat(input):
    """
    Interact with an in-memory chat bot with a window of memory set to a single prompt and response.

    Args:
        input (string): Prompt.

    Returns:
        string: LLM response.
    """
    # Index the response for the response text, print and return it
    response = chain.invoke(input)
    print(response)
    return(response['response'])

# If the script is being run as the main program, invoke window_memory_chat
if __name__ == "__main__":
    print("Carl Sagan vs Neil deGrasse Tyson")
    window_chat("Carl Sagan vs Neil deGrasse Tyson")
    print("Who do you think is the best astronomer?")
    window_chat("Who do you think is the best astronomer?")
    print("Back to my original question...")
    window_chat("Back to my original question...")