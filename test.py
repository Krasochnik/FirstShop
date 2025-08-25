import pytz

# Получаем список всех возможных временных зон
time_zones = pytz.all_timezones

for tz in time_zones:
    print(tz)