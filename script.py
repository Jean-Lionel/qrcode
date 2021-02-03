import  barcode
from barcode.writer import ImageWriter
from random import randint


def genarateCodeNumber(n):
    #Si necessaire on peut verifier que le code n'a pas été déjà générer avant
    #Si le code existe on generer l'autre
    code = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
    
    return code 
    

def generateBarCode(value):
    
    #for generating svg barcode
    hr = barcode.get_barcode_class('ean13')

    Hr = hr(value)
    #Nom d'enregistrement .svg
    qr = Hr.save(value)

    #for generating png barcode
    
    png = barcode.get_barcode_class('code39')

    Png = png(value,writer=ImageWriter())
    qr = Png.save(value)
    
 
code = genarateCodeNumber(13)   
generateBarCode(code);  
print(code)