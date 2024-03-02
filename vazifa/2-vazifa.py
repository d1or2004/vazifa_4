def masala(data, target):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for g in range(j + 1, len(data)):
                if data[i] + data[j] + data[g] == target:
                    return [i, j, g]


data = [2, 7, 11, 15, 5]  # ketma - ket 3 son uchun o'rinli
target = 31
print(masala(data, target))
