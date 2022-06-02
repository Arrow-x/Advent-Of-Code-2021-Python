def main():
    raw = open("day6/input", "r")

    input_str = []
    for raw_fish in raw:
        input_str.append(raw_fish)
    raw.close()

    fishes = [[] for y in range(81)]
    for raw_fish in input_str:
        fishes[0] = (list(map(int, raw_fish.split(","))))

    for day in range(80):
        for fish in fishes[day]:
            new_day_fish = fish - 1
            if new_day_fish == -1:
                new_day_fish = 6
                fishes[day+1].append(8)
            fishes[day+1].append(new_day_fish)

    # for i in fishes:
    #     print(i)
    print(len(fishes[80]))


if __name__ == "__main__":
    main()
