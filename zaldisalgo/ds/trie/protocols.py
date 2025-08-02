from typing import Protocol, Iterable, TypeVar, Literal, Sized

T = TypeVar("T", bound=Iterable)


class TrieProtocol(Sized, Protocol[T]):
    def complete(self, prefix: T) -> Iterable[T]:
        """Autocomplete search

        :param prefix: prefix of search sequences.
        :return: existed sequences which started from prefix.
        """
        ...

    def add(self, *words: T) -> None:
        """Add new words to the dictionary

        :param words: sequence of words which should be added.
        """
        ...