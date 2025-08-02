<p align="center">
<img src="./img/algo_logo.png" width="500" />
</p>

# Zaldis Algo

Implementations of known data structures and algorithms in Python.

Dependencies:

* Python 3.12+

## Implemented algorithms

### Data Structures

* [Undirected Graph](./zaldisalgo/ds/graph/undirected_graph.py)
* [Hash Table](./zaldisalgo/ds/hash_table/main.py)
* [Binary Heap](./zaldisalgo/ds/heap)
* [Trie](./zaldisalgo/ds/trie)

### Algorithms

* [Binary Search](./zaldisalgo/algos/search/binary_search/main.py)
* [Sort Algos](./zaldisalgo/algos/sort)

## How to test

* Install [poetry](https://python-poetry.org/) package manager.
* Install dependencies: `poetry install`.
* Run `poetry run pytest tests`.

> Alternatively all algorithms provide run example in theirs files.