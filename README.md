# Python Data Structures & Algorithms

Core data structures and algorithms implemented from scratch in Python (no external libraries), written as self-study during Fall 2025. Each topic has a main implementation plus practice problems I solved on top of it.

> **Note:** I followed the [COURSE NAME / INSTRUCTOR] course while building this repo. The implementations were written and tested by me as I worked through it.

## Contents

| Folder | What's inside |
|---|---|
| `linked_lists/` | Singly and doubly linked lists, plus practice problems |
| `stacks_queues/` | Stack and queue implementations |
| `hash_tables_sets/` | Hash table (with collision handling) and set-based problems |
| `trees/` | Binary search tree (iterative and recursive), tree traversals (BFS/DFS), tree inversion |
| `heaps/` | Max heap (insert, remove, sink down) and heap-based problems |
| `graphs/` | Undirected graph using an adjacency list |
| `sorts/` | Bubble, selection, insertion, merge, and quick sort |
| `recursion/` | Recursion basics (factorial) |
| `dynamic_programming/` | Fibonacci with memoization |

Files named `*problem*` are practice problems for the topic in the same folder.

## Time Complexity Summary

| Structure | Access / Search | Insert | Remove | Notes |
|---|---|---|---|---|
| Singly linked list | O(n) | O(1) at ends, O(n) in middle | O(n) | |
| Doubly linked list | O(n) | O(1) at ends, O(n) in middle | O(1) at ends, O(n) in middle | |
| Stack | O(n) | O(1) push | O(1) pop | LIFO |
| Queue | O(n) | O(1) enqueue | O(1) dequeue | FIFO |
| Hash table | O(1) average | O(1) average | O(1) average | O(n) worst case on collisions |
| Binary search tree | O(log n) average | O(log n) average | O(log n) average | O(n) worst case if unbalanced |
| Max heap | O(1) peek max | O(log n) | O(log n) | |
| Graph (adjacency list) | O(V + E) traversal | O(1) add vertex | depends on vertex degree | |

| Sorting algorithm | Best | Average | Worst |
|---|---|---|---|
| Bubble sort | O(n) | O(n²) | O(n²) |
| Selection sort | O(n²) | O(n²) | O(n²) |
| Insertion sort | O(n) | O(n²) | O(n²) |
| Merge sort | O(n log n) | O(n log n) | O(n log n) |
| Quick sort | O(n log n) | O(n log n) | O(n²) |

## How to Run

Requires Python 3. Each file runs on its own:

```
python trees/BST.py
python heaps/heaps.py
python sorts/quicksort.py
```

Most files include a small example at the bottom that prints the result.

## What I Practiced

- Pointer-style manipulation with nodes (linked lists, trees)
- Recursion and tree traversal patterns
- Choosing a data structure based on time complexity
- Writing sorting algorithms and comparing their trade-offs

## Author

Emre Karaoğlu, Computer Engineering student at Istanbul Technical University