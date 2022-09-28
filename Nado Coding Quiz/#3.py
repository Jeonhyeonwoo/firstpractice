seat_col = ["A","B","C"] 


for i in range(len(seat_col)):
    print("\n")
    for j in range (1,21): # for j in range (1,21)[::2] 하면 두칸씩 띄워서 출력 
        if j % 2 != 0:
            print(seat_col[i] + str(j), end=" ")    