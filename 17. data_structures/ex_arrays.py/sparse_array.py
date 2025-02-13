def matching_strings(strings, queries):
    results = []
    for i in range(len(queries)):
        count = 0 
        for j in range (len(strings)):
            if queries[i] == strings[j]:
                count += 1
        results.append(count)
    return results

strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']
    
print(matching_strings(strings, queries)) 
print(matching_strings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab']))