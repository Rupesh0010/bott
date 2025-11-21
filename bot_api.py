from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
import traceback

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        prompt = ChatPromptTemplate.from_template(
            "You are a helpful assistant.\nUser question: {user_question}"
        )

        llm = ChatNVIDIA(
            model="meta/llama-3.1-8b-instruct",
            api_key=os.getenv("NVIDIA_API_KEY")
        )

        chain = prompt | llm | StrOutputParser()
        answer = await chain.ainvoke({"user_question": req.message})

        return {"response": answer}

    except Exception as e:
        print("🔥 ERROR:", e)
        traceback.print_exc()
        return {"error": str(e)}
