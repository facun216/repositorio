def funcion_Mayuscula(l):
	if  l.isupper()== True:
		print "La letra es : ", l
	else:
		print "La letra es : ", l.upper()

pepe=raw_input("Ingrese un Caracter ")
funcion_Mayuscula(pepe)