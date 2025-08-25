from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from config import REPO_ID, MAX_TOKENS, TEMPERATURE
load_dotenv()
def chat_model(repo_id=REPO_ID, max_tokens=MAX_TOKENS, temperature=TEMPERATURE):
    endpoint=HuggingFaceEndpoint(
        repo_id=repo_id,
        max_new_tokens=max_tokens,
        temperature=temperature
    )
    return ChatHuggingFace(llm=endpoint)