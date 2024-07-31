def dynamicArray(n, queries):
    # Initialize the lists
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    results = []

    # Process each query
    for query in queries:
        type_query, x, y = map(int, query.split())
        if type_query == 1:
            idx = (x ^ lastAnswer) % n
            arr[idx].append(y)
        elif type_query == 2:
            idx = (x ^ lastAnswer) % n
            size = len(arr[idx])
            lastAnswer = arr[idx][y % size]
            results.append(lastAnswer)
    
    return results

# Test case
n = 2
queries = [
    "1 0 5",
    "1 1 7",
    "1 0 3",
    "2 1 0",
    "2 1 1"
]

print(dynamicArray(n, queries))  # Expected output: [7, 3]
