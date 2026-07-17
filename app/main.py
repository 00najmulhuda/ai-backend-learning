import ollama 

response = ollama.chat(
    model = "qwen2.5:3b",
    messages =  [
        {
            "role":"system",
            "content":"you are beginer freindly python teacher"
        },
        {
            "role":"user",
            "content":"whatis fastapi"
        },
        {
            "role":"assistant",
            "content":"FastAPI is modern python framework used to build API"
        },
        {
            "role":"user",
            "content":"who created it"
        }
    ],
    options = {
        "temperature":1.0,
        "num_predict":300
    }
)

print(response["message"]["content"])