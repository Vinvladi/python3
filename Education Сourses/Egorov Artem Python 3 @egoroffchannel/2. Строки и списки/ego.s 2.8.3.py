name = input()
second_name = input()
text = """Здравствуйте, {sn} {n}!""".format(n=name,sn=second_name)
print(text)