from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.tools import PythonREPLTool

import pandas as pd

# Load your dataset
df = pd.read_csv("vgsales.csv")

# Set up LLM
llm = OllamaLLM(model="llama3")

# Define a custom tool that has access to the dataframe
def run_code(query):
    local_vars = {"df": df}
    try:
        exec("result = " + query, {}, local_vars)
        return local_vars["result"]
    except Exception as e:
        return str(e)

custom_tool = Tool(
    name="pandas_query",
    func=run_code,
    description="Useful for querying the pandas dataframe `df`"
)

# Create the agent with the Python REPL tool
agent = initialize_agent(
    tools=[PythonREPLTool(), custom_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Ask questions
while True:
    query = input("Ask a question about your data (or type 'exit'): ")
    if query.lower() == "exit":
        break
    print("⏳ Processing...\n")
    print(agent.run(query))
    print("✅ Done.\n")
