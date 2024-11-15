from langchain_community.llms import OllamaLLM


llm =  OllamaLLM(model="phi3.5")

response = llm.generate("hello, why is the sky blue ")
print(response)
