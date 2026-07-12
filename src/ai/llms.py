
from langchain_openai import ChatOpenAI
from django.conf import settings

def get_openai_api_key():
    return settings.OPENAI_API_KEY

def get_openai_model(model = "gpt-4o-mini"):
    llm = ChatOpenAI(
        model=model,
        # stream_usage=True,
        temperature=0,
        # max_tokens=None,
        # timeout=None,
        # reasoning_effort="low",
        max_retries=2,
        api_key= get_openai_api_key(),
        # organization="...",
        # other params...
    )
    return llm

