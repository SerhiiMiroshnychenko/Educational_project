# Can tuples change?
tuples_one = (1, "2", [3, "4"])
print("The first version:", tuples_one)
try:
    tuples_one[0] = "1"
    print("Tuples can change! The second version:", tuples_one)
except TypeError:
    print("Tuples can not change!")
try:
    tuples_one[2][0] = "3"
    print("Tuples can change! The second version:", tuples_one)
except TypeError:
    print("Tuples can not change!")
