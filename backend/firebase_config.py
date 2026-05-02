import streamlit as st
import firebase_admin

from firebase_admin import credentials, firestore

def init_firebase():
	# Kiểm tra xem app đã được khởi tạo chưa, tránh khởi tạo 2 lần 
	if not firebase_admin._apps:
		# Đường dẫn tới file chứa SDK Key
		cred = credentials.Certificate("serviceAccountKey.json")
		firebase_admin.initialize_app(cred)

def get_db():
	init_firebase()
	return firestore.client()

