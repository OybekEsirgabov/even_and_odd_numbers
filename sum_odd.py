#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
a = 4679
b = a//1000
c = a//100-b*10
d = a//10-c*10-b*100
e = a-b*1000-c*100-d*10
print(e%2*e+d%2*d+c%2*c+b%2*b)