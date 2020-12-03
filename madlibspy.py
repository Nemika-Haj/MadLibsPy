import requests, json, random

class Madlibs:
  def get(path=None):
    if path:
      with open(path, "r") as f:
        data = json.load(path)
    else:
      data = random.choice(requests.get("https://api.bytestobits.dev/madlibs").json())
    
    return data
  
  def convert(answers:list, questions:int, text:str):
    en = 0
    for i in range(questions):
      text = text.replace("{" + str(en) + "}", answers[en])
      en += 1
    return text
