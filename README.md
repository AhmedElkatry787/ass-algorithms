# ass-algorithms

CS314 algorithms tasks, one folder per lecture.

| Folder | Topic | Files |
|---|---|---|
| `lecture1` | Insertion sort | `insertion_sort.py`, `test_insertion_sort.py`, `experiment.py` |
| `lecture2` | Merge sort and quick sort | `sorts.py`, `test_sorts.py`, `measure.py` |
| `lecture3` | Heap sort | `heap_sort.py`, `test_heap_sort.py`, `measure.py` |

`lecture3/measure.py` compares heap sort with merge sort and quick sort, so it uses `lecture2/sorts.py`.

## Run

From inside a lecture folder:

```bash
python test_insertion_sort.py   # lecture1
python test_sorts.py            # lecture2
python test_heap_sort.py        # lecture3
python measure.py               # timings (lecture2, lecture3)
```
