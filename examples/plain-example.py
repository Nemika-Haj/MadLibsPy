from madlibspy import Madlibs as ml

data = ml.get()

answers = [input(f"Enter a {i}: ") for i in data["variables"]]

output = ml.convert(answers, data['questions'], data['text'])
print(output)

data = ml.get()

answers = [input(f"Enter a {i}: ") for i in data["variables"]]

output = ml.convert(answers, data['questions'], data['text'])
print(output)