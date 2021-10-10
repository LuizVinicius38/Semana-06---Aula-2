def todos(a):     
    if entrada in ("a", "e", "i", "o", "u"):
           print("vogal")

    elif entrada in ("b", "c", "d", "f", "g", "h",
               "j", "k", "l", "m", "n", "p",
               "q", "r", "s", "t", "v", "x",
               "y", "w", "z"):
           print("consoante")

    elif entrada.isdigit():
        print("número")
    

    elif entrada in(" ", "ç", "/"):
           print("símbolo")
    else:
           print("símbolo")
entrada = input("").lower()
todos(entrada)



