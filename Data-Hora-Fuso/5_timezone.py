from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))

print(f"Data e hora em Oslo: {data_oslo}")
print(f"Data e hora em São Paulo: {data_sp}")