time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []

for time_slot in time_slots:
    heart_rate = int(input(f"Enter your heart rate (in BPM) in the {time_slot}: "))
    heart_rates.append([time_slot, heart_rate])

total_heart_rate = 0
for time_slot, heart_rate in heart_rates:
    total_heart_rate += heart_rate

average_heart_rate = total_heart_rate / len(heart_rates)

print(f"Average heart rate today: {average_heart_rate} BPM")
