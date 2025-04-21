class Bin:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def get_sum(self):
        items_sum = 0
        for item in self.items:
            items_sum += item
        return items_sum

    def is_full(self):
        return self.get_sum() >= self.capacity

    def add_item(self, item):
        if self.capacity - self.get_sum() >= item:
            self.items.append(item)
        else:
            raise Exception("Bin Overflow")
