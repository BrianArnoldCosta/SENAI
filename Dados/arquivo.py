from os import system as limp
limp("cls")
from datetime import datetime

# with open("teste.txt", "r") as arquivo:
#     x = arquivo.read()
# print(x)

# with open("teste.txt", "a") as arquivo:
#     arquivo.write("Salvando dados no arquivo\n")

from os import system as limp
limp("cls")

for i in range(5):
    d = datetime.now()
    with open("teste.txt", "a") as arquivo:
        arquivo.write(f"{d} Salvando dados aqui {i}\n")