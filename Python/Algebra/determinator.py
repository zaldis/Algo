class Determinator(object):
    def __init__(self, matrix: list):
        self._matrix = matrix
        self._count_rows = len(matrix)
        self._count_columns = len(matrix[0])
        self._sign = 1

    def _slice_matrix(self) -> tuple:
        """
        Cut input matrix on two square matrix for 'matrix multiple'
        First element of result is matrix with one element
        Second element of result is result matrix
        """
        coefficient = self._matrix[0][0]
        del self._matrix[0]
        self._count_rows -= 1
        for row in range(self._count_rows):
            self._matrix[row] = self._matrix[row][1:]
        self._count_columns -= 1

        return coefficient, self._matrix

    def _is_zero_column(self, start_row=0, column_number=0):
        for row in range(start_row, self._count_rows):
            if self._matrix[row][column_number] != 0:
                return False

        return True

    def _swap_with_nonzero(self, start_row=0):
        """
        Find first row with nonzero first coefficient and
        swap it with first row
        """
        column = 0
        for row in range(self._count_columns):
            if self._matrix[row][column] != 0 and row != start_row:
                self._matrix[row], self._matrix[start_row] = self._matrix[start_row], self._matrix[row]
                self._sign *= -1
                break

    def _clear_coefficients(self):
        """
        Modify matrix into matrix with zero-coefficients
        in first column
        """

        for row in range(1, self._count_rows):
            coefficient = self._matrix[row][0] / (0.0 + self._matrix[0][0])
            for column in range(self._count_columns):
                self._matrix[row][column] -= self._matrix[0][column] * coefficient

    def determinate(self) -> float:
        """
        Find determinate of input matrix
        """
        determinant = 1.0
        while self._matrix is not None:
            if len(self._matrix) == 0:
                break

            if self._is_zero_column():
                return 0.0

            if self._matrix[0][0] == 0:
                self._swap_with_nonzero()

            self._clear_coefficients()
            respond = self._slice_matrix()
            determinant *= respond[0]
            self._matrix = respond[1]

        return self._sign * determinant


# if __name__ == '__main__':
#     size = int(input())
#     matrix = []
#     for line_number in range(size):
#         row = [int(number) for number in input().split()]
#         matrix.append(row)
#
#     determinant = Determinator(matrix).determinate()
#     print(round(determinant))