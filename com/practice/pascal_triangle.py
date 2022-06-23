def triangle(n):
    result = []
    for row in range(n):
        new_row = [1]
        for col in range(1, row + 1):
            new_cell = new_row[col - 1] * float(row + 1 - col) / col
            new_row.append(int(new_cell))
        result.append(new_row)
    return result


print(triangle(4))
