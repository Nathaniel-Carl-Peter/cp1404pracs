"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
get sales
if sales >= 1,000
    bonus = sales * 0.15
else:
    bonus = sales * 0.1
display bonus
"""

# sales = float(input("Enter sales: $"))
# if sales >= 1000:
#     bonus = sales * 0.15
# else:
#     bonus = sales * 0.1
# print(f"Your bonus ${bonus}")

# Version 2 with loop
"""
Pseudo:

get sales
while sales >= 0
    calculate bonus
    get sales
do next thing
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1  # 10%
    else:
        bonus = sales * 0.15  # 15%
    print(f'Your bonus is ${bonus:.2f}')
    sales = float(input("Enter sales: $"))

"""
Test input and Expected Output:

5000 = 50
2000 = 300
1000 = 150
"""
