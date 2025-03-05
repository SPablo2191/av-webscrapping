import pandas as pd

# creamos un diccionario

example_data = {
    "name" : ["Pedro", "Juan", "Diego", "Luis", "Maria"],
    "age" : [23, 34, 45, 56, 67],
    "city" : ["Madrid", "Barcelona", "Sevilla", "Valencia", "Bilbao"]
}

df = pd.DataFrame(example_data)
print(df)