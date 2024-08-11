# a=int(input("enter the value of a:"))
# print(a,type(a))
# b=float(input("b :"))
# print(b,type(b) )
# c=complex(input("c:"))
# print(c,type(c))
 

# INTERGER "INT()"
a=int("100")
print(a,type(a))
# if we given the flaot value in int it will show the value error "string" if we use str
a=int("10.5")
print(a,type(a))
# if we given the complex value in int it will show the value error "string" if we use str
a=int("1+2j")
print(a,type(a))
# if we given the string value in int it will show the value error "string" if we use str
a=int("don")
print(a,type(a))
# if we given the with out string in the int it will show the output value it is an it value 
a=int(100)
print(a,type(a))
# if we given the with out string in the int it will show the output value it is the float value
a=int(10.5)
print(a,type(a))
# if we given the without string in the int it will not show the out put  value it is the complex value (type error)
a=int(1+2j)
print(a,type(a))



# FLOAT ()
# if we give the float value in int it will show the the output with using the string
a=float("100")
print(a,type(a))
# if we give the float value in the float it will show the output with using the string
a=float("100.5")
print(a,type(a))
# if we give the float value in the complex it will show the value error using the string 
a=float("1+2j")
print(a,type(a))
# if we give the float value in the str it will show the value error using  the string 
a=float("don")
print(a,type(a))
# if we give the float value in int it will show the output without using string 
a=float(100)
print(a,type(a))
# if we give the float value in float it will show the output without using the string 
a=float(100.5)
print(a,type(a))
# if we give the float value in complex it will not show the out put it will show the type error
a=float(1+2j)
print(a,type(a))



# COMPLEX ()
# if we give the complex value it wil show the output with using string
a=complex("100")
print(a,type(a))
# if we give the complex value it will show the out put with using the string
a=complex("10.5")
print(a,type(a))
# if we give the complex value it wil show the output with using the string 
a=complex("1+2j")
print(a,type(a))
# if we give the complex value it will not show the output with using string
a=complex("don")
print(a,type(a))
# if we give the complex value it will show the out put (int)
a=complex(100)
print(a,type(a))
# if we give the complex value it will show the out put (float)
a=complex(10.5)
print(a,type(a))
# if we give the complex value it will show the output (complex)
a=complex(1+2j)
print(a,type(a))




# STRING (STR)
# if we give the string value it will show the output (int)
a=str("10")
print(a,type(a))
# if we give the string value it will show the output (float)
a=str("10.5")
print(a,type(a))
# if we give the string value it will show the output (complex)
a=str("1+2j")
print(a,type(a))
# if we give the string value it will show the output (int) with out double codes
a=str(10)
print(a,type(a))
# if we give the string value it wil show the output (float) with out double codes
a=str(1+2j)
print(a,type(a))

