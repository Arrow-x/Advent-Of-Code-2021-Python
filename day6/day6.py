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
    fish_count = len(fishes)

    for day in range(days):
        add_counter = 0
        for fish_idx in range(fish_count):
            fishes[fish_idx] -= 1
            if fishes[fish_idx] == -1:
                fishes[fish_idx] = 6
                add_counter += 1
        for a in range(add_counter):
            fishes.append(8)
            fish_count += 1

    print(fish_count)


if __name__ == "__main__":
    main()
