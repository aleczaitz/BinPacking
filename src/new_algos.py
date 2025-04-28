import random
import copy

def genetic_bin_packing(items, capacity, generations=50, population_size=30):
    """ Genetic Algorithm for Bin Packing"""
    def fitness(solution):
        return len(solution)

    def create_random_solution(items):
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

    def mutate(solution):
        if len(solution) < 2:
            return solution
        bin_from = random.choice(solution)
        if not bin_from:
            return solution
        item = random.choice(bin_from)
        bin_from.remove(item)

        for b in solution:
            if sum(b) + item <= capacity:
                b.append(item)
                return solution
        solution.append([item])
        return solution

    def crossover(parent1, parent2):
        split = len(parent1) // 2
        new_bins = parent1[:split] + parent2[split:]
        flattened = [item for bin in new_bins for item in bin]
        return create_random_solution(flattened)

    population = [create_random_solution(items) for _ in range(population_size)]



    for _ in range(generations):
        population = sorted(population, key=fitness)
        next_gen = population[:population_size//2]


        while len(next_gen) < population_size:

            parent1 = random.choice(population[:10])
            parent2 = random.choice(population[:10])
            child = crossover(copy.deepcopy(parent1), copy.deepcopy(parent2))
            if random.random() < 0.3:  # Mutate

                child = mutate(child)
            next_gen.append(child)

        population = next_gen


    best_solution = min(population, key=fitness)
    return best_solution




def first_fit_decreasing_lookahead(items, capacity):
    """First-Fit Decreasing with simple Lookahead"""
    items = sorted(items, reverse=True)
    bins = []


    i = 0
    while i < len(items):

        item = items[i]
        placed = False

        for b in bins:
            if sum(b) + item <= capacity:
                # Lookahead

                if i + 1 < len(items):
                    next_item = items[i + 1]
                    space_left_now = capacity - (sum(b) + item)
                    space_left_if_skip = capacity - sum(b)

                    if space_left_now >= next_item or space_left_if_skip < next_item:

                        b.append(item)
                        placed = True
                        break

                else:
                    b.append(item)
                    placed = True
                    break


        if not placed:
            bins.append([item])

        i += 1

    return bins
