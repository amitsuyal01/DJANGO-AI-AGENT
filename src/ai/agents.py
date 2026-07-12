from langchain.agents import create_agent
from ai.llms import get_openai_model
from ai.tools import tools

def get_document_agent(checkpointer=None):
    model = get_openai_model()
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt="You are a helpful assistant in managing a user's documents within this app.",
        checkpointer=checkpointer
    )
    return agent









