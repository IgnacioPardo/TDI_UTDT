def nueva_bodega(s:str) -> bool:
	"""
	Descripcion: 	Dado un string no vacio, devuelve True si y solo si dentro de esos string 
					se encuentran las palabras "nueva", "bodega", o "vino"
	Pre: len(s) != 0
	Post: Si "nueva", "bodega", o "vino" se encuentran en s devuelve True, de lo contrario False
	"""
	vr:bool = "nueva" in s or "bodega" in s or "vino" in s or "Nueva" in s or "Bodega" in s or "Vino" in s
	return vr

nueva_bodega("En mi bodega tengo muchos vinos") #True
nueva_bodega("En mi casa no queda vino") #True
nueva_bodega("Hola como estas") #False
nueva_bodega("Mira mi nueva cartera") #True
nueva_bodega("El vino es una bebida obtenida de la uva, mediante la fermentación alcohólica de su mosto o zumo") #True
#Tiene en cuenta mayuscula?
nueva_bodega("Bodega es lugar donde se elaboran y almacenan vinos") #True
nueva_bodega("Hoy es viernes") #False
nueva_bodega("Bienvenidos a Introduccion a la Programacion") #False
nueva_bodega("2+2 = 4") #False