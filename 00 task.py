import os

names = []
n = int(input("Total Absent => "))

# Open and read lines from the file
with open("ATTENDANCE SHEET.txt", "r") as f:
    lines = f.readlines()

# Clear the screen to avoid showing input (optional, depends on terminal)
os.system('cls' if os.name == 'nt' else 'clear')

# Collect absent student names
for i in range(n):
    roll = input(f"Enter Roll Number for Absent Student {i+1}: ").strip()
    found = False
    for line in lines:
        parts = line.strip().split('==')
        if len(parts) >= 2:
            Roll = parts[0].strip()
            name = parts[1].strip()
            if Roll == roll:
                names.append(name)
                found = True
                break
    if not found:
        names.append(f"Roll {roll} not found")

# Clear the screen again to show only final output (optional)
os.system('cls' if os.name == 'nt' else 'clear')

# Show absent names
print("Absent Students:")
print("----------------")
for name in names:
    print(name)