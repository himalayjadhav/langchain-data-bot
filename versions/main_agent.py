from langchain_ollama import OllamaLLM
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd

# Load dataset
df = pd.read_csv("vgsales.csv")

# Initialize local LLM
llm = OllamaLLM(model="llama3")

# Create pandas agent
agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    allow_dangerous_code=True
)

# Interaction loop
while True:
    query = input("Ask a question about your data (or type 'exit'): ")
    if query.lower() == "exit":
        break
    # print(agent.invoke(query))
    print("⏳ Processing...")
    print(agent.run(query))
    print("✅ Done.")
  
  