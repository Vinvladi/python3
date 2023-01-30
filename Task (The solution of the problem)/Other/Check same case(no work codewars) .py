def same_case(a, b):
    if ord(a) in range(97,122):
        if ord(b) in range(97,122):
            return "1"
        elif ord(b) in range(65,90):
            return "0"
        else:
            return "-1"
    elif ord(a) in range(65,90):
        if ord(b) in range(65,90):
            return "1"
        elif ord(b) in range(97,122):
            return "0"
        else:
            return "-1"
    else:
        return "-1"
    pass


same_case("%","c")
print(same_case("%","c"))