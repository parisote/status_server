from fastapi import APIRouter, Body, HTTPException, status, Depends
#from fastapi_versioning import VersionedFastAPI, version
from src.controller.controller import Controller
from src.models.status import StatusModel
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.database import db
import os
from src.routes.security import get_api_key
from fastapi.security.api_key import APIKey

routes = APIRouter(prefix="/status")
collection = os.environ['COLLECTION_STATUS']

@routes.post("/", response_description="Add new status", response_model=StatusModel)
async def add_status(add_status: StatusModel = Body(...), api_key: APIKey = Depends(get_api_key)):
    obj = await Controller.insert_into_db(add_status, collection)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=obj)
