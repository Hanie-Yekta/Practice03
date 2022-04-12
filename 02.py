# tul mar
print("Enter the the length of the snake:")
n = int(input())

for i in range(0, n):
    if i % 2 == 0:
        print("🟩", end="")
    else:
        print("🟨", end="")
