for row in range(7):
    for col in range(5):
        if (row==6) or (col==2) or (row==1 and (col<2 and col>0)):
            print("*",end=" ")
        else:
            print(end="  ")
    print(" ")
