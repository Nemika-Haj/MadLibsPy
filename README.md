# **MadlibsPy**
Create your own madlibs game!

## **Installation**
Use `python -m pip install madlibspy`

## **Example**
```py
import madlibspy as madlibs

data = madlibs.Madlibs(API_TOKEN) # You need an API token from api.bytestobits.dev

answers = [input(f"Enter a/an {i}: ") for i in data.variables]

text = data.convert(answers)

"""text = answers >> data
This also works, it's a faster way of convertion.
"""
print(data.title)
print(text)
```
*And much more!*

## **Documentation**
Coming soon...!