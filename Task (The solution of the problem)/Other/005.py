text = """В западном интернете понятия «треш-стримы» нет, и все попытки начать создавать   
         подобное жёстко осуждаются и приводят к блокировке нарушителей на сервисах,   
         но случаи треш-стримов все равно фиксируются, как, например, стример из США."""
lines = text.splitlines()
stripped_lines = [line.strip() for line in lines]
filtered = filter(lambda s: 'все' in s, stripped_lines) #модуль фильтра
changed_and_filtered2 = map(lambda s: s.lower(), filtered) #действие, но оно будет выполнено, только после старта цикла for
print('hello')

for line in changed_and_filtered2:
	print(line)
