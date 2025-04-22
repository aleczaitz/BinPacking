# Bin Packing Problem
#### Algorithms Final - Matthew Hamp & Alec Zaitz

### Algorithms being tested:
- `Exact`: recurses through every possibility
- `First-fit`: places each item in the one it fits in first
- `Best-fit`: places each item in a spot that minimizes overall space left

### To Test:
1. Make necessary adjustments under the `#load data` comment in `main.py`.
2. Run the `main.py` in an IDE or in the terminal.
3. Console will print out where each algorithm place each item, along with
its running time and number of bins used.

### Sample Test:
```
Running Exact Algorithm...
Exact Bin 1: [0.65, 0.24]
Exact Bin 2: [0.83, 0.13]
Exact Bin 3: [0.56, 0.39]
Exact Bin 4: [0.71, 0.21]
Exact Bin 5: [0.97]
Exact Bin 6: [0.58, 0.36]
Exact Bin 7: [0.44, 0.49]
Exact Bin 8: [0.77, 0.18]
Exact Bin 9: [0.66, 0.33]
Exact Bin 10: [0.92]
Exact Bin 11: [0.62]
Exact Bin 12: [0.55]
Exact Algo Time: 2.6351 seconds
Exact Algo - Bins used: 12
```
