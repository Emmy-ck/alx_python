for i in range(0,10):
    for j in range(i + 1, 10):
        if (i == 8) and (j == 9):
            print(89)
        else:
            print("{}{}".format(i,j), end=", ")
        #print("{}".format(j), end=", ")
#print(" ".join("{}{}".format(i, j) for i in range(10) for j in range(i + 1, 10)))
