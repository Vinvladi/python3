text = """В западном интернете понятия «треш-стримы» нет, и все попытки начать создавать 
		  подобное жёстко осуждаются и приводят к блокировке нарушителей на сервисах, 
		  но случаи треш-стримов все равно фиксируются, как, например, стример из США."""
lines = text.splitlines()
stripped_lines = [line.strip() for line in lines]
changed_and_filtered1 = [line.lower() for line in stripped_lines if 'понятия' in line]
# в новый список выберем только те строки, в которых есть вхождение слова 'все'
print(changed_and_filtered1)