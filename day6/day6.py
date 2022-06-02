def main():
    days = 80
    raw = open("day6/input", "r")

    input_str = []
    for raw_fish in raw:
        input_str.append(raw_fish)
    raw.close()

    # fishes = [[] for y in range(days+1)]
    for raw_fish in input_str:
        fishes = (list(map(int, raw_fish.split(","))))

    for day in range(days):
        new_fishs = []
        for fish in fishes:
            new_fish = fish - 1
            if new_fish == -1:
                new_fish = 6
                new_fishs.append(8)
            new_fishs.append(new_fish)
        fishes = new_fishs

    # for i in fishes:
    #     print(i)
    print(len(fishes))


if __name__ == "__main__":
    main()
