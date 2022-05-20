def main():
    data_len = 10
    data = open("day5/exm", "r")
    nonempty_lines = [lin.strip("\n") for lin in data if lin != "\n"]

    point_map = [0]*len(nonempty_lines)
    for i in range(len(point_map)):
        point_map[i] = [0]*data_len
    data.close()

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

            point_map[line[1]] = [a + b for a,
                                  b in zip(point_map[line[1]], ll)]
        if line[0] == line[2]:
            if line[1] < line[3]:
                for i in range(line[1], line[3]+1):
                    point_map[i][line[0]] += 1
            if line[1] > line[3]:
                for i in range(line[3], line[1]+1):
                    point_map[i][line[0]] += 1

    for i in point_map:
        print(i)


if __name__ == "__main__":
    main()
