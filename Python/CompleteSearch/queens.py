"""
    Queens problem

    Input:
        Queens positions
    Output:
        Valid - if no two queens attack each other
        Invalid - in other way

    Complexity:
        Time: O(n)
        Space: O(n)

        n - size of the board (n x n) 
"""


from typing import List


def is_valid_queens_position(positions: List[str]) -> bool:
    board_size = 8
    columns = [0] * board_size
    rows = [0] * board_size
    main_diag = [0] * (3 * board_size)
    back_diag = [0] * (3 * board_size)
    
    for position in positions:
        row = ord(position[0]) - ord('A')
        col = ord(position[1]) - ord('1')

        if rows[row] or columns[col] or main_diag[row+col] or back_diag[row-col]:
            return False
        else:
            rows[row] = columns[col] = main_diag[row+col] = back_diag[row-col] = 1
    return True


if __name__ == '__main__':
    """
        Valid

        K 0 0 0 0 0 0 0
        0 0 0 0 0 0 K 0
        0 0 0 0 K 0 0 0
        0 0 0 0 0 0 0 K
        0 K 0 0 0 0 0 0
        0 0 0 K 0 0 0 0
        0 0 0 0 0 K 0 0
        0 0 K 0 0 0 0 0
    """
    queens_position = ['A1', 'B5', 'C8', 'D6', 'E3', 'F7', 'G2', 'H4', ]
    print('Valid' if is_valid_queens_position(queens_position) else 'Invalid')

    """
        Invalid

        0 0 0 0 K 0 0 0
        0 0 0 0 0 0 0 0
        0 0 K 0 0 0 0 0
        0 0 K 0 K K 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 K 0
        K 0 0 0 0 0 0 0
    """
    queens_position = ['C3', 'E4', 'C4', 'E1', 'C4', 'F4', 'A8', 'G6', ]
    print('Valid' if is_valid_queens_position(queens_position) else 'Invalid')