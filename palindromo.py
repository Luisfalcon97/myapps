""" def no_space(texto):
    nuevo_texto = ""
    for chart in texto:
        if chart != " ":
            nuevo_texto += chart
    return nuevo_texto
            
            
def es_palindromo(texto):
    texto = no_space(texto).lower()
    otxet = texto[::-1]
    if texto == otxet:
        return True
    else:
        return False
    

print("Abba", es_palindromo("Abba"))
print("Roma", es_palindromo("Roma"))
print("Amo la paloma", es_palindromo("Amo la paloma")) """

def no_space(texto):
    return texto.replace(" ", "")

def es_palindromo(texto):
    texto = no_space(texto).lower()
    otxet = texto[::-1]
    return texto == otxet


print("Abba", es_palindromo("Abba"))
print("Amo la paloma", es_palindromo("Amo la paloma"))


        





    
    

