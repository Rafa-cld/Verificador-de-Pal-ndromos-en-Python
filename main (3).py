text = "Eleven animals I slam in a net"
def es_palindromo(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

if es_palindromo(text):
    print("Es palíndromo")
else:
    print("No es palíndromo")