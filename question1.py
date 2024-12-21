a = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Pune", "Hyderabad"]

def f(x):
    v = "aeiouAEIOU"
    return ''.join([y for y in x if y not in v])

b = []
for c in a:
    b.append(f(c))

print("List without vowels:")
print(b)


b.sort(key=len)

print("Sorted list by length:")
print(b)
