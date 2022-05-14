# Clase en la que se define el metodo para crear menu principal

class Menu:
    
    def show_menu(self):
    
        print('a) Listar documentos \nb) Abrir documento \nc) Crear / Editar documentos \nd) Eliminar documento \ne) Salir')
    
        self.option = input('Ingresa una opción (a, b, c, d, e): ').lower()
    
        return self.option