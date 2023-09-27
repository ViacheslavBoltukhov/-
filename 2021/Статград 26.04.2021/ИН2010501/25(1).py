for m in range(2,50,2):
    for n in range(1,50,2):
        if 2**m*3**n in range(200_000_000, 400_000_001):
            print(2**m*3**n)

