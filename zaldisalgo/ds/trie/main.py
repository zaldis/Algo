from typing import Iterable

from zaldisalgo.ds.trie.protocols import TrieProtocol


class Trie[T]:
    """ WIP: It's a rough implementation of Tie data structure

    TBD: improved readability, documentation, tests
    """
    def __init__(self):
        self._root: dict[any, dict] = {}
        self._size = 0

    def __len__(self):
        return self._size

    def complete(self, prefix: T) -> Iterable[T]:
        """Autocomplete search

        :param prefix: prefix of search sequences.
        :return: existed sequences which started from prefix.
        """
        curr_node = self._root
        for item in prefix:
            if item in curr_node:
                curr_node = curr_node[item]
            else:
                return []

        found_words = []
        next_visit_items = [[curr_node, item, list()] for item in list(curr_node.keys())]
        while len(next_visit_items):
            curr_node, next_item, meet_items = next_visit_items.pop()
            meet_items.append(next_item)

            curr_node = curr_node[next_item]
            if not len(curr_node):
                found_words.append(prefix + "".join(meet_items))
                meet_items.pop()
            else:
                next_visit_items.extend(
                    [[curr_node, item, meet_items] for item in list(curr_node.keys())]
                )
        return found_words


    def add(self, *words: T) -> None:
        """Add new words to the dictionary

        :param words: sequence of words which should be added.
        """
        for word in words:
            self._feed_word(word)

    def _feed_word(self, word: T) -> None:
        curr_node = self._root
        for item in word:
            if item not in curr_node:
                curr_node[item] = {}
                self._size += 1
            curr_node = curr_node[item]

    @staticmethod
    def of(*words: T) -> 'Trie[T]':
        trie = Trie()
        trie.add(*words)
        return trie



if __name__ == '__main__':
    trie: TrieProtocol[str] = Trie[str].of("postponed", "postmodern")
    trie.add("blackberry")
    print("Trie nodes:", len(trie))
    print("Search 'post...'", trie.complete("post"))
    assert set(trie.complete("post")) == {"postponed", "postmodern"}