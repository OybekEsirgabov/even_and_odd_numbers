#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
a = 4673
b = a//1000
c = a//100-b*10
d = a//10-c*10-b*100
e = a-b*1000-c*100-d*10
print((e+1)%2+(d+1)%2+(c+1)%2+(b+1)%2)