# second smmalest digit in a number
number=8279
smallest=9
second_smallest=9
while(number>0):
    digit=number%10
    number=(number//10)
    if(digit<smallest):
        second_smallest=smallest
        smallest=digit
print(second_smallest)