# задача решена
s = input()
d = ""
count = 1
for i in range(0, len(s)-1, 1):
    if s[i].isalpha() == True: 
        if s[i] == s[i+1]:
            count +=1
            if i == len(s)-2:
                if s[i] == s[i+1]:
                    d = d + str(s[i]) + str(count)
                else:
                    d = d + str(s[i]) + "1" + str(s[i+1]) +"1"
        else:
            d = d + str(s[i]) + str(count)
            count = 1
            if i == len(s)-2:
                if s[i] == s[i+1]:
                    d = d + str(s[i]) + str(count)
                else:
                    d = d + str(s[i+1]) +"1"
    else:
        count = 1        
        continue
if len(s) == 1:
    d = s[0] + "1"
print(d)