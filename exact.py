from bin import Bin


def bin_packing_exact(items, capacity):
    """
    Exact Algorithm - creates a recursive branch for
    every scenario of where you place each item,
    including in its own bin

    Base case = index == len(items)

    Making sure to backtrack and undo the placement
    after each placement

    Keep the best solution, found so far, and check if
    it should be updated at the end of each recursion
    """
    best_solution_bins = []

    def recurse(bins, index):
        nonlocal best_solution_bins

        # Base case: all items have been placed
        if index == len(items):
            if best_solution_bins == [] or len(bins) < len(best_solution_bins):
                # Deep copy to avoid mutation on backtrack
                best_solution_bins = [Bin(capacity) for b in bins]
                for i, bin in enumerate(bins):
                    best_solution_bins[i].items = bin.items[:]
                    best_solution_bins[i].current_weight = bin.current_weight
            return

        current_item = items[index]

        # Try placing item in existing bins
        for bin in bins:
            if bin.can_fit(current_item):
                bin.add_item(current_item)
                recurse(bins, index + 1)
                bin.remove_item(current_item)

        # Try placing item in a new bin
        new_bin = Bin(capacity)
        new_bin.add_item(current_item)
        bins.append(new_bin)
        recurse(bins, index + 1)
        bins.pop()  # backtrack

    # Start recursion with empty bin list and index 0
    recurse([], 0)
    return best_solution_bins

