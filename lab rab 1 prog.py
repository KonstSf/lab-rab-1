a = open('/Users/soniakonstantinova/Documents/ШКОЛА/программирование/книжки/steam_description_data.csv')
i = 0 #
j = 0 #
h = 0 #
m =0 #
n = 0
prob = 0 #
prep = 0 #
pred = 'a' #
prered = 'a'
for each in a:
    z = len(each)
    for eh in each:
        if eh == ' ' or eh == '\n':
            prob += 1
            if pred != ' ' and pred != '\n':
                m+=1
        if 32 < ord(eh) < 48 or 57 < ord(eh) < 65 or 90 < ord(eh) < 97 or 122 < ord(eh) < 127:
            prep += 1
            if eh == '?' or eh == '!':
                n += 1
        if pred == '.' and (31 < ord(eh) < 48 or 57 < ord(eh) < 65 or 90 < ord(eh) < 97 or 122 < ord(eh) < 127 or eh == '\n'):
                n +=1
        if pred.isupper()== True and eh == '.' and prered == ' ':
            n -= 1
        prered = pred
        pred = eh
    j += (z - prob)
    h += (z - prep)
    prep = 0
    i += z
    prob = 0
print('количество символов:',i)
print('количество символов без пробелов:',j)
print('количество символов знаков препинания:',h)
if eh == ' ' or eh == '\n':
    print('количество слов:', m)
else:
    print('количество слов:', m + 1)
if eh == '.':
    print('количество предложений:', n+1)
else:
    print('количество предложений:', n)

