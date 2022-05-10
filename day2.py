import fileinput


def main():
    # part_one(fileinput.input())
    part_two(fileinput.input())


def part_one(lines):
    depth = 0
    hor_pos = 0
    for line in lines:
        line_key = line.rstrip().split(" ")[0]
        line_val = int(line.rstrip().split(" ")[1])
        match line_key:
            case "forward":
                hor_pos += line_val
            case "up":
                depth -= line_val
            case "down":
                depth += line_val
    print(hor_pos * depth)


def part_two(lines):
    depth = 0
    hor_pos = 0
    aim = 0
    for line in lines:
        line_key = line.rstrip().split(" ")[0]
        line_val = int(line.rstrip().split(" ")[1])
        match line_key:
            case "forward":
                hor_pos += line_val
                depth += aim * line_val
            case "up":
                aim -= line_val
            case "down":
                aim += line_val
    print(hor_pos * depth)


if __name__ == "__main__":
    main()
