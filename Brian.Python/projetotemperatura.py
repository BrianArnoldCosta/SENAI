from os import system as limp
limp("cls")

pressao = float(input("DIGITE A PRESSÃO ALTERIAL DO PACIENTE: "))
temperatura = float(input("DIGITE A TEMPERATURA DO PACIENTE: "))
bcpm = float(input("DIGITE OS BATIMENTOS CARDIACOS POR MINUTO DO PACIENTE: ")) #batimentos cardiacos por minuto

if temperatura <35:
    print(f"{temperatura}ºC: Hipotermia")
elif 35 <= temperatura <= 37.5:
    print(f"{temperatura}ºC: Normal")
elif 37.6 <= temperatura <= 39:
    print(f"{temperatura}ºC: Febre Leve")
elif temperatura >39:
    print(f"{temperatura}ºC: Febre Alta") 

if bcpm > 100:
    print(f"{bcpm}BPM: PACIENTE COM TAQUICARDIA")
elif bcpm <60 :
    print(f"{bcpm}BPM: PACIENTE COM BRADICARDIA")
elif 60 <= bcpm <= 100 :
    print(f"{bcpm}BPM: PACIENTE NORMAL")

if pressao > 14.1:
    print(f"{pressao}: PACIENTE COM PRESSÃO ALTA")
elif pressao < 10.1:
    print(f"{pressao}: PACIENTE COM PRESSÃO BAIXA")
elif 10.1< pressao < 14:
    print(f"{pressao}: PACIENTE COM PRESSÃO NORMAL")


if 35 <= temperatura <=39 and 60<= bcpm <= 100 and 10.1< pressao < 14:
    print ("CASO ATENDIMENTO NORMAL")

elif temperatura >39 and  bcpm > 100 and pressao > 14.1:
    print ("CASO ATENDIMENTO GRAVE")

elif temperatura <35 and  bcpm < 60 and pressao < 10.1:
    print ("CASO DE ATENDIMENTO URGENTE")