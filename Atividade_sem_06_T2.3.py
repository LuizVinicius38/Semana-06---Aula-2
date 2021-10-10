def consoantes(z):
    t = True
    f = False
    if z in ("b", "c", "d", "f", "g", "h", "j", "k", "l",
              "m", "n", "p", "q", "r", "s", "t", "v", "x",
              "y", "w", "z"):
        return t
    else:
        return f
letras = str(input("")).lower()
print(consoantes(letras))
