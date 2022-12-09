import random

with open("big_file.txt", "a") as f:
    for line in range(150000):
        f.write(str([int(random.random() * 10) for num in range(50)]).replace("[", "").replace("]", "") + "\n")

sum = 0
count = 0
avg = 0


with open("big_file.txt", "r") as f:
    for line in f:
        for num in line.replace(", ", "").replace("\n", ""):
            sum += int(num)
            count += 1

avg = sum / count
print("Sum: ", sum, "Avg: ", avg)