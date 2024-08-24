# gender = input("enter gender\n male \t female\t others\n option :")
# if gender in ['male','female','others']:
#     age=int(input("age :"))
#     if gender in ['male', 'other']:
#         if age>=18 and age<=65:
#             print('eligible to vote')
#         else:
#             print('not eligible to vote')
# else:
#     if age >=21 and age <=45 :
#         print(' eligible ')
#     else:
#         print('not eligible ')
# else:
# print('invalid syntax')













operation=input("select the operation \n+\t-\t*\t/ :")
if operation in ['+','-','*','/']:
    a=int(input("a: "))
    b=int(input("b: "))
    if operation=='+':
        print(a+b)
    elif operation=='-':
        print(a-b)
    elif operation=='*':
        print(a*b)
    else:
        print(a/b)
else:
  print("invalid operation")