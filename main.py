from exact import BinPackingExact


def load_items(filename):
    """parse a data file and return a list of items"""
    return None


def main():
    data = load_items("data1.txt")
    packed_bins = BinPackingExact(data)
    print(packed_bins)


if __name__ == "__main__":
    main()
