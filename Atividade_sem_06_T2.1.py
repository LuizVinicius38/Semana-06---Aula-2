letra = input("").lower()
def vogal(z):
    t = True
    f = False
    if z in ("a", "e", "i", "o", "u"):
        return t
    else:
        return f
print(vogal(letra))
