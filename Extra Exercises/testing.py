"""
Escribir un programa en que se pregunte al usuario por una frase y una letra, y muestre en la pantalla el 
número de veces que esta esa letra en la frase.
"""

phrase=input("Ingrese una frase: ")
letter=input("Ingrese una letra: ")
count=0

for char in phrase:
    if char==letter:
        count +=1

print(f"La letra {letter} aparece {count} veces en la frase.")
    

