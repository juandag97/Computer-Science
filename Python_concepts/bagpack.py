
def bagpack(size_bag, weights, values, n):
    # Always remember to define the base case
    if n == 0 or size_bag == 0:
        return 0
    if weights[n - 1] > size_bag:
        return bagpack(size_bag, weights, values, n - 1)
    return max(values[n - 1] + bagpack(size_bag - weights[n - 1], weights, values, n-1),
            bagpack(size_bag, weights, values, n-1))

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10,20,30]
    size_bag = 5
    n = len(values)

    result = bagpack(size_bag, weights, values, n)
    print(result)