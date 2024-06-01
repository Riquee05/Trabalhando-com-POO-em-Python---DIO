import datetime # importando modulo Datetime

#classe Date
# A classe date é usada para representar uma data (ano, mês, dia).

data = datetime.date(2024, 6, 1)
print(data)  # Output: 2024-06-01

# Obter Data atual

data_hoje = datetime.date.today()
print(data_hoje)

# Acessar atributos da classe

ano = data.year
mes = data.month
dia = data.day
print(ano, mes, dia)  # Output: 2024 6 1

#classe Time
# A classe time é usada para representar um horário (hora, minuto, segundo, microsegundo).

horario = datetime.time(14, 30, 15)
print(horario)  # Output: 14:30:15

# Acessar atributos da classe

hora = horario.hour
minuto = horario.minute
segundo = horario.second
microsegundo = horario.microsecond
print(hora, minuto, segundo, microsegundo)  # Output: 14 30 15 0

#classe DateTime
# A classe datetime combina uma data e um horário.

data_hora = datetime.datetime(2024, 6, 1, 14, 30, 15)
print(data_hora)  # Output: 2024-06-01 14:30:15

# obter data e hora atual

agora = datetime.datetime.now()
print(agora)

# Acessar atributos da classe

ano = agora.year
mes = agora.month
dia = agora.day
hora = agora.hour
minuto = agora.minute
segundo = agora.second
microsegundo = agora.microsecond
print(ano, mes, dia, hora, minuto, segundo, microsegundo)

# Operações em Datas e Horas

data1 = datetime.date(2024, 6, 1)
data2 = datetime.date(2024, 6, 10)
diferenca = data2 - data1
print(diferenca.days)  # Output: 9

# Adicionar ou Subtrair Tempo

from datetime import timedelta

data_hora_atual = datetime.datetime.now()
nova_data_hora = data_hora_atual + timedelta(days=10, hours=2)
print(nova_data_hora)

# Converter data e hora para String

data_str = data_hora.strftime("%Y-%m-%d %H:%M:%S")
print(data_str)  # Output: 2024-06-01 14:30:15

# Converter de String para data e hora

data_str = "2024-06-01 14:30:15"
data_hora = datetime.datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
print(data_hora)  # Output: 2024-06-01 14:30:15

