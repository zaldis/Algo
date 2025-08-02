from typing import Protocol, TypeVar, Sequence

T = TypeVar("T")


class Heap(Protocol[T]):
    @staticmethod
    def of(*nodes: T) -> 'Heap[T]':
        """
        :return: Heap instance which will be built based on provided nodes.
        """
        ...

    @property
    def size(self) -> int:
        """
        :return: Amount of nodes in the Heap.
        """
        ...

    @property
    def head(self) -> int:
        """
        :return: Head of the Heap.
        :raise EmptyHeapError: If heap is empty during removing.
        """
        ...

    def add_node(self, node: T) -> None:
        """ Add new node in the proper position in the Heap

        :param node: The instance of new node.
        """
        ...

    def extract_head(self) -> T:
        """ Remove the current head from the Heap

        The heap will be rebalanced after removing the head.

        :return: The current (removed) head.
        :raise EmptyHeapError: If heap is empty during removing.
        """
        ...