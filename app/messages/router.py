from fastapi import APIRouter

from app.messages.schemas import SMessages

router = APIRouter(
	prefix="/api/v1",
	tags={"АПИ работы с сообщениями"}
)


@router.get('/messages/')
async def show_all_messages() -> list[SMessages]:
	return [{"user_name": "one", "user_message": "text 1"}, {"user_name": "two", "user_message": "text 2"}]

@router.post('/message/')
async def send_message(message: SMessages) -> dict:
    return {"status": 200}