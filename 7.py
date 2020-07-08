for row in range(7):
    for col in range(5):
        if (row==0 and col<4) or (col==3) or (row==3 and col>0):
            print("*",end=" ")
        else:
            print(end="  ")
    print(" ")
