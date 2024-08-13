# we have 3 logical operator they are "AND","OR",NOT
# this are operator are used to compare two condisiton 
# this operator returns to boolean
# truth table "AND"
# c1 c2 R
# F  F  F
# F  T  F
# T  F  F
# T  T  T
# TRUTH TABLE "OR"
# c1 c2 R
# F  F  F
# T  F  T
# F  T  T
# T  T  T
# TRUTH TABLE "NOT"
# C R
# T F
# F T
# EXAMPLE PROGRAM 
a,b,c=10,20,10
print(a==b and a==c)
print(a==b or a==c)
print(not a==c)
print(a==c and not a==b or not a*2==c-10 or not a<b and b+10==c)   