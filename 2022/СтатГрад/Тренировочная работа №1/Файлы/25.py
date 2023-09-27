count=0
for numb in range(200_000_001,300_000_001):
    m_n=1   #Произведение 5-ти первых делителей числа
    count_m_n=0 #Количество делителей числа
    # Ищем делители числа до корня этого числа т.к их произведение
    # должно быть меньше самого числа
    for j in range(2,int(numb**0.5)+1):
        if numb%j==0:
            count_m_n+=1
            m_n*=j
        if count_m_n==5:
            if m_n<numb:
                print(m_n)
                count += 1
            break
    if count==5:
        break