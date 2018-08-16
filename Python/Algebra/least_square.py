from Algebra.vector import *

from Algebra.gauss import find_solution as gauss_find
from Algebra.gauss import HAVE_ONE_SOLUTION


def _create_linear_system(coefficients: list, results: Vector) -> (list(), Vector):
    count_unknowns = len(coefficients)
    _results = Vector([])
    unknowns = [Vector([]) for it in range(count_unknowns)]

    for row in range(count_unknowns):
        for column in range(len(coefficients)):
            scalar_product = make_scalar_product(coefficients[column], coefficients[row])
            unknowns[column].add(scalar_product)
        scalar_product = make_scalar_product(results, coefficients[row])
        _results.add(scalar_product)

    return unknowns, _results


def _convert_to_matrix(unknowns_coefficients: list, system_result: Vector) -> list:
    count_rows = unknowns_coefficients[0].get_size()
    count_columns = len(unknowns_coefficients)

    matrix = [[0 for c in range(count_columns + 1)] for r in range(count_rows)]
    for row in range(count_rows):
        for column in range(count_columns):
            matrix[row][column] = unknowns_coefficients[column].get_coordinate(row)
        matrix[row][count_columns] = system_result.get_coordinate(row)

    return matrix


class RootsError(Exception):
    def __init__(self):
        super().__init__("Roots isn't found")


def find_roots(coefficients: list, results: Vector) -> list:
    unknowns_coefficients, system_result = _create_linear_system(coefficients, results)

    matrix = _convert_to_matrix(unknowns_coefficients, system_result)
    gauss_result = gauss_find(matrix)
    if gauss_result[0] == HAVE_ONE_SOLUTION:
        return gauss_result[1]
    else:
        raise RootsError()


if __name__ == '__main__':
    # print("Start testing:")
    count_rows, count_unknowns = [int(number) for number in input().split()]
    unknowns = [Vector([]) for _ in range(count_unknowns)]
    vector_res = Vector([])

    for row_id in range(count_rows):
        row_items = input().split()
        for column_id in range(count_unknowns):
            unknowns[column_id].add(float(row_items[column_id]))

        vector_res.add(float(row_items[count_unknowns]))

    res = find_roots(unknowns, vector_res)
    for item in res:
        print(item, end=" ")
