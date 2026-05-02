from fastapi import FastAPI
from backend.schemas.chat import ChatRequest
from backend.services.ai_service import get_ai_response
from backend.services.firebase_service import save_message, load_chat_history

app = FastAPI()

@app.post("/api/chat")
def chat_endpoint(request: ChatRequest):
    
	save_message(request.session_id, "user", request.message)

	chat_history = load_chat_history(request.session_id)

	reply = get_ai_response(chat_history)

	save_message(request.session_id, "assistant", reply)
	
	return {"bot_reply": reply}
