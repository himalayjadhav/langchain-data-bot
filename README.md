# 🧠 Local LLM Data Analyst Bot with LangChain + Ollama + Llama3

Interact with your CSV files using **natural language**, all **offline**, with **no API keys** needed.

This project uses LangChain and Ollama to run a Llama3-based chatbot that can understand your questions and analyze CSV data using Python + Pandas behind the scenes.

---

## 🚀 Features

- 💬 Ask natural language questions like:  
  *“What are the top 5 games by sales in North America?”*
- 📊 Automatically runs Python code (via `pandas`) to answer
- 🧱 Powered by **LangChain** and **Llama3 via Ollama**
- 🔐 100% Local — No internet or API keys required
- 📂 Works with any CSV file

---

## 🛠️ Tech Stack

- Python 3.10  
- [LangChain](https://www.langchain.com/)  
- [Ollama](https://ollama.com/) (runs Llama 3 locally)  
- Pandas  
- Llama 3 model (e.g., `llama3` or `llama3:8b`)

---

## 🖼️ How It Works

1. You load a CSV file (e.g., video game sales)
2. Ask questions like “Which game sold most in Japan?”
3. LangChain + Llama 3 understands your question
4. It writes and runs Python code on your CSV
5. You get clean, accurate answers — with no coding!

---

## ⚙️ How to Run Locally

1. **Install Ollama**  
   https://ollama.com/download  
   (Run `ollama run llama3` once to install the model)

2. **Clone this repo & install Python dependencies**
   ```bash
   pip install -r requirements.txt
   
3.  Place your CSV file in the project folder
   (e.g., vgsales.csv)

4.  Run the bot
   python main.py

5.  Ask your questions 🎉

   
   Ask a question about your data (or type 'exit'): List top 5 games in North America

 The top 5 games in North America are:
Wii Sports, Super Mario Bros., Mario Kart Wii, Wii Sports Resort, and Pokemon Red/Blue.

✨ Why This Is Different

🔌 Runs Locally: No OpenAI, no cloud, no API cost

📦 Reusable: Swap in any CSV dataset

🔍 Explainable: See the Python code it runs

🧠 LLM Smartness: Uses modern open-source LLMs

🏗️ Future Improvements

    GUI interface (e.g., with Streamlit or Gradio)

    Automatic CSV loader with summaries

    Export results as a report

