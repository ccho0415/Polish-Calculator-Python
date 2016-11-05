import sys
lst = []
firstinput = input("First Input of Equation Please!")
firstinput = int(firstinput)
lst.append(firstinput)
while True:
    inp = input("Next Input Please!")
    if inp in {"*", "/", "-", "+", "?"} :
        print("got operator")
        if len(lst) >= 2:
            x = lst.pop()   # stack = [1,2], x = 3
            y = lst.pop() #stack = [1] x = 3 y = 2
            if inp == "*":
                lst.append(x*y)  #stack [1,6]
            elif inp == "/":
                lst.append(y/x)	#stack [1, 1.5]
            elif inp == "-":
                lst.append(x-y) #stack [1,1] 
            elif inp == "+":
                lst.append(x+y) #stack [1,5]
        else:
            print ("Not Enough Numbers!!!")
    elif inp == "I am done":
         print (lst)
         sys.exit(0)
    else:
        try:
            a = int(inp)        
            lst.append(a)
        except ValueError:
            print("Beep Boop Error Has Occured")
            sys.exit(0)          
       
