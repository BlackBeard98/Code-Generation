class Ejemplo:
	def __init__(self, nombre:str):
		self.nombre = nombre
		
	def m_instancia(self):
		print(self.nombre)
	
	@classmethod
	def m_clase_nombre(cls):
		print(cls.__name__)
	
	# Este metodo deberia ser estatico
	def saludo(self):
		print("Hola mundo")