categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_expenses = expenses[0]
iof_max_expenses = 0

for i in range(len(expenses)):
    if max_expenses < expenses[i]:
        iof_max_expenses = i
        max_expenses = expenses[i]

print('The most expensive category:', categories[iof_max_expenses])
print('It costs:', max_expenses)