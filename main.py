def es_palindromo(text): # Verifica si el texto dado es un palíndromo
    
    # Limpiar el texto: convertir a minúsculas y eliminar caracteres no alfanuméricos
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]
    
text = input("Ingrese un texto para verificar si es palíndromo: ")

# Verificar y mostrar resultado
if es_palindromo(text):
    print("Es palíndromo")
else:
    print("No es palíndromo")
