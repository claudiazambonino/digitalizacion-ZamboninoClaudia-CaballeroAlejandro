entrada_usuario = input("Introduce el nombre de un país: ")

pais = entrada_usuario.strip().lower()

if pais == "españa" or pais == "francia" or pais == "italia":
    print(entrada_usuario.strip(), " está en EUROPA.")
elif pais == "argentina" or pais == "méxico" or pais == "colombia":
    print(entrada_usuario.strip(), " está en AMÉRICA.")
elif pais == "japón" or pais == "china" or pais == "india":
    print(entrada_usuario.strip(), " está en ASIA.")
elif pais == "egipto" or pais == "sudáfrica" or pais == "marruecos":
    print(entrada_usuario.strip(), " está en ÁFRICA.")
else:
    print("País no registrado.")


