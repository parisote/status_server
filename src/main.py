from fastapi import FastAPI, Request, Depends
from src.routes.status import status
from src.routes.message import discord
#from fastapi_versioning import VersionedFastAPI, version

import time

app = FastAPI(docs_url=None, redoc_url=None)

#GET ROOT
@app.get("/")
async def root():
    return {"message": "Hello World"}


# EVENTO STARTUP
@app.on_event("startup")
async def startup():
    print("Connecting...")


# ROUTES
app.include_router(status.routes)
app.include_router(discord.routes)


# EVENTO SHUTDOWN
@app.on_event("shutdown")
def shutdown_event():
    print("Shutdown app")

#app = VersionedFastAPI(app, version_format='{major}', prefix_format='/v{major}')
