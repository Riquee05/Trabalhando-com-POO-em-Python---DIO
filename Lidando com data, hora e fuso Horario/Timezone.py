# Instalar PYTZ

# Comando no terminal - (pip install pytz)

from datetime import datetime # Importar as bibliotecas necessarias
import pytz # type: ignore

# Listar todos os fusos horarios disponiveis
for tz in pytz.all_timezones:
    print(tz)

# Obter a data e hora atual no fuso horário local
local_tz = pytz.timezone('America/Sao_Paulo')
local_time = datetime.now(local_tz)
print("Hora local:", local_time)

# Converter entre fusos horários
# Data e hora atual no fuso horário UTC
utc_time = datetime.now(pytz.utc)
print("Hora UTC:", utc_time)

# Converter de UTC para fuso horário específico
brasilia_tz = pytz.timezone('America/Sao_Paulo')
brasilia_time = utc_time.astimezone(brasilia_tz)
print("Hora em Brasília:", brasilia_time)

# Criar um objeto datetime com fuso horário específico
# Criar uma data e hora específica no fuso horário UTC
dt = datetime(2024, 6, 1, 12, 0, 0, tzinfo=pytz.utc)
print("Hora UTC:", dt)

# Converter para outro fuso horário
ny_tz = pytz.timezone('America/New_York')
ny_time = dt.astimezone(ny_tz)
print("Hora em Nova Iorque:", ny_time)

# Trabalhar com data e hora sem fuso horário (naive) e converter para com fuso horário (aware)
# Data e hora "naive" (sem fuso horário)
naive_time = datetime(2024, 6, 1, 12, 0, 0)
print("Hora naive:", naive_time)

# Tornar "aware" (com fuso horário)
aware_time = local_tz.localize(naive_time)
print("Hora aware:", aware_time)

#Dicas finais

# Sempre que possível, use objetos datetime "aware" para evitar confusões e bugs relacionados a fusos horários.
# Utilize a função astimezone() para converter entre fusos horários.
# A função localize() da pytz é usada para transformar datetime "naive" em "aware".

#Seguindo esses passos, você conseguirá manipular datas e horas com diferentes fusos horários de forma eficaz em Python.