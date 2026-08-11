from collections import Counter
def first_non_repeating_letter(s):
    d = s.lower() 

    print(Counter(d).values(),Counter(d) )
    for i, p in zip(Counter(d).values(), Counter(d)):
        if i == 1:
            return p
        else:
            continue

        return ""


print(first_non_repeating_letter("aabbrRteaaa"))