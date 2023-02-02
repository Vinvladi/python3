number_inp = int(input())
n_l = number_inp - 1  # число до значения
n_r = number_inp + 1  # число после значения
text = """Для числа {n} предыдущим будет число {n_l}.\nДля числа {n} следующим будет число {n_r}.""".format(
    n=number_inp, n_l=n_l, n_r=n_r)
print(text)
