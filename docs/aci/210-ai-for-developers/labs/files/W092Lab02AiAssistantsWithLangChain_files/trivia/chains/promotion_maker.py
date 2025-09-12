# Import necessary modules
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_aws.chat_models.bedrock import ChatBedrock

# Set the model ID for the Nova Lite LLM
modelId = "amazon.nova-lite-v1:0"

# Create an instance of ChatBedrock
# Stop sequence "User" prevents LLM from continuing conversation with itself
nova_llm = ChatBedrock(model_id = modelId,
                        model_kwargs = {
                            "stop": ["User"]
                        })

# Multiline string template to create promotional content
template = """
User: You run a trivia night. Given the theme, time and location, write an invitation for the event. 
Use a 
Theme: {theme}
Time: {time}
Location: {location}

Assistant:
"""

# Define the prompt template from the string. The input variables are automatically inferred
prompt_template = PromptTemplate.from_template(template)

# Chain to run queries against LLMs 
# https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html
chain = LLMChain(llm = nova_llm, prompt = prompt_template)

def promotion_maker(theme, time_of, location):
    """
    Create a promotional flyer.

    Args:
        theme (string): The theme of the trivia night.
        time_of (string): The time/time and date of the trivia night.
        location (string): The location of the trivia night.

    Returns:
        string: The promotional flyer.
    """

    # Invoke the LLMChain and save the response
    response = chain.invoke(
        {
            "theme": theme,
            "time": time_of,
            "location": location,
        }
    )

    # Index the response for the response text, print and return it
    content = response["text"]
    print(content)
    return(content)

# If the script is being run as the main program, invoke promotion_maker
if __name__ == "__main__":
    promotion_maker(theme = "Astronomy", time_of= "October 12th", location= "The Local Pub")