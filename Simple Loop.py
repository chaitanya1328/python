num = int(input("Enter a number for the table: "))
print(f"Multiplication Table for {num}:")
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")