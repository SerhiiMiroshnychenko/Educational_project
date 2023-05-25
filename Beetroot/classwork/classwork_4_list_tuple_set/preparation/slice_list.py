days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[1:4])
print(days[2:])
print(days[:4])
print(days[-3:])
for day in days[-2:]:
    print(day.upper())
days1 = days  # взаємозалежні копії
days2 = days[:]  # незалежна копія
print(days1 == days2)
print(days1)
print(days2)
days.append("week")
days1.append("month")
days2.append("year")
print(days)
print(days1)
print(days2)
print("Wednesday" in days)
print("year" in days)
print("Monday" not in days)
print(1 not in days)
