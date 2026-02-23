# temperature_monitoring_system.py

def monitor_temperature(temps):
    hottest = max(temps)
    coldest = min(temps)

    updated_temps = []
    extreme_days = 0

    for t in temps:
        if t > 45:
            updated_temps.append("Heat Alert")
        else:
            updated_temps.append(t)

        if t > 40:
            extreme_days += 1

    print("\nHottest Temperature:", hottest)
    print("Coldest Temperature:", coldest)
    print("Updated Temperature List:", updated_temps)
    print("Number of Extreme Days (>40°C):", extreme_days)


temps_input = list(map(float, input("Enter daily temperatures: ").split()))
monitor_temperature(temps_input)