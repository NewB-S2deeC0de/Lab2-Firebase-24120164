from datetime import datetime, timezone
from backend.firebase_config import get_db

db = get_db()

def save_message(session_id: str, role: str, content: str):
	"""Lưu 1 tin nhắn vào database"""
	doc = {
		"role": role, 
		"content": content, 
		"timestamp": datetime.now(timezone.utc)
	}

	# collection 'chats' -> document 'session_id' -> collection 'message'
	db.collection("chats").document(session_id).collection("messages").add(doc)

def load_chat_history(session_id: str, limit: int = 10) -> list:
	"""Tải chat history lên, sắp xếp theo thời gian"""
	query = (
		db.collection("chats")
		.document(session_id)
		.collection("messages")
		.order_by("timestamp")
		.limit(limit)
	)

	docs = query.stream()
	history = []

	for doc in docs:
		# Loại bỏ field doc.id, link lưu trữ của object doc trên server, thông tin về thời gian tạo, trạng thái kết nối...
		data = doc.to_dict()
		history.append({
			"role": data.get("role"),
			"content": data.get("content")
		})

	return history
