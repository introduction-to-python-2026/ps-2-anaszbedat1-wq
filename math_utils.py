def find_max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3: 
      return num1 
    if num2 > num1 and num2 > num3: 
      return num2 
    return num3
    num1 = 1
num2 = 3
num3 = -1
max_num = find_max_number(num1, num2, num3)
print("The maximum number is:", max_num)
def find_mean(num1, num2, num3):
   num_mean = (num1 + num2 + num3)/3 
   return num_mean
    num1 = 1
num2 = 3
num3 = 2
mean_value = find_mean(num1, num2, num3)
print("The mean is:", mean_value)
def find_mean_std(num1, num2, num3):
  mean = find_mean(num1, num2, num3)
  num_std = ((num1-mean)**2 + (num2-mean)**2 + (num3-mean)**2 / 3)**0.5
def find_mean(num1, num2, num3):
   num_mean = (num1 + num2 + num3)/3
   return num_mean

def find_mean_std(num1, num2, num3):
   num_mean = find_mean(num1, num2, num3)
   num_std = (((num1 - num_mean)**2 + (num2 - num_mean)**2 + (num3 - num_mean)**2)/3)**0.5
   return num_mean, num_std

def find_mean_std(num1, num2, num3):
   num_mean = find_mean(num1, num2, num3)
   num_std = (((num1 - num_mean)**2 + (num2 - num_mean)**2 + (num3 - num_mean)**2)/3)**0.5
   return num_mean, num_std
