from fastapi import Query
from pydantic import BaseModel


class SMessages(BaseModel):
    
    user_name: str = Query(min_length=1)
    user_message: str = Query(min_length=1, max_length=300)