# biblioteca.py


class Libro:
	def _init_(self, titulo, autor, isbn):
		self.titulo = titulo
		self.autor = autor
		self.isbn = isbn
		self.disponible = True
	
	def _str_(self):
		return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"


class Usuario:
	def _init_(self, nombre, id_usuario):
		self.nombre = nombre
		self.id_usuario = id_usuario
	
	def _str_(self):
		return f"{self.nombre} (ID: {self.id_usuario})"


class Reserva:
	def _init_(self, libro, usuario):
		self.libro = libro
		self.usuario = usuario
	
	def _str_(self):
		return f"Reserva: {self.libro} para {self.usuario}"


class Biblioteca:
	def _init_(self):
		self.libros = []
		self.usuarios = []
		self.reservas = []
	
	def agregar_libro(self, libro):
		self.libros.append(libro)
		print(f"Libro agregado: {libro}")
	
	def registrar_usuario(self, usuario):
		self.usuarios.append(usuario)
		print(f"Usuario registrado: {usuario}")
	
	def reservar_libro(self, isbn, id_usuario):
		libro = next((l for l in self.libros if l.isbn == isbn and l.disponible), None)
		usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
		
		if libro and usuario:
			libro.disponible = False
			reserva = Reserva(libro, usuario)
			self.reservas.append(reserva)
			print(f"Reserva realizada: {reserva}")
		else:
			print("Reserva no se pudo realizar. Libro o usuario no encontrado, o libro no disponible.")
	
	def mostrar_libros(self):
		for libro in self.libros:
			estado = "Disponible" if libro.disponible else "No disponible"
			print(f"{libro} - {estado}")
	
	def mostrar_usuarios(self):
		for usuario in self.usuarios:
			print(usuario)
	
	def mostrar_reservas(self):
		for reserva in self.reservas:
			print(reserva)