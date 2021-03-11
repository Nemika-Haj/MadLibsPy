from madlibspy import Madlibs

madlib = Madlibs(API_TOKEN, random=False, fp="custom_madlib.json") # Seting random=False requires a filepath (fp)

answers = [input(f"Enter a/an {i}: ") for i in madlib.variables]

text = answers >> madlib

print(madlib.title)
print(text)