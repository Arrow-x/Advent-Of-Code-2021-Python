import fileinput


def main():
    # part_one(fileinput.input())
    co2_list = list(fileinput.input())
    oxygen_list = list(fileinput.input())

    oxygen_gen_byte = ""
    co2_scr_byte = ""
    len_of_byte = len(oxygen_list[0])

    for i in range(len_of_byte):
        if len(oxygen_list) == 1:
            oxygen_gen_byte = oxygen_list[0]
            break

        ones_list = []
        zeros_list = []
        for line in oxygen_list:
            if line[i] == "1":
                ones_list.append(line)
            if line[i] == "0":
                zeros_list.append(line)

        if len(ones_list) > len(zeros_list):
            oxygen_list = ones_list
        if len(ones_list) == len(zeros_list):
            oxygen_list = ones_list
        if len(ones_list) < len(zeros_list):
            oxygen_list = zeros_list

    for i in range(len_of_byte):
        if len(co2_list) == 1:
            co2_scr_byte = co2_list[0]
            break

        ones_list = []
        zeros_list = []

        for line in co2_list:
            if line[i] == "1":
                ones_list.append(line)
            if line[i] == "0":
                zeros_list.append(line)

        if len(ones_list) > len(zeros_list):
            co2_list = zeros_list
        if len(ones_list) == len(zeros_list):
            co2_list = zeros_list
        if len(ones_list) < len(zeros_list):
            co2_list = ones_list

    o2_gen_decimal = int(oxygen_gen_byte, 2)
    co2_scrub_decimal = int(co2_scr_byte, 2)
    print(
        "Oxygen Generator byte is",
        oxygen_gen_byte,
        "it's decimal is",
        o2_gen_decimal,
    )
    print("CO2 Scrubber byte is", co2_scr_byte, "it's decimal is", co2_scrub_decimal)
    print("Life support rating is", o2_gen_decimal * co2_scrub_decimal)


def part_one(files):
    gamma_rate_byte = [0] * 12
    epsilon_rate_byte = [0] * 12
    zero_count = [0] * 12
    one_count = [0] * 12

    for line in files:
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
