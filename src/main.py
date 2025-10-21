import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from config import settings
from langchain_core.messages import HumanMessage
from langsmith import traceable


os.environ["LANGSMITH_API_KEY"] = settings.LANGSMITH_API_KEY
os.environ["LANGSMITH_PROJECT"] = settings.LANGSMITH_PROJECT
os.environ["LANGSMITH_TRACING"] = settings.LANGSMITH_TRACING

model = ChatOpenAI(
    model=settings.MODEL_DEPLOYMENT,
    api_key=settings.OPENAI_API_KEY,
)

@traceable
def chat_service(question: str) -> str:
    response = model.invoke([HumanMessage(content=question)])
    return response.content

app = FastAPI()


class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    return chat_service(request.message)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")
