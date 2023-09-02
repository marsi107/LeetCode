def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Create a generator object
cd = countdown(5)

# Iterating over the generator
for num in cd:
    print(num)

print(__name__)
import this
import antigravity