import _ctypes

# s.isidentifier() Визначає, чи є цільовий рядок дійсним ідентифікатором Python
print('foo32'.isidentifier())
print('32foo'.isidentifier())
print('foo$32'.isidentifier())

a = 10
print(id(a))

print(_ctypes.PyObj_FromPtr(140707404436552))
