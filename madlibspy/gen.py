from .errors import APIError
from typing import Union
from PyJS import *
from PyJS.modules import fs

import requests
import forbiddenfruit as ff

API_URL = "https://api.bytestobits.dev/madlibs"

__all__ = (
    "Madlibs"
)

class Madlibs:
    def __init__(self, random:bool=True, fp:str=None):
        if random:
            try:
                self.data = requests.get(API_URL)
                if not self.data.status_code == 200:
                    raise APIError("There was an error fetching data from the API (https://api.bytestobits.dev/)")
                else:
                    self.data = self.data.json()
            except requests.ConnectionError as e:
                raise e
            except APIError as e:
                raise e
        else:
            self.data = JSON.parse(fs.createReadStream(fp))

        self.title = self.data['title']
        self.variables = self.vars = self.data['variables']
        self.questions = self.data['questions']
        self.text = self.data['text']

    def get_questions(self) -> tuple:
        return tuple(self.data['variables'])

    def convert(self, answers:list) -> str:
        text = self.data['text']
        for i in range(self.data['questions']):
            text = text.replace("{" + str(i) + "}", answers[i])
        
        return text

"""
Overwrite the list, tuple __rshift__ function for faster convertion

Example:
list >> Madlibs
"""

@ff.curses(list, "__rshift__")
@ff.curses(tuple, "__rshift__")
def ans_rshift(self:Union[list, tuple], other:Madlibs):
    return other.convert(self)