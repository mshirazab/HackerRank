import sys


def inverse(arr, r, c):
    arrI = [list(['O']) * c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] == "O":
                if i > 0:
                    arrI[i-1][j] = "."
                if i < r-1:
                    arrI[i+1][j] = "."
                if j > 0:
                    arrI[i][j-1] = "."
                if j < c-1:
                    arrI[i][j+1] = "."
                arrI[i][j] = "."
    return arrI


def main():
    r, c, n = input().strip().split(' ')
    r, c, n = [int(r), int(c), int(n)]
    grid = []

    for _ in range(r):
        grid_t = str(input().strip())
        grid.append(grid_t)

    if n == 0 or n == 1:
        print('\n'.join(grid))
        return
    gridI = inverse(grid, r, c)
    gridM = inverse(gridI, r, c)
    gridI = '\n'.join([''.join(elem) for elem in gridI])
    gridM = '\n'.join([''.join(elem) for elem in gridM])
    if n % 4 == 1:
        print(gridM)
    if n % 2 == 0:
        for _ in range(r):
            print("O" * c)
    if n % 4 == 3:
        print(gridI)


if __name__ == "__main__":
    main()
