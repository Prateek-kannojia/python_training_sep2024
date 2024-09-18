import sys
state_capital=sys.argv[1:]
state=list() 
capital=list()
newstate=''
newcapital=''
def state_capital_split():      
    for i in range(0,len(state_capital)):
        parts=state_capital[i].split()
        state.append(parts[0])
        capital.append(parts[1])

state_capital_split()

print(state)
print(capital)
