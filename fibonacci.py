def fibonacci_sum(nth):
    intials = [0, 1]
    for i in range(nth - 1):
        intials.append(intials[i] + intials[i + 1])
    return sum(intials)


print(fibonacci_sum(50))
