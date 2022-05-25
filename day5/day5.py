def main():
    data_len = 1000
    data = open("day5/input", "r")
    nonempty_lines = [lin.strip("\n") for lin in data if lin != "\n"]

    point_map = [0]*data_len
    for i in range(len(point_map)):
        point_map[i] = [0]*data_len
    data.close()
    parser(point_map, nonempty_lines, data_len)


def parser(point_map, nonempty_lines, data_len):
    for line in nonempty_lines:
        line = line.replace(" -> ", ",")
        line = line.rstrip().split(",")
        line = list(map(int, line))

        x1 = line[0]
        x2 = line[1]
        y1 = line[2]
        y2 = line[3]

        if x2 == y2:
            ll = [0]*data_len
            if x1 < y1:
                for i in range(x1, y1+1):
                    ll[i] += 1
            if x1 > y1:
                for i in range(y1, x1+1):
                    ll[i] += 1

            point_map[x2] = [a + b for a, b in zip(point_map[x2], ll)]

        if x1 == y1:
            if x2 < y2:
                for i in range(x2, y2+1):
                    point_map[i][x1] += 1
            if x2 > y2:
                for i in range(y2, x2+1):
                    point_map[i][x1] += 1

        if abs(y1 - x1) == abs(y2 - x2):
            mark_diag(x1, y1, x2, y2, point_map, y1 - x1, y2 - x2)

    overlaps(point_map)


def overlaps(point_map):
    overlap_count = 0
    for i in point_map:
        for b in i:
            if b >= 2:
                overlap_count += 1

    print("The lines overlap", overlap_count, "Times!")


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
