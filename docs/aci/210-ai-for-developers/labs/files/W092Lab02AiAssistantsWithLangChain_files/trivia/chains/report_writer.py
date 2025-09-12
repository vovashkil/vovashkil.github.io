# Import necessary modules
from langchain_core.prompts import ChatPromptTemplate
from langchain_aws.chat_models.bedrock import ChatBedrock

# Set the model ID for the Nova Lite LLM
modelId = "amazon.nova-lite-v1:0"

# Create an instance of ChatBedrock
nova_chat = ChatBedrock(model_id = modelId)

# The from_template method of ChatPromptTemplate creates a ChatPromptTemplate
# for a human message
prompt_template = ChatPromptTemplate.from_template(role="human", 
    template = "Give me small report about {topic}")

# This pipe takes an input, forms a prompt from the prompt template, then sends
# that prompt to the ChatBedrock model
# https://python.langchain.com/v0.2/docs/how_to/sequence/
chain = prompt_template | nova_chat


def report_writer(topic):
    """
    Create a report on a subject.

    Args:
        topic (string): The intended topic of the report.

    Returns:
        string: The report.
    """

    # Invoke the piped chain and save the response
    response = chain.invoke(
        {
            "topic": topic
        }
    )

    # Index the response for the response text, print and return it
    content = response.content
    print(content)
    return(content)

# If the script is being run as the main program, invoke report_writer
if __name__ == "__main__":
    report_writer("The Big Dipper")