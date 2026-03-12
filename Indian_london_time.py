h = int(input("Enter hour in India: "))
m = int(input("Enter minutes in India: "))
total_minutes = h*60 + m - 330   # 330 minutes = 5 hours 30 minutes
london_hour = (total_minutes // 60) % 24
london_minute = total_minutes % 60

print(f"London Time: {london_hour}:{london_minute}")
