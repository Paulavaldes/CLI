from pathlib import Path

# Clase en la que se definen metodos para manejo de archivos
class File:

    def __init__(self):

        self.file_name = input('Introduce el nombre del archivo: ')  


    # metodo para controlar la forma en la que el usuario introduce el nombre del archivo, que funcione con extension y sin extension
    def suffix(self):

        if self.file_name.endswith('.txt'):
            
            self.file = self.current_directory / self.file_name

        else:

            self.file = self.current_directory / f'{self.file_name}.txt'

   
    # abrir archivo .txt
    def show_content(self):
        
        self.current_directory = Path.cwd()

        self.suffix()

        # intentamos abrir el archivo sin validar que existe
        try:
            
            # creamos bloque with para que las variables que aqui se creen, se eliminen al abandonar el contexto, evitamos usar close() para cerrar el archivo
            # el metodo open no lleva segundo argumento, de esta forma el trabajo que hace por defecto es de solo lectura
            with open(self.file) as file:

                self.content = file.read()

                print(self.content)

        # si el archivo no existe, capturamos y gestionamos el error mediante Exception, la Clase padre de todas las excepciones
        except Exception as err:
        
            print('El archivo no existe.')

    
    # crear/editar archivo .txt
    # no usamos try except porque si el archivo introducido por el usuario no existe, se crea
    def edit(self):

        self.current_directory = Path.cwd()

        self.suffix()

        # bloque with para introducir texto en el archivo mediante metodo open con argumento append
        with open(self.file, 'a') as file: 

            file.write(input('Introduce texto: '))

        # bloque with para imprimir el archivo con el nuevo contenido
        with open(self.file, 'r') as file: 

            self.content = file.read()

            print(self.content)


    # eliminar archivo .txt
    def delete(self):
    
        self.current_directory = Path.cwd()

        self.suffix()

        try:
    
            self.file.unlink()

            print('El archivo ha sido eliminado.')
    
        except Exception as err:

            print('El archivo no existe.')