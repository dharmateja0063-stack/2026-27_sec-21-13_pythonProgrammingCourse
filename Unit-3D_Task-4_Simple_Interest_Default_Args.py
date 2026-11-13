def simple_interest(p, t, r=5):
    si = (p * t * r) / 100
    return si

print("Default Rate Interest =", simple_interest(1000, 2))
print("Explicit Rate Interest =", simple_interest(1000, 2, 10))