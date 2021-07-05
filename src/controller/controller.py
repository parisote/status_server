from fastapi import APIRouter, Body, HTTPException, status, Depends
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from src.database import db
import os

class Controller:

    @staticmethod
    async def insert_into_db(obj, collection):
        assert isinstance(obj.id, ObjectId)
        add_obj = jsonable_encoder(obj)
        new_obj = await db[collection].insert_one(add_obj)
        created_obj = await db[collection].find_one({"_id": new_obj.inserted_id})
        return created_obj
