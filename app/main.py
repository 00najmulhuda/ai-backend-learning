import ollama 

response = ollama.chat(
    model = "qwen2.5:3b",
    messages =  [
        {
            "role":"user",
            "content":"explain FastAPI is simplete words and in short"
        }
    ]
)

print(response["message"]["content"])