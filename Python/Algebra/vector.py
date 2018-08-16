class BasisNumberError(Exception):
    def __init__(self, message: str):
        self.message = message


class Vector:
    def __init__(self, coordinates: list):
        self._coordinates = coordinates
        self._size = len(coordinates)

    def get_size(self) -> int:
        return self._size

    def get_coordinate(self, basis_number: int) -> float:
        if basis_number < 0 or basis_number >= self._size:
            raise BasisNumberError("Invalid basis number. Basis number can't be bigger than maximum size of vector and "
                                   "smaller then 0")

        return self._coordinates[basis_number]

    def add(self, coordinate: float):
        self._coordinates.append(coordinate)
        self._size += 1

    def __iter__(self):
        for coordinate in self._coordinates:
            yield coordinate


class VectorSizeError(Exception):
    def __init__(self):
        super().__init__("For calculate scalar product we must have two vectors with equal size")


def make_scalar_product(vector_a: Vector, vector_b: Vector) -> float:
    if vector_a.get_size() != vector_b.get_size():
        raise VectorSizeError()

    res = 0
    for basis_number in range(vector_a.get_size()):
        res += vector_a.get_coordinate(basis_number) * vector_b.get_coordinate(basis_number)

    return res


"""
if __name__ == "__main__":
    vector_a = Vector([1, 2, 3, 4])
    vector_b = Vector([1, -1, 0])
    print(make_scalar_product(vector_a, vector_b))
"""
