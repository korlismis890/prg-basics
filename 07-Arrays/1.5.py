arr = [1, 2, 3, 4, 5]

arr[0] -= 1
print(f'First value subtracted by one: {arr}')

arr[len(arr) - 1] += 4
print(f'Increased last array element by 4: {arr}')

arr[(len(arr) - 1) // 2] *= 2
print(f'Mutiplied middle array element by 2: {arr}')