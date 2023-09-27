for x112 in range(30):
    for x221 in range(30):
        for x122 in range(30):
            for x211 in range(30):
                if (2*x112+x122==2*x221+x211) and (2*x211+x221==40) and (x112+2*x122>50):
                    print(x112+2*x122)
                    exit(0)