import random
import math


def sphere(x):
    return sum(a * a for a in x)


def rastrigin(x):
    return 10 * len(x) + sum(a * a - 10 * math.cos(2 * math.pi * a) for a in x)


def absolute(x):
    return sum(abs(a) for a in x)


def prt_vector(dim, prt):
    return [1 if random.random() < prt else 0 for _ in range(dim)]


def soma(func, low, high, dim, variant, pop_size=25, maxfes=20000,
         step=0.22, path_length=3, prt=0.3, migrations=1000):
    if variant not in (1, 2, 3):
        raise ValueError('Neznama strategia')

    pop = [[random.uniform(low, high) for _ in range(dim)] for _ in range(pop_size)]
    values = [func(x) for x in pop]
    fes = pop_size
    migration = 0

    while migration < migrations and fes < maxfes:
        if variant == 1:
            leader = random.randrange(pop_size)
        elif variant == 2:
            leader = values.index(min(values))

        new_pop = pop[:]
        new_values = values[:]

        for i in range(pop_size):
            if variant == 3:
                leaders = range(pop_size)
            else:
                leaders = [leader]

            start = pop[i]
            for j in leaders:
                if i == j:
                    continue

                for k in range(1, int(path_length / step) + 1):
                    if fes >= maxfes:
                        break
                    t = k * step
                    vector = prt_vector(dim, prt)
                    x = [start[d] + (pop[j][d] - start[d]) * t * vector[d]
                         for d in range(dim)]
                    if all(low <= a <= high for a in x):
                        value = func(x)
                        fes += 1
                        if value < new_values[i]:
                            new_pop[i] = x
                            new_values[i] = value
                if fes >= maxfes:
                    break
            if fes >= maxfes:
                break

        pop = new_pop
        values = new_values
        migration += 1

    return min(values), fes


def test():
    functions = [(sphere, -5.12, 5.12), (rastrigin, -5.12, 5.12),
                 (absolute, -100, 100)]
    names = ['All-To-Random', 'All-To-Best', 'All-To-All']

    for func, low, high in functions:
        print('\n' + func.__name__)
        for variant in range(1, 4):
            results = []
            for run in range(10):
                random.seed(run)
                value, fes = soma(func, low, high, 6, variant,
                                  pop_size=10 if variant == 3 else 25)
                results.append(value)
                assert fes == 20000
            print(f'{names[variant - 1]}: best={min(results):.6g}, avg={sum(results) / len(results):.6g}')


if __name__ == '__main__':
    test()
