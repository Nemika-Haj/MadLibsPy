# MadLibsPy

## How to use
> Here's an example of how to use MadLibsPy
```py
from madlibspy import Madlibs as ml

data = ml.get()

answers = [input(f"Enter a {i}: ") for i in data["variables"]]

output = ml.convert(answers, data['questions'], data['text'])
print(output)
``` 