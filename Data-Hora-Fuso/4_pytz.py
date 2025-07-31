import datetime
import pytz

date_oslo = datetime.datetime.now(pytz.timezone('Europe/Oslo'))
date_sp = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))

print(f"Data e hora em Oslo: {date_oslo.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
print(f"Data e hora em São Paulo: {date_sp.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")