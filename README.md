# Video Summarizer Agentic AI

An AI-powered Streamlit web app that analyzes uploaded video content using **Google Gemini 2.0 Flash**, enhanced by **DuckDuckGo search** and managed via **Phidata Agents**. This multimodal agent can extract insights from videos, answer user queries, and enhance responses with supplementary web data — all in real-time.

---

##  Features

-  **Video Understanding with Gemini 2.0 Flash**
-  **Web-Augmented Answers via DuckDuckGo**
-  **Interactive Natural Language Interface**
-  **Drag-and-Drop Video Upload**
-  **Real-time Summarization and Insight Generation**
-  **Phidata Agent Framework for tool chaining**
-  **Built with **Streamlit** for rapid prototyping**

---

## How It Works

1. **Upload a video file** (`.mp4`, `.mov`, `.avi`)
2. Enter a **question or query** about the video
3. The system:
   - Uploads the video to **Google Gemini 2.0 Flash**
   - Uses **Phidata's Agent API** to generate an intelligent analysis
   - Leverages **DuckDuckGo search** to supplement with real-time info
4. Returns a **detailed, user-friendly response** in natural language

---

## 🛠️ Tech Stack

| Layer          | Tools & Libraries                                |
|----------------|---------------------------------------------------|
|  LLM         | Google Gemini 2.0 Flash via `phi.model.google`   |
|  Agent Mgmt  | Phidata Agent (`phi.agent.Agent`)                |
|  Web Search  | DuckDuckGo Tool from `phi.tools`                 |
|  UI         | Streamlit (`st.file_uploader`, `st.text_area`, etc.) |
|  Temp Files  | Python `tempfile` for secure file management     |
|  Env Vars    | `dotenv` for managing API keys                   |

---

## 📁 Project Structure

```bash
Video-Summarizer-Agentic-AI/
│
├── app.py                 # Main Streamlit app script
├── .env                  # Contains your GOOGLE_API_KEY
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## Clone the repo
git clone https://github.com/your-username/Video-Summarizer-Agentic-AI.git

cd Video-Summarizer-Agentic-AI

## Create a virtual environment
python -m venv venv
venv\Scripts\activate    # Windows
OR
source venv/bin/activate # macOS/Linux

Install requirements - pip install -r requirements.txt

Add your Google API Key - GOOGLE_API_KEY=your-google-api-key-here

Run - streamlit run app.py

---

## Example Prompt
Video Insight: “Summarize the business discussion and identify key strategies mentioned.”
Result: Detailed summary of the speaker’s points + web-based enhancements.
