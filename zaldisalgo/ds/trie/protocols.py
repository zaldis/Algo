from typing import Protocol, Iterable, TypeVar, Sized, Sequence, Hashable

T = TypeVar("T", bound=Hashable)


class TrieProtocol(Sized, Protocol[T]):
    def __contains__(self, key: Sequence[T]) -> bool:
        """Checks if the key was added

        :returns: True if key exists in the Trie
        """
        ...

    def add(self, *keys: Sequence[T]) -> None:
        """Adds new keys to the Trie

        :param keys: sequence of keys which should be added to the Trie.
        :return: None value
        """
        ...

    def complete(self, prefix: Sequence[T]) -> Iterable[T]:
        """Autocomplete search

        :param prefix: prefix of search sequences.
        :return: existed sequences which started from prefix.
        """
        ...
