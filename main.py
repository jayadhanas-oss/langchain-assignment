import os
import sys
from langchain_openai import ChatOpenAI

# 1. Safety check to make sure keys are set in the environment
if not os.environ.get("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY is not set in environment variables.")
    sys.exit(1)

# 2. Initialize the OpenAI model (LangChain automatically reads the OPENAI_API_KEY)
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 3. Define the prompt/input
prompt = "Tell me a fun fact about Tamil Nadu."
print(f"Input: {prompt}\n")

# 4. Invoke the model and display the result
response = llm.invoke(prompt)
print(f"Output: {response.content}")