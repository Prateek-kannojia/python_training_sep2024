# print the math table of a number for upto multiples of 20
input_number=int(input('enter a number to print table '))
for i in range (1,21):
    # print(f'{i} * {input_number}=',input_number*i)
    print('%2d * %2d = %3d'%(i,input_number,input_number*i))