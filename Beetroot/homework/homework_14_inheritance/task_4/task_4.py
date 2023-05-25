from custom_exception import CustomException
from error_handling import error_handling

#%%
error1 = CustomException('This is "Error 1".')
print(error_handling(error1))
#%%
error2 = CustomException('This is "Error 2".')
print(error_handling(error2))
#%%
error3 = CustomException('This is "Error 3".')
print(error_handling(error3))
#%%
error4 = CustomException('This is "Error 4".')
print(error_handling(error4))
#%%
error5 = CustomException('This is "Error 5".')
print(error_handling(error5))
