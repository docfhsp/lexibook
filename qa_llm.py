from langchain.llms import OpenAI
from callback import LexiBookCallbackHandler
from langchain.callbacks.base import BaseCallbackManager

class QaLlm():

    def __init__(self) -> None:
        manager = BaseCallbackManager([LexiBookCallbackHandler()])
        #Need to play with temperature to generate different questions when program is run again
        self.llm = OpenAI(temperature=0, callback_manager=manager, model_name="gpt-4")

    def get_llm(self):
        return self.llm