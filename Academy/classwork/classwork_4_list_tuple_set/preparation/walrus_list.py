# вивід кубів чисел від 0 до 10 не більших 500
print(walrus_list := [y for x in range(11) if (y := x**3) <= 500])
