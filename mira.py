def greet(name):
    return f"Hello, {name}!"

# List of names
names = ["Mira", "Alex", "Sam"]

# Loop through and greet each one
for name in names:
    print(greet(name))

# Simple calculation
total = sum(len(n) for n in names)
print(f"Total characters in all names: {total}")