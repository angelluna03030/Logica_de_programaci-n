def juegetesbusqueda(jugetesid):
    lent = len(jugetesid)
    repetir = -1
    for i in range(lent):
        for j in range(i + 1, lent):
            a = jugetesid[i]
            b = jugetesid[j]
        if a == b:
            repetir = a
            lent = j 
jugetesid = [1,2,3,4,45,2,4,90,7,8,9,0]
resultado = juegetesbusqueda(jugetesid)
print(resultado)
            
        




