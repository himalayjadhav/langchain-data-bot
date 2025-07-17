from langchain_ollama import OllamaLLM
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd

# Load your dataset
df = pd.read_csv("vgsales.csv")

# Connect to the Ollama model
llm = OllamaLLM(model="llama3")

# Enable dangerous code execution (for pandas agent)
agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)

# Ask questions
while True:
    query = input("Ask a question about your data (or type 'exit'): ")
    if query.lower() == "exit":
        break
    print(agent.invoke(query))
