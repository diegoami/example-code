from operator import itemgetter

def sort_by_key(sequence, key):
    return sorted(sequence, key=key)

if __name__ == "__main__":
    from multiprocessing import Pool

    items = [([(1,2),(4,1)], itemgetter(1)),
             ([(5,3),(2,7)], itemgetter(0))]

    with Pool(5) as p:
        result = p.starmap(sort_by_key, items)
    print(result)