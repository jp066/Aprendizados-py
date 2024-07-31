#def reverse_array_1(array):
#    vetor = []
#    for indice in array:
#        vetor.insert(0, indice)
#    return vetor
#
#def reverse_array_2(array):
#    return array[::-1]
#
#def reverse_array_3(array):
#    return list(reversed(array))
#
#array = [1, 2, 3, 4, 5]
#print(reverse_array_1(array))  # Output: [5, 4, 3, 2, 1]
#print(reverse_array_2(array))  # Output: [5, 4, 3, 2, 1]
#print(reverse_array_3(array))  # Output: [5, 4, 3, 2, 1]

def hourglassSum(arr):
    max_sum = float('-inf')  # Initialize with a very small number
    
    for i in range(4):  # Hourglass center row can be from 0 to 3
        for j in range(4):  # Hourglass center column can be from 0 to 3
            # Compute the sum of the hourglass centered at (i, j)
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass = top + middle + bottom
            
            # Update the maximum hourglass sum
            if hourglass > max_sum:
                max_sum = hourglass
    
    return max_sum

# Input reading and function call
arr = [list(map(int, input().split())) for _ in range(6)]

# Call the function and print the result
print(hourglassSum(arr))