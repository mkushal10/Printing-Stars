for row in range(7):
    for col in range(6):
        if (row==3) or (col==4) or (col==0 and row<4):
            print("*",end=" ")
        else:
            print(end="  ")
    print(" ")
