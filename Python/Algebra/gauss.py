import operator

_MAX_COUNT_ROWS = 100
_MAX_COUNT_COLUMNS = 100

HAVE_ONE_SOLUTION = 'YES'
HAVE_MUCH_SOLUTIONS = 'INF'
HAVE_NOT_SOLUTION = 'NO'


def _init(matrix: list) -> list:
    parameters = [[0] * _MAX_COUNT_COLUMNS for r in range(_MAX_COUNT_ROWS)]
    right_vector = [0] * _MAX_COUNT_ROWS
    w, h = 0, 0
    for h in range(len(matrix)):
        for w in range(len(matrix[h]) - 1):
            parameters[h][w] = matrix[h][w]
        right_vector[h] = matrix[h][w + 1]

    return [parameters, right_vector]


def _step_up(parameters: list, right_vector: list, count_rows: int, count_columns) -> list:
    x = [-1.0] * count_columns
    for row_id in range(count_rows - 1, -1, -1):
        summ = 0.0
        for next_column in range(row_id + 1, count_rows):
            summ += parameters[row_id][next_column] * x[next_column]

        x[row_id] = (right_vector[row_id] - summ) / parameters[row_id][row_id]

    return x


def _step_down(parameters: list, right_vector: list, row: int, count_rows: int, column: int, count_columns):
    for next_row in range(row + 1, count_rows):
        delta = parameters[next_row][column] / parameters[row][column]

        right_vector[next_row] -= delta * right_vector[row]
        for next_column in range(column, count_columns):
            parameters[next_row][next_column] -= delta * parameters[row][next_column]


def _find_max_row(parameters: list, max_row: int, count_rows: int, column: int) -> int:
    for row in range(max_row + 1, count_rows):
        if parameters[row][column] > parameters[max_row][column]:
            max_row = row

    return max_row


def find_solution(matrix: list) -> list:
    """
    :param matrix:
        consists of list of arguments of the system.
        a[1][1]*x[1] + a[1][2]*x[2] + ... + a[1][m]*x[m] = b[1]
        a[2][1]*x[1] + a[2][2]*x[2] + ... + a[2][m]*x[m] = b[2]
                        ...         ...
        a[n][1]*x[1] + a[n][2]*x[2] + ... + a[n][m]*x[m] = b[n]

        [
            [a[1][1], a[1][2], ... , a[1][m], b[1]]
            [a[2][1], a[2][2], ... , a[2][m], b[2]]
                ...     ...     ...     ...
            [a[n][1], a[n][2], ... , a[n][m], b[n]]
        ]
    :return pair:
        first element is a bool type, that answer: Does system have solutions?
        second element returns list of roots of the system of equations
    """
    count_equations = len(matrix)
    count_variables = len(matrix[0]) - 1

    if count_equations < count_variables:
        return [HAVE_MUCH_SOLUTIONS, None]
    else:
        parameters, right_vector = _init(matrix)
        for row in range(count_equations):
            max_row = _find_max_row(parameters, row, count_equations, row)
            parameters[row], parameters[max_row] = parameters[max_row], parameters[row]
            right_vector[row], right_vector[max_row] = right_vector[max_row], right_vector[row]

            if abs(parameters[row][row]) <= 1e-10:
                return [HAVE_NOT_SOLUTION, None]

            _step_down(parameters, right_vector, row, count_equations, row, count_variables)

        x = _step_up(parameters, right_vector, count_equations, count_variables)
        return [HAVE_ONE_SOLUTION, x]


"""
if __name__ == "__main__":
    matrix = []
    count_rows, count_columns = map(int, input().split())
    for row_id in range(count_rows):
        line = input()
        row = [float(num) for num in line.split()]
        matrix.append(row)

    res = find_solution(matrix)
    if res[0] != HAVE_MUCH_SOLUTIONS and res[0] != HAVE_NOT_SOLUTION:
        print(res[0])
        for ans_value in res[1]:
            print(ans_value, end=' ')
    else:
        print(res[0])
"""
