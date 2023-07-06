def sum_natural_numbers():
    multiples = []
    for i in range(0, 1000):
        if i % 3 == 0 and i % 5 == 0:
            multiples.append(i)
        elif i % 3 == 0:
            multiples.append(i)
        elif i % 5 == 0:
            multiples.append(i)
        else:
            continue
    print(sum(multiples))

sum_natural_numbers()