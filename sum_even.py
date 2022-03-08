#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
a = 4673
b = a//1000
c = a//100-b*10
d = a//10-c*10-b*100
e = a-b*1000-c*100-d*10
print((e+1)%2*e+(d+1)%2*d+(c+1)%2*c+(b+1)%2*b)