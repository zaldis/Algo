from dataclasses import dataclass, field
from typing import Iterable, Sequence, TypeVar, Hashable

from zaldisalgo.ds.trie.protocols import TrieProtocol


T = TypeVar("T", bound=Hashable)


@dataclass
class TrieNode[T]:
    """Trie Node

    Stores information about prefix and existing following edges
    """
    is_terminal: bool = False
    _edges: dict[T, 'TrieNode[T]'] = field(default_factory=lambda: {})

    @property
    def children(self) -> dict[T, 'TrieNode[T]']:
        return self._edges

    def add_edge(self, edge: T) -> 'TrieNode[T]':
        if edge not in self._edges:
            self._edges[edge] = TrieNode()
        return self._edges[edge]


class Trie[T]:
    """Naive implementation of Trie

    >>> # To create a new Trie instance:
    >>> Trie[str].of('car', 'bar', 'shelf')
    """

    def __init__(self):
        self._root: TrieNode[T] = TrieNode()
        self._amount_of_paths = 0

    def __contains__(self, path: Sequence[T]) -> bool:
        """Checks if the key was added

        :returns: True if key exists in the Trie
        """
        try:
            ending_node = self._follow_path(path)
            return ending_node.is_terminal
        except:
            return False

    def __len__(self) -> int:
        return self._amount_of_paths

    def complete(self, prefix: Sequence[T]) -> list[Sequence[T]]:
        """Autocomplete search

        :param prefix: the prefix of search sequences.
        :returns: existing sequences which started from prefix.
        """
        curr_node = self._follow_path(prefix)
        completed_paths = []
        self._dfs_complete_search(curr_node, list(prefix), completed_paths)
        return completed_paths

    def add(self, path: Iterable[T]) -> None:
        """Add new words to the Trie

        :param words: sequence of keys which should be added.
        """
        curr_node = self._root
        deep_level = 0
        for edge in path:
            curr_node = curr_node.add_edge(edge)
            deep_level += 1
        if not curr_node.is_terminal:
            curr_node.is_terminal = True
            self._amount_of_paths += 1

    def _dfs_complete_search(
        self,
        node: TrieNode[T],
        path: list[T],
        completed_paths: list[list[T]]
    ) -> None:
        if node.is_terminal:
            completed_paths.append(list(path))
        for edge, next_node in node.children.items():
            path.append(edge)
            self._dfs_complete_search(next_node, path, completed_paths)
            path.pop()

    def _follow_path(self, path: Sequence[T]) -> TrieNode[T]:
        curr_node = self._root
        for edge in path:
            if edge not in curr_node.children:
                raise ValueError(f"Invalid path: {path}.")
            curr_node = curr_node.children[edge]
        return curr_node

    @staticmethod
    def of(*paths: Iterable[T]) -> 'Trie[T]':
        trie: Trie[T] = Trie()
        for path in paths:
            trie.add(path)
        return trie


if __name__ == '__main__':
    words_trie: TrieProtocol[str] = Trie[str].of(
        "postponed",
        "postmodern",
        "black",
    )
    words_trie.add("blackberry")
    autocomplete = words_trie.complete("post")
    print("Search 'post...'", autocomplete)
    assert list("postponed") in autocomplete
    assert list("postmodern") in autocomplete

    autocomplete = words_trie.complete("black")
    print("Search 'black...'", autocomplete)
    assert list("black") in autocomplete
    assert list("blackberry") in autocomplete

    phones_trie: TrieProtocol[int] = Trie[int].of(
        [3, 8, 0, 5, 0, 6, 5, 4, 8],
        [3, 8, 0, 1, 1, 8, 2, 7, 3],
        [4, 8, 1, 0, 3, 9, 3, 8, 2],
    )
    prefix = [3, 8, 0]
    print("Search '380...'", phones_trie.complete(prefix))
    assert [4, 8, 1, 0, 3, 9, 3, 8, 2] in phones_trie
    assert prefix not in phones_trie
    assert [3, 8, 0, 5, 0, 6, 5, 4, 8] in phones_trie.complete(prefix)
    assert [3, 8, 0, 1, 1, 8, 2, 7, 3] in phones_trie.complete(prefix)
