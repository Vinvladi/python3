person={}
s = "Ivanov IVAN Samara SGU 5 4 5 5 4 3 5"
s = s.split()
person['lastName'] = s[0]
person['firstName'] = s[1]
person['city'] = s[2]
person['university'] = s[3]
person['marks'] = []
for i in s[4:]:
    person['marks'].append(int(i))
print(s)
print(person)
