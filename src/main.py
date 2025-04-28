from exact import bin_packing_exact
import time
from approximate import first_fit_dec, best_fit_dec
from new_algos import first_fit_decreasing_lookahead, genetic_bin_packing


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
            print(f"\nNumber of items: {item_count}")
        return items
    except ValueError:
        raise Exception("Error loading file")
    except FileNotFoundError:
        raise Exception(f'File {filename} not found')


def main():
    files = ["../data/data1.txt", "../data/data2.txt", "../data/data3.txt", "../data/data4.txt"]
    bin_capacity = 1

    for file in files:
        print(f"\n=== Testing {file.split('/')[-1]} ===")
        data = load_items(file)
        print(f"Bin size: {bin_capacity}")

        # Exact Algorithm
        start_time = time.time()
        packed_bins = bin_packing_exact(data, bin_capacity)
        end_time = time.time()
        print(f"Exact - Bins: {len(packed_bins)} Time: {end_time - start_time:.8f}s")

        # First-Fit Decreasing (FFD)
        start_time = time.time()
        ffd_bins = first_fit_dec(data, bin_capacity)
        end_time = time.time()
        print(f"FFD - Bins: {len(ffd_bins)} Time: {end_time - start_time:.8f}s")

        # Best-Fit Decreasing (BFD)
        start_time = time.time()
        bfd_bins = best_fit_dec(data, bin_capacity)
        end_time = time.time()
        print(f"BFD - Bins: {len(bfd_bins)} Time: {end_time - start_time:.8f}s")

        # First-Fit Decreasing Lookahead (FFD-LA)
        start_time = time.time()
        ffd_la_bins = first_fit_decreasing_lookahead(data, bin_capacity)
        end_time = time.time()
        print(f"FFD-LA - Bins: {len(ffd_la_bins)} Time: {end_time - start_time:.8f}s")

        # Genetic Algorithm
        start_time = time.time()
        genetic_bins = genetic_bin_packing(data, bin_capacity)
        end_time = time.time()
        print(f"Genetic - Bins: {len(genetic_bins)} Time: {end_time - start_time:.8f}s")


if __name__ == "__main__":
    main()
