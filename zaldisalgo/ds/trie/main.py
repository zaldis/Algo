from dataclasses import dataclass, field
from typing import Iterable, Sequence

from zaldisalgo.ds.trie.protocols import TrieProtocol


@dataclass
class _Node[T]:
    """Trie Node

    Stores information about prefix and existing following edges
    """
    value: Sequence[T]
    is_terminal: bool = False
    is_root: bool = False
    _edges: dict[T, '_Node[T]'] = field(default_factory=lambda: {})

    @property
    def children(self) -> Sequence['_Node[T]']:
        """:returns: The sequence of connected children nodes."""
        return list(self._edges.values())

    def get_child(self, child_edge: T) -> '_Node[T]':
        """:returns: The child node by the edge name."""
        return self._edges[child_edge]

    def has_child(self, child_edge: T) -> bool:
        """:returns: True if the node has the edge with the passed name."""
        return child_edge in self._edges

    def add_child(self, child_edge: T, prefix: Sequence[T]) -> None:
        """ Creates a new node

        Connects a created node with the current one by the provided edge.
        :param child_edge: the name of the edge.
        :param prefix: the value of new node's prefix.
        """
        self._edges[child_edge] = _Node(prefix)


class Trie[T]:
    """Naive implementation of Trie

    >>> # To create a new Trie instance:
    >>> Trie[str].of('car', 'bar', 'shelf')
    """

    def __init__(self):
        self._root: _Node[T] = _Node([], is_root=True)

    def __contains__(self, key: Sequence[T]) -> bool:
        """Checks if the key was added

        :returns: True if key exists in the Trie
        """
        curr_node = self._follow_key(key)
        return curr_node.value == key

    def complete(self, prefix: Sequence[T]) -> Iterable[T]:
        """Autocomplete search

        :param prefix: the prefix of search sequences.
        :returns: existing sequences which started from prefix.
        """
        found_words = []
        curr_node = self._follow_key(prefix)
        if curr_node.value != prefix:
            return found_words

        next_visit_nodes = [curr_node]
        while len(next_visit_nodes):
            curr_node = next_visit_nodes.pop()
            next_visit_nodes.extend(curr_node.children)
            if curr_node.is_terminal:
                found_words.append(curr_node.value)
        return found_words

    def add(self, *keys: Sequence[T]) -> None:
        """Add new words to the Trie

        :param keys: sequence of keys which should be added.
        """
        for key in keys:
            self._feed_key(key)

    def _follow_key(self, key: Sequence[T]) -> _Node[T]:
        curr_node = self._root
        for edge in key:
            if curr_node.has_child(edge):
                curr_node = curr_node.get_child(edge)
            else:
                break
        return curr_node

    def _feed_key(self, key: Sequence[T]) -> None:
        curr_node = self._root
        for pos, edge in enumerate(key):
            if not curr_node.has_child(edge):
                curr_node.add_child(edge, prefix=key[:pos+1])
            curr_node = curr_node.get_child(edge)
        curr_node.is_terminal = True

    @staticmethod
    def of(*words: T) -> 'Trie[T]':
        trie: Trie[T] = Trie()
        trie.add(*words)
        return trie


if __name__ == '__main__':
    words_trie: TrieProtocol[str] = Trie[str].of("postponed", "postmodern", "black")
    words_trie.add("blackberry")  # Insert
    print("Search 'post...'", words_trie.complete("post"))
    assert set(words_trie.complete("post")) == {"postponed", "postmodern"}

    print("Search 'black...'", words_trie.complete("black"))
    assert set(words_trie.complete("black")) == {"black", "blackberry"}

    # Building
    phones_trie: TrieProtocol[int] = Trie[int].of(
        [3, 8, 0, 5, 0, 6, 5, 4, 8],
        [3, 8, 0, 1, 1, 8, 2, 7, 3],
        [4, 8, 1, 0, 3, 9, 3, 8, 2],
    )
    print("Search '380...'", phones_trie.complete([3, 8, 0]))  # Autocomplete
    assert [3, 8, 0] in phones_trie  # Search
    assert [3, 8, 0, 5, 0, 6, 5, 4, 8] in phones_trie.complete([3, 8, 0])
    assert [3, 8, 0, 1, 1, 8, 2, 7, 3] in phones_trie.complete([3, 8, 0])