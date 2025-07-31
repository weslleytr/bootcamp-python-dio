import datetime

data_hora_atual = datetime.datetime.now()
data_hora_str = "2025-07-31 20:19"
mascara = "%d/%m/%Y %H:%M %a"
mascara_en = "%Y-%m-%d %H:%M"

print("Data e hora atual:", data_hora_atual.strftime(mascara))

data_convertida = datetime.datetime.strptime(data_hora_str, mascara_en)
print("Data e hora convertida:", data_convertida)
print(type(data_convertida))