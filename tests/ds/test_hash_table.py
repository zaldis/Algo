from zaldisalgo.ds import HashTable


def test_hash_table_with_numeric_keys():
    hash_table = HashTable()

    hash_table[1] = 'Petia'
    hash_table[2] = 'Vasia'
    hash_table[3] = 'Roma'

    assert hash_table[1] == 'Petia'
    assert hash_table[2] == 'Vasia'
    assert hash_table[3] == 'Roma'
