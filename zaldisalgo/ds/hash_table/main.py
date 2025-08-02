from typing import Hashable


class HashTable:
    """Separate chaining hash table"""

    def __init__(self, size: int = 1000) -> None:
        self._table = []
        for _ in range(size):
            self._table.append([])

    def __getitem__(self, item) -> any:
        return self._get_item(item)

    def __setitem__(self, item: Hashable, value: any) -> None:
        return self._set_item(item, value)

    def _get_item(self, key: Hashable) -> any:
        index = hash(key) % len(self._table)
        for target_key, target_value in self._table[index]:
            if target_key == key:
                return target_value
        return None

    def _set_item(self, key: Hashable, value: any) -> None:
        index = hash(key) % len(self._table)
        self._table[index].append(
            (key, value, )
        )


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table['name'] = 'Ivan'
    hash_table['age'] = 20
    print("Stored name is: ", hash_table['name'])
    print("Stored age is: ", hash_table['age'])
