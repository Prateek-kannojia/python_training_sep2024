input_number=int(input('enter a number'))
number_digit_sum=0
lucky_num = 0
temp=0
while (input_number>0):
    lucky_digit=int(input_number%10)
    print(lucky_digit)
    number_digit_sum+=lucky_digit
    input_number=int(input_number/10)
    if number_digit_sum >10:
        lucky_num=number_digit_sum
        while(lucky_num>0):
            lucky_digit=lucky_num%10
            lucky_num=lucky_num//10
            temp+=lucky_digit

print('lucky digit is ',temp)
