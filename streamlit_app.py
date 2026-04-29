import threading
import uvicorn
from main import app  # твой FastAPI код

def run_api():
    uvicorn.run(app, host="0.0.0.0", port=8000)

threading.Thread(target=run_api, daemon=True).start()

import streamlit as st
st.title("API is running")
