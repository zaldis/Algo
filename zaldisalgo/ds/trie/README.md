# Trie

Specialized search tree data structure used to store and re<ins>trie</ins>ve strings from a dictionary or set.

A Trie for the following keys: "A", "to", "tea", "ted", "ten", "i", "in", "inn".

<p align="center">
    <img style="background-color: white" width="400" src="./img/trie_example.svg">
</p>

* [Implementation](./main.py)

## Algorithm Complexity

* `n` - size of keys dictionary.
* `p` - the length of the key (prefix).
* `l` - is the total number of characters in all words that match the given prefix.

<ins>Time</ins>:

* [Building](#building): `O(total-chracters(n))`
* [Insert operation](#insert): `O(p)`
* [Search operation](#search): `O(p)`
* [Autocomplete search](#autocomplete): `O(p + l)`

<ins>Memory</ins>: 
* Overall tree: `O(total-characters(N))`

## Implementation details

### Building

A Trie can be presented as a prefix tree.

Every node keeps information about edges (by dedicated "symbol") and prefix
starting from the root to this node.

To build this structure from the predefined dictionary, it's necessary for each key (word):
1. Iterate through dictionary's keys (words).
2. [Insert](#insert) this word.

### Insert

1. Iterate through symbols (word's letters).
2. Follow the available edge or create a new node, and its corresponding edge if it does not exist.

<p align="center">
    <img style="background-color: white" width="600" src="./img/trie_insert.svg">
</p>

### Search

1. Iterate through symbols (word's letters).
2. Follow the existing edge for the given "symbol".
3. If it's not possible to find the edge, then the prefix/word doesn't exist in the Trie.

### Autocomplete

1. [Search](#search) by passed prefix.
2. Then, find all available words by traversing the subtree using DFS.

<p align="center">
    <img style="background-color: white" width="600" src="./img/trie_autocomplete.svg">
</p>