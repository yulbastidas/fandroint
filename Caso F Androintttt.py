#caso f androind donde el usuario una vez realizado su compra ya no necesita volver agregar los datos 
#realizado por Yuly Bastidas, Alvaro Felipe Valenzuela 

class Usuario:
    def __init__(self, nombre, apellido, email, tarjeta):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta = tarjeta
        self.puntos = 0 
        
class Aplicacion:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class PlataformaVenta:
    def __init__(self):
        self.usuarios = {}
        self.aplicaciones = {}

    def crear_usuario(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        email = input("Ingrese su correo electrónico: ")
        tarjeta = input("Ingrese el número de su tarjeta de crédito: ")

        nuevo_usuario = Usuario(nombre, apellido, email, tarjeta)
        self.usuarios[email] = nuevo_usuario

    def agregar_aplicacion(self, nombre, precio):
        nueva_aplicacion = Aplicacion(nombre, precio)
        self.aplicaciones[nombre] = nueva_aplicacion

    def realizar_compra(self, email, aplicacion):
        if email in self.usuarios and aplicacion in self.aplicaciones:
            usuario = self.usuarios[email]
            app = self.aplicaciones[aplicacion]
            usuario.puntos += 10 
            print(f"Compra exitosa. Se ha cobrado ${app.precio} a la tarjeta {usuario.tarjeta}.")
            print("¡Compra realizada!")
            print("Se te han sumado 10 puntos a la cuenta")
            print(f"Total de puntos de {usuario.nombre}: {usuario.puntos}")
        else:
            print("No se pudo completar la compra. Verifique su información.")

plataforma = PlataformaVenta()

plataforma.crear_usuario()
plataforma.agregar_aplicacion("Netflix", 10.99)
plataforma.agregar_aplicacion("HBO", 5.99)

email_usuario = input("Ingrese su correo electrónico para realizar la compra: ")
app_compra = input("Ingrese el nombre de la aplicación que desea comprar: ")
plataforma.realizar_compra(email_usuario, app_compra)

