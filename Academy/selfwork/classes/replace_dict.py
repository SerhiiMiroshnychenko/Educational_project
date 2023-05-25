class Mirror(dict):
    def reflect(self):
        return {value: key for key, value in self.items()}
#%%
test_dict = Mirror()
keys = 'abcd'
for value, key in enumerate(keys, start=1):
    test_dict[key] = value
print(test_dict)
print(test_dict['c'])
print(test_dict.get('v', 'not found'))
test_dict = test_dict.reflect()
print(test_dict)
#%%
td_2 = Mirror()
k = ('one', 'two', 'three')
v = ('first', 'second', 'third')
for i in range(len(k)):
    td_2[k[i]] = v[i]
print(td_2)
td_2 = td_2.reflect()
print(td_2)
