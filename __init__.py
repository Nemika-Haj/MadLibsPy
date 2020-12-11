__version__ = "1.0-Public"

import requests, json

class Madlibs:
  def get(path=None):
    if path:
      with open(path, "r") as f:
        data = json.load(path)
    else:
      data = requests.get("https://api.bytestobits.dev/madlibs").json()
    
    return data
  
  def convert(answers:list, questions:int, text:str):
    en = 0
    for i in range(questions):
      text = text.replace("{" + str(en) + "}", answers[en])
      en += 1
    return text