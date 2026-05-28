daily_temp = [32.5, -4.0, 0.0, 45.2, -12.3, 105.0, 28.4]
recorded_temperatures = []

for temp in daily_temp:
    if temp < 0.0:
        continue
    elif temp >= 100.0:
        break
    recorded_temperatures.append(temp)

print(recorded_temperatures)