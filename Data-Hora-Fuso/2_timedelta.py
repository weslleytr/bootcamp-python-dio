from datetime import timedelta, datetime

tipo_carro = "C" # P para passeio, C para carga
tempo_passeio = 30
tempo_carga = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_passeio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada} ")
elif tipo_carro == "C":
    data_estimada = data_atual + timedelta(minutes=tempo_carga)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada} ")
else:
    print("Tipo de carro inválido. Use 'P' para passeio ou 'C' para carga.")

