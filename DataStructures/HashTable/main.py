from typing import Hashable


class HashTable:
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


hash_table = HashTable()
hash_table[1] = 'Petia'
hash_table[2] = 'Vasia'
hash_table[3] = 'Roma'

assert hash_table[1] == 'Petia'
assert hash_table[2] == 'Vasia'
assert hash_table[3] == 'Roma'

print("well done!")
