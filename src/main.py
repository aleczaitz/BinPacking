from exact import bin_packing_exact


def load_items(filename):
    """parse a data file and return a list of items"""
    try:
        with open(filename) as file:
            lines = file.readlines()
            items = []
            for line in lines:
                line = line.strip()
                if line == "":
                    continue  # skip blank lines
                items.append(float(line))
        return items
    except ValueError:
        raise Exception("Error loading file")
    except FileNotFoundError:
        raise Exception(f'File {filename} not found')


def main():
    data = load_items("../data/data1.txt")
    packed_bins = bin_packing_exact(data, 1)
    for i, b in enumerate(packed_bins):
        print(f'Bin {i + 1}: {b.items}')


if __name__ == "__main__":
    main()
