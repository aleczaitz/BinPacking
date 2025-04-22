from exact import bin_packing_exact
import time
from approximate import first_fit_dec, best_fit_dec



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
    # Load data
    data = load_items("../data/data4.txt")
    bin_capacity = 1

    print(f"Bin size: {bin_capacity}\n")

    print("\nRunning Exact Algorithm...")
    start_time = time.time()
    packed_bins = bin_packing_exact(data, bin_capacity)
    end_time = time.time()
    for i, b in enumerate(packed_bins):
        print(f'Exact Bin {i + 1}: {b.items}')
    print(f"Exact Algo Time: {end_time - start_time:.4f} seconds")
    print(f"Exact Algo - Bins used: {len(packed_bins)}")


    print("\nRunning First-Fit Decreasing (FFD)...")
    start_time = time.time()
    ffd_bins = first_fit_dec(data, bin_capacity)
    end_time = time.time()
    for i, b in enumerate(ffd_bins):
        print(f'FFD Bin {i + 1}: {b}')
    print(f"FFD Time: {end_time - start_time:.4f} seconds")
    print(f"FFD - Bins used: {len(ffd_bins)}")


    print("\nRunning Best-Fit Decreasing (BFD)..")
    start_time = time.time()
    bfd_bins = best_fit_dec(data, bin_capacity)
    end_time = time.time()
    for i, b in enumerate(bfd_bins):
        print(f'BFD Bin {i + 1}: {b}')
    print(f"BFD Time: {end_time - start_time:.4f} seconds")
    print(f"BFD - Bins used: {len(bfd_bins)}")



if __name__ == "__main__":
    main()
