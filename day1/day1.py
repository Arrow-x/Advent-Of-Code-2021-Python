import fileinput


def main():
    reading = []
    for line in fileinput.input():
        reading.append(int(line.rstrip()))
    mesure_sliding_data(reading)


def mesure_noisy_data(reading):
    times_increased = 0
    for i in range(len(reading)):
        if i == 0:
            continue

        if reading[i] > reading[i - 1]:
            times_increased += 1

    print("reading increased:", times_increased, "Times")


def mesure_sliding_data(reading):
    times_increased = 0
    for i in range(len(reading) - 3):
        if (reading[i + 1] + reading[i + 2] + reading[i + 3]) > (
            reading[i] + reading[i + 1] + reading[i + 2]
        ):
            times_increased += 1

    print("sliding readings increased:", times_increased, "Times")


if __name__ == "__main__":
    main()
