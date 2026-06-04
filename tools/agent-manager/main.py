from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "openai:gpt-5-mini",
    base_url="https://models.github.ai/inference")

def main():
    response = model.invoke("What is the meaning of life?")
    print(response)

if __name__ == "__main__":
    main()
