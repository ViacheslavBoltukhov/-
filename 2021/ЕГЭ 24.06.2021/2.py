'''Логическая функция F задаётся выражением (¬a ∧ ¬b) ∨ (b ≡ c) ∨ d. '''
print('a b c d')
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                if not(((not a) and (not b)) or (b==c) or d):
                    print(a,b,c,d)