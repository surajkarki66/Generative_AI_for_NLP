
from src.agent import Agent
from src.model import OllamaModel
from src.tools import basic_calculator, reverse_string


if __name__ == "__main__":

    tools = [basic_calculator, reverse_string]
    
    model_service = OllamaModel
    model_name = "llama2"
    stop = "<|eot_id|>"

    agent = Agent(tools=tools, model_service=model_service, model_name=model_name, stop=stop)

    while True:
        prompt = input("Ask me anything: ")
        if prompt.lower() == "exit":
            break

        agent.work(prompt)
