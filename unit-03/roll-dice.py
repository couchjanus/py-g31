import random
arts = []

def init():
    arts = []
    start_rec = chr(9484) + chr(9472)*9 + chr(9488)
    end_rec = chr(9492) + chr(9472)*9 + chr(9496)
    
    start_line = chr(9474) + chr(32)*2
    end_line = chr(32)*2 + chr(9474)
    
    for j in (1,2,3,4,5,6):
        if j == 1:
            l1 = l3 = chr(32)*5
        elif j in (2,3):
            l1 = chr(9679) + chr(32)*4
            l3 = chr(32)*4 + chr(9679)
        elif j in (4,5, 6):
            l1 = l3 = chr(9679) + chr(32)*3 + chr(9679)
            if j == 6:
                l2 = chr(9679) + chr(32)*3 + chr(9679)
        if j in (1,3,5):
            l2 = chr(32)*2 + chr(9679) + chr(32)*2  
        if j in (2,4):
            l2 = chr(32)*5
            
        tmp = start_rec + '\n' + start_line +l1 + end_line +'\n'+start_line +l2 + end_line +'\n'+start_line +l3 + end_line +'\n' + end_rec +'\n'
        arts.append(tmp)
    return arts
    

n = int(input('Enter n in [1-6]: ').strip())
if n in (1,2,3,4,5,6):
    num = n
else:
    print("Please enter a number from 1 to 6")

def roll_dice(num):
    roll_results = []
    
    for _ in range(num):
        roll = random.randint(1,6)
        roll_results.append(roll)
    return roll_results

res = roll_dice(num)

arts = init()
rolls = ''
for i in res:
    rolls += arts[i-1]

# print(chr(9484) + chr(9472)*9 + chr(9488))
print(rolls)