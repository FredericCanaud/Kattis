MEM = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]


def mod_pow2(n):
    while n >= len(MEM):
        MEM.append((MEM[-1] * 2) % (10**9+7))
    return MEM[n]


def inversions(input):
    total, zeros, questions = (0,)*3
    for x in reversed(input):
        if x == '1':
            z = zeros * mod_pow2(questions)
            q = 0 if questions == 0 else questions * mod_pow2(questions-1)
            total = (total + z + q) % (10**9+7)
        elif x == '0':
            zeros += 1
        else:
            total *= 2
            z = zeros * mod_pow2(questions)
            q = 0 if questions == 0 else questions * mod_pow2(questions-1)
            total = (total + z + q) % (10**9+7)
            questions += 1

    return total


if __name__ == "__main__":
    print(inversions(input()))

