{x: [i for i in range(1, abs(x) + 1) if x % i == 0] for x in sorted(list(numbers))}