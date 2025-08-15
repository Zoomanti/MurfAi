# 🎙️ AI Voice Assistant

A full-stack **FastAPI-powered Voice-to-Voice AI Assistant** with speech recognition, contextual conversation memory, text-to-speech, and a sleek, responsive UI. This app allows users to have natural voice conversations with an AI, with chat history persistence per session.

![AI Voice Assistant Screenshot](https://via.placeholder.com/900x500.png?text=AI+Voice+Assistant+UI)  
*Replace with actual screenshot in production*

---

## ✨ Features

- 🎤 **Voice Recording**: Click-to-record audio directly from the browser.
- 🔊 **Text-to-Speech (TTS)**: Converts AI responses to natural-sounding speech using [Murf AI](https://murf.ai).
- 🧠 **LLM Integration**: Powered by **Google Gemini** for intelligent, context-aware responses.
- 📝 **Speech-to-Text (STT)**: Uses **AssemblyAI** to transcribe spoken audio.
- 💬 **Chat History**: Maintains conversation context across messages in a session.
- 🔁 **Session Management**: Unique session IDs, new session creation, and history clearing.
- 🎨 **Modern UI**: Responsive, animated, and user-friendly interface with real-time feedback.
- 🌐 **FastAPI Backend**: High-performance backend with async handling for audio and AI processing.
- 🧩 **Fallbacks**: Browser TTS fallback if Murf API fails or is not configured.

---

## 🔧 Technologies Used

| Tech | Purpose |
|------|--------|
| **FastAPI** | Backend API server |
| **HTML/CSS/JS** | Frontend UI (no frameworks) |
| **AssemblyAI** | Speech-to-Text (STT) |
| **Google Gemini** | Large Language Model (LLM) |
| **Murf AI** | Text-to-Speech (TTS) |
| **dotenv** | Environment variable management |
| **httpx** | Async HTTP client |
| **aiofiles** | Async file operations |
| **Uvicorn** | ASGI server |

---

## 📦 Prerequisites

Before running the app, ensure you have:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pypi.org/project/pip/)
- API keys for:
  - 🔑 **Murf AI** – [Get API Key](https://app.murf.ai/api-keys)
  - 🔑 **AssemblyAI** – [Get API Key](https://www.assemblyai.com/dashboard)
  - 🔑 **Google Gemini** – [Get API Key](https://ai.google.dev)

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-voice-assistant.git
   cd ai-voice-assistant
