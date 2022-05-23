def main():
    data_len = 1000
    data = open("input", "r")
    nonempty_lines = [lin.strip("\n") for lin in data if lin != "\n"]

    point_map = [0]*data_len
    for i in range(len(point_map)):
        point_map[i] = [0]*data_len
    data.close()
    part2(point_map, nonempty_lines, data_len)


def part1(point_map, nonempty_lines, data_len):
    for line in nonempty_lines:
        line = line.replace(" -> ", ",")
        line = line.rstrip().split(",")
        line = list(map(int, line))
        if line[1] == line[3]:
            ll = [0]*data_len
            if line[0] < line[2]:
                for i in range(line[0], line[2]+1):
                    ll[i] += 1
            if line[0] > line[2]:
                for i in range(line[2], line[0]+1):
                    ll[i] += 1

            sumlist = [a + b for a, b in zip(point_map[line[1]], ll)]
            point_map[line[1]] = sumlist

        if line[0] == line[2]:
            if line[1] < line[3]:
                for i in range(line[1], line[3]+1):
                    point_map[i][line[0]] += 1
            if line[1] > line[3]:
                for i in range(line[3], line[1]+1):
                    point_map[i][line[0]] += 1

    overlap_count = 0
    for i in point_map:
        for b in i:
            if b >= 2:
                overlap_count += 1
    print("Vertical and Horizantal line overlap", overlap_count, "Times!")


def part2(point_map, nonempty_lines, data_len):
    for line in nonempty_lines:
        line = line.replace(" -> ", ",")
        line = line.rstrip().split(",")
        line = list(map(int, line))
        if line[1] == line[3]:
            ll = [0]*data_len
            if line[0] < line[2]:
                for i in range(line[0], line[2]+1):
                    ll[i] += 1
            if line[0] > line[2]:
                for i in range(line[2], line[0]+1):
                    ll[i] += 1

            sumlist = [a + b for a, b in zip(point_map[line[1]], ll)]
            point_map[line[1]] = sumlist
            continue

        if line[0] == line[2]:
            if line[1] < line[3]:
                for i in range(line[1], line[3]+1):
                    point_map[i][line[0]] += 1
            if line[1] > line[3]:
                for i in range(line[3], line[1]+1):
                    point_map[i][line[0]] += 1
            continue

        if abs(line[2] - line[0]) == abs(line[3] - line[1]):
            print(line)
            mark_diag(line[0], line[2], line[1], line[3],
                      point_map, line[2] - line[0], line[3] - line[1])

    overlap_count = 0
    for i in point_map:
        for b in i:
            if b >= 2:
                overlap_count += 1

    print("Vertical Horizantal and diagonal lines overlap", overlap_count, "Times!")


def mark_diag(x1, x2, y1, y2, point_map, dir_x, dir_y):
    cur_x = x1
    cur_y = y1

    while cur_x != x2 + mysign(dir_x) and cur_y != y2 + mysign(dir_y):
        point_map[cur_y][cur_x] += 1
        if dir_x > 0:
            cur_x += 1
        else:
            cur_x -= 1
        if dir_y > 0:
            cur_y += 1
        else:
            cur_y -= 1


def mysign(x):
    if x >= 0:
        return 1
    else:
        return -1


if __name__ == "__main__":
    main()
