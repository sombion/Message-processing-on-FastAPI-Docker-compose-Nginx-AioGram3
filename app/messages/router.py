from fastapi import APIRouter


router = APIRouter(
	prefix="/api/v1",
	tags={"АПИ работы с сообщениями"}
)


@router.get('/messages')
async def show_all_messages():
	return {"status": 200}

@router.post('/message')
async def send_message():
    return {"status": 200}