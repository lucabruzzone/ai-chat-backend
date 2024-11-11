# pylint: disable=import-error
from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from openai import OpenAI

from settings import OPENAI_API_KEY

# client = OpenAI({"api_key": OPENAI_API_KEY})
client = OpenAI()

router = APIRouter()


class ChatMessage(BaseModel):
    role: str
    content: str
    id: str


@router.get("/greetings")
async def root():
    return "I like turtles"


@router.post("/chat")
async def get_chat(item: List[ChatMessage]):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            # prompt="Acá te daré algunas instrucciones de la conversación",
            messages=item
        )
        response_message = completion.choices[0].message
        return {"message": response_message}

    except Exception as e:
        print(f"Error al obtener la respuesta de AI: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Lo siento, hubo un error al procesar tu solicitud. Error: {e}"
        ) from e
