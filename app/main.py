from fastapi import FastAPI

from app.messages.router import router as router_messages

app = FastAPI()

app.include_router(router_messages)