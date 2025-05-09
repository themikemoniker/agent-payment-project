# 🧠 CrewAI Flask App

A simple Flask web application that uses CrewAI to run an LLM-powered agent that responds to user input.

## ✨ Features

- Flask + Tailwind CSS frontend
- CrewAI agent powered by OpenAI (or any LLM via LiteLLM)
- Streams response output using Server-Sent Events (SSE)
- Clean, responsive UI
- .env-based API key config

## 🚀 Getting Started

1. Clone the repo

git clone https://github.com/YOUR_USERNAME/crewai-flask-app.git
cd crewai-flask-app

2. Set up a virtual environment

python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Set your OpenAI API key

Create a file called `.env` and add:

OPENAI_API_KEY=your-openai-key-here

5. Run the app

python app.py

Then open your browser to: http://localhost:5000

## 📁 Project Structure

crewai_flask_app/
├── app.py              # Flask backend + CrewAI logic
├── requirements.txt    # Python dependencies
├── .env                # Your API key (excluded from Git)
├── .gitignore
├── templates/
│   └── index.html      # Frontend UI with Tailwind + JS
└── venv/               # Python virtual environment (ignored)

## 🔄 Alternative LLMs

If you want to avoid OpenAI limits, you can use:
- OpenRouter
- Together.ai
- Local models via Ollama
- Any LiteLLM-compatible provider

## 📄 License

MIT — free to use, modify, and share!
