name = "Mira"
age = 19
gpa = 3.85

print("My name is %s and I am %d years old" % (name, age))

print("My name is {} and I am {} years old".format(name, age))
print("My name is {0} and I am {1} years old. {0} is a student.".format(name, age))
print("My name is {n} and I am {a} years old".format(n=name, a=age))

print(f"My name is {name} and I am {age} years old")
print(f"GPA rounded: {gpa:.1f}")
print(f"Age squared: {age ** 2}")

price = 1234567.891
print(f"{price:,.2f}")
print(f"{age:05d}")
print(f"{gpa:>10.2f}")
print(f"{name:<10}|")
print(f"{name:^10}|")