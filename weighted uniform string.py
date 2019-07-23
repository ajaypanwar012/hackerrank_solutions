def weightedUniformStrings(s, queries):
    weights = set()
    prev = -1
    length = 0
    for c in s:
        weight = ord(c) - ord('a') + 1
        weights.add(weight)
        if prev == c:
            length += 1
            weights.add(length*weight)
        else:
            prev = c
            length = 1
     
    for q in queries:
        if q in weights:
            print("Yes")
        else:
            print("No")
s = input()
queries_count = int(input())

queries = []

for _ in range(queries_count):
    queries_item = int(input())
    queries.append(queries_item)

weightedUniformStrings(s, queries)