def same_case(a, b):
    if (a.isalpha() and b.isalpha()) or (a.isupper() and b.isupper()) == "True":
        return 1
    if (a.isupper() and b.isalpha()) or (a.isalpha() and b.isupper()) == "True":
        return 0



same_case("%","c")
print(same_case("%","c"))

S.islower()

S.isupper()
