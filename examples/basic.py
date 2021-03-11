import madlibspy as madlibs

data = madlibs.Madlibs(API_TOKEN)

answers = [input(f"Enter a/an {i}: ") for i in data.variables]

text = data.convert(answers)

"""text = answers >> data
This also works, it's a faster way of convertion.
"""
print(data.title)
print(text)