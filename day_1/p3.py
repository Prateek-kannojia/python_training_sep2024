# perfect square
import math
num=int(input('enter a number to check if it is a perfect square'))
root=math.sqrt(num)
root=math.floor(root)
if((root*root)==num):
    print(f'{num} is a perfect square')
else:
    print(f'{num} is not a perfect square')
