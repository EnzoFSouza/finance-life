import json

with open("finance-life/ativos.txt", "r") as f:
    ativos = json.load(f)
    print(ativos)
    f.close()

print(type(ativos)) #lista
for i in range(len(ativos)):
    print(ativos[i])