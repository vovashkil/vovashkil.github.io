# Import necessary modules
from langchain_community.chat_message_histories import DynamoDBChatMessageHistory
import boto3
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_aws.chat_models.bedrock import ChatBedrock
from langchain.globals import set_debug
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.schema.output_parser import StrOutputParser

# Set the model ID for the Nova Lite LLM
modelId = "amazon.nova-lite-v1:0"

# Create a DynamoDB resource using Boto3
dynamodb =  boto3.client('dynamodb')

# The name of the DynamoDB table where messages will be retained
table_name = "SessionTable"

def create_dynamo_chat():
    """
    Create DynamoDB table and LangChain components necessary for a chatbot with cloud memory.
    """
    # Create a table with the primary key being session ID. All tables need a primary key
    table = dynamodb.create_table(TableName = table_name,
                                    KeySchema = [{"AttributeName": "SessionId", "KeyType": "HASH"}],
                                    AttributeDefinitions = [{"AttributeName": "SessionId", "AttributeType": "S"}],
                                    BillingMode = "PAY_PER_REQUEST")

    # Wait until the table exists.
    dynamodb.get_waiter('table_exists').wait(TableName = table_name)

    try:
        # The prompt templates leverages the MessagePlaceholder class which assumes the variable is already a list of messages
        # https://python.langchain.com/v0.2/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html#langchain_core.prompts.chat.MessagesPlaceholder
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "You are an assistant for a bar trivia night."),
                MessagesPlaceholder("history"),
                ("human", "{question}"),
            ]
        )


        # Create an instance of ChatBedrock
        # Stop sequence prevents LLM from continuing conversation with itself
        nova_chat = ChatBedrock(model_id=modelId,
                                    model_kwargs = {
                                        "max_tokens": 300,
                                        "stop": ["User", "human"]
                                    })

        # LCEL chain takes inputs including history, creates a prompt, passes 
        # it to the chat model, and outputs a string
        global chain
        chain = prompt_template | nova_chat | StrOutputParser()

        # RunnableWithMessageHistory is a runnable that manages message history 
        # for another runnable. The key parameters correspond to the settings
        # stipulated in the prompt_template
        # The lambda function takes a session_id as an argument and returns a DynamoDBChatMessageHistory instance
        # global chain_with_history is invoked in another function
        # https://python.langchain.com/v0.2/api_reference/core/runnables/langchain_core.runnables.history.RunnableWithMessageHistory.html#langchain_core.runnables.history.RunnableWithMessageHistory
        # DynamoDBChatMessageHistory manages retrieval and storage of messages
        # to the DynamoDB table
        # https://api.python.langchain.com/en/latest/chat_message_histories/langchain_community.chat_message_histories.dynamodb.DynamoDBChatMessageHistory.html
        global chain_with_history
        chain_with_history = RunnableWithMessageHistory(
                    chain,
                    lambda session_id: DynamoDBChatMessageHistory(
                        table_name = table_name, session_id = session_id
                    ),
                    input_messages_key="question",
                    history_messages_key="history")


    except Exception as e:
        print(e)


def dynamodb_chat(input):
    """
    Interact with a chat bot with a cloud memory store.

    Args:
        input (string): Prompt.

    Returns:
        string: LLM response.
    """
    # Invoke chain_with_history, <SESSION_ID> will be the primary key passed to DynamoDBChatMessageHistory
    response = chain_with_history.invoke({"question" : input}, config = {"configurable": {"session_id": "1"}})

    # Print and return LLM response
    print(response)
    return(response)

def delete_table():
    """
    Delete SessionTable.

    Returns:
        dict: Table deletion response.
    """
    # response = table.delete()
    response = dynamodb.delete_table(TableName = table_name)
    return(response)

# If the script is being run as the main program, create table and necessary resources, invoke dynamodb_chat, then delete table
if __name__ == "__main__":
    create_dynamo_chat()
    dynamodb_chat("Two people are tied at the end of triva. What do I do?")
    dynamodb_chat("Nevermind, they agreed to split first prize.")
    delete_table()