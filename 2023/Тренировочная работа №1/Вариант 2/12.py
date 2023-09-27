max2=0
for x112 in range(60):
    for x122 in range(60):
        for x221 in range(60):
            for x211 in range(60):
                if 2*x112+x122==2*x221+x211 and x221+2*x211==47 and x112+2*x122<70:
                    max2=max(max2,x112+2*x122)
print(max2)
