🤖 AI-Powered Conversational Question Answering Chatbot
📌 Overview

This project is an AI-powered conversational Question Answering (Q&A) chatbot built using LangChain, Google Gemini LLM, and Streamlit.
The chatbot allows users to ask questions in a chat interface and generates intelligent responses using a Large Language Model (LLM).

The application demonstrates how Generative AI and prompt-based interaction can be used to build conversational assistants.

🚀 Features

Interactive chat-based interface

Powered by Google Gemini LLM

Built using LangChain framework

Session-based chat history

Simple and responsive Streamlit UI

Real-time AI-generated responses

🛠️ Tech Stack

Python

Streamlit

LangChain

Google Gemini API

python-dotenv

📂 Project Structure

Qna_chatBot
│
├── app.py              # Main Streamlit chatbot application
├── .env                # Environment variables (API keys)
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation

⚙️ Setup Instructions

Follow these steps to run the project locally.

1️⃣ Clone the Repository
git clone https://github.com/robinvatshr08/Qna_chatBot.git
cd Qna_chatBot
2️⃣ Create Virtual Environment
python -m venv env

Activate the environment

Mac / Linux
source env/bin/activate
Windows
env\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Create .env File

Create a .env file in the root directory.

GOOGLE_API_KEY=your_google_gemini_api_key

Get API key from:
https://makersuite.google.com/app/apikey

5️⃣ Run the Application
streamlit run app.py

The chatbot will open in your browser:

http://localhost:8501
