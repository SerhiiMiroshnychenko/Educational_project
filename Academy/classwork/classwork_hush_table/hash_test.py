# # Python 3 code to demonstrate
# # working of hash()
#
# # initializing objects
# int_val = 6
# str_val = 'GeeksforGeeks'
# flt_val = (24.56, [1, 2])

# Printing the hash values.
# Notice Integer value doesn't change
# You'll have answer later in article.
# print("The integer hash value is : " + str(hash(int_val)))
# print("The string hash value is : " + str(hash(str_val)))
# print("The float hash value is : " + str(hash(flt_val)))


# class Emp:
#     def __init__(self, emp_name, id):
#         self.emp_name = emp_name
#         self.id = id
#
#     def __eq__(self, other):
#         # Equality Comparison between two objects
#         return self.emp_name == other.emp_name and self.id == other.id
#
#     def __hash__(self):
#         # hash(custom_object)
#         return hash((self.emp_name, self.id))
#         # return self.emp_name % self.id
#
#
# emp = Emp('Ragav', 12)
# print("The hash is: %d" % hash(emp))
#
# # We'll check if two objects with the same
# # attribute values have the same hash
# emp_copy = Emp('Ragav', 12)
# print("The hash is: %d" % hash(emp_copy))
# print(emp == emp_copy)


class NewList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.list_ = args

    def __hash__(self):
        return hash(self.list_)


n = NewList(1, 2, 3, 4, 5)
print(hash(n))
n.append(6)
print(n)
