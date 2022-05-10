import fileinput


def main():
    gamma_rate_byte = [0] * 12
    epsilon_rate_byte = [0] * 12
    zero_count = [0] * 12
    one_count = [0] * 12

    for line in fileinput.input():
        bits = list(str(line.rstrip()))
        for b in range(len(bits)):
            if int(bits[b]) == 1:
                one_count[b] += 1
            if int(bits[b]) == 0:
                zero_count[b] += 1

    for b in range(len(zero_count)):
        if zero_count[b] > one_count[b]:
            gamma_rate_byte[b] = 0
            epsilon_rate_byte[b] = 1
        if zero_count[b] < one_count[b]:
            gamma_rate_byte[b] = 1
            epsilon_rate_byte[b] = 0

    gamma_rate = int("".join(map(str, gamma_rate_byte)), 2)
    epsilon_rate = int("".join(map(str, epsilon_rate_byte)), 2)

    print("Gamma rate:", gamma_rate)
    print("Epsilonrate", epsilon_rate)
    print("So the Gama rate times the Epsilon rate is", gamma_rate * epsilon_rate)


if __name__ == "__main__":
    main()
