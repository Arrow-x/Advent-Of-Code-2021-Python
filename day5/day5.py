def main():
    data = open("day5/exm", "r")
    nonempty_lines = [lin.strip("\n") for lin in data if lin != "\n"]

    point_map = [0]*len(nonempty_lines)
    data.close()

    for line in nonempty_lines:
        line = line.replace(" -> ", ",")
        line = line.rstrip().split(",")
        line = list(map(int, line))
        if line[1] == line[3]:
            ll = [0]*10
            if line[0] < line[2]:
                for i in range(line[0], line[2]):
                    ll[i] += 1
            if line[0] > line[2]:
                for i in range(line[2], line[0]):
                    ll[i] += 1

            if type(point_map[line[1]]) == int:
                point_map[line[1]] = ll
            elif type(point_map[line[1]]) == list:
                point_map[line[1]] = [a + b for a,
                                      b in zip(point_map[line[1]], ll)]

    for i in point_map:
        print(i)


if __name__ == "__main__":
    main()
