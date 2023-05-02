
# loop = True
# type(loop)

def helper():
    print('_'*70)
    print("\tAvailable operations:\n\t'h'\tDisplay this message\n\t'+'\tAddition\n\t")
    print('_'*70)

def iput(prompt):
    x = input(prompt)
    return float(x) if x.isdigit() else f"{x} is not a number!"

while True:
    choice = input("Your choice(h|+|-|*|/|%|//|**|q): ")
    # print(choice, type(choice))
    
    if choice == 'h':
        helper()
    
    elif choice == '+':
        a = input('First Number = ')
        if a.isdigit():
            a = float(a)
        else:
            print(a, ' is not a number!')
        b = input('Second Number = ')
        if b.isdigit():
            b = float(b)
        else:
            print(b, ' is not a number!')
            
        print(a + b)
        
    elif choice == '-':
        a = input('First Number = ')
        if a.isdigit():
            a = float(a)
        else:
            print(a, ' is not a number!')
        b = input('Second Number = ')
        if b.isdigit():
            b = float(b)
        else:
            print(b, ' is not a number!')
            
        print(f"{a} - {b} = {a-b}")
    
    elif choice == '*':
        a = iput('First Number = ')
        if isinstance(a, str): print(a); continue
        b = iput('Second Number = ')
        if isinstance(b, str): print(b); continue
        print(f"{a} * {b} = {a*b}")
        
    elif choice == 'q':
        print('Bye and Heppy Coding!')
        break
        # loop = False
        
    else:
        print('Unrecognized operation!')
        helper()

