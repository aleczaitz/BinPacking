from exact import bin_packing_exact
import time


def load_items(filename):
    """parse a data file and return a list of items"""
    try:
        with open(filename) as file:
            lines = file.readlines()
            items = []
            item_count = 0
            for line in lines:
                line = line.strip()
                if line == "":
                    continue  # skip blank lines
                items.append(float(line))
                item_count += 1
            print(f"\nNumber of items: {item_count}\n")
        return items
    except ValueError:
        raise Exception("Error loading file")
    except FileNotFoundError:
        raise Exception(f'File {filename} not found')


def main():
    data = load_items("../data/data4.txt")
    start_time = time.time()
    packed_bins = bin_packing_exact(data, 1)
    end_time = time.time()
    for i, b in enumerate(packed_bins):
        print(f'Bin {i + 1}: {b.items}')
    print(f"\nExact Algorithm performance: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()
