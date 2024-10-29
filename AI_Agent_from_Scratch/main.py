
from src.agent import Agent
from src.model import OllamaModel
from src.tools import capitalize_words, reverse_string, fetch_trending_news


if __name__ == "__main__":

    tools = [capitalize_words, reverse_string, fetch_trending_news]
    
    model_service = OllamaModel
    model_name = "llama2"
    stop = "<|eot_id|>"

    agent = Agent(tools=tools, model_service=model_service, model_name=model_name, stop=stop)

    while True:
        prompt = input("Ask me anything: ")
        if prompt.lower() == "exit":
            break

        agent.work(prompt)
