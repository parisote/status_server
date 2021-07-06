from fastapi import APIRouter, Body, HTTPException, status, Depends
#from fastapi_versioning import VersionedFastAPI, version
from src.models.message import MessageModel
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.database import db
import requests
import os
from src.routes.security import get_api_key
from fastapi.security.api_key import APIKey
from src.controller.controller import Controller


routes = APIRouter(prefix="/discord")
collection = os.environ['COLLECTION_DISCORD']
bot_token = os.environ['TELEGRAM_KEY']
telegram_id = os.environ['TELEGRAM_TEST_GROUP']

@routes.post("/", response_description="Add new message to discord", response_model=MessageModel, tags=['Discord'])
async def add_message(add_message: MessageModel = Body(...), api_key: APIKey = Depends(get_api_key)):
    obj = Controller.insert_into_db(add_message, collection)
    await send_message_telegram(add_message)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=obj)


async def send_message_telegram(message : MessageModel):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + telegram_id + '&parse_mode=Markdown&text=' + message.value
    response = requests.get(send_text)
