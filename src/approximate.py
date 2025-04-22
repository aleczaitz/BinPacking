def first_fit_dec(items, capacity):
    """First-Fit Decreasing"""
    items = sorted(items, reverse=True)
    bins = []


    for item in items:
        placed = False
        for b in bins:
            if sum(b) + item <= capacity:

                b.append(item)
                placed = True
                break
        if not placed:

            bins.append([item])
    return bins


def best_fit_dec(items, capacity):
    """Best-Fit Decreasing"""

    items = sorted(items, reverse=True)

    bins = []

    for item in items:

        best_index = -1
        min_space_left = float('inf')

        for i, b in enumerate(bins):
            space_left = capacity - sum(b)
            if item <= space_left and space_left < min_space_left:
                best_index = i
                min_space_left = space_left


        if best_index != -1:
            bins[best_index].append(item)


        else:
            bins.append([item])

    return bins
