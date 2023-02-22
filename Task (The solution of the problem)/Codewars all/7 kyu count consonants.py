def consonant_count(s):  # поиск всех гласных в строке
    count = 0
    for i in range(len(s)):
        if ("a" <= s[i] <= "z" or "A" <= s[i] <= "Z") and s[i] not in "aeiouAEIOU":
            count += 1
        else:
            continue
    return count
