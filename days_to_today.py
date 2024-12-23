from datetime import datetime, timedelta

current_date = (datetime.now())

days_ago = current_date - timedelta(days=171)

print(f"Дата 171 дней назад: {days_ago.strftime('%Y-%m-%d')}")