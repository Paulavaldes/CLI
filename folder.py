from pathlib import Path

# Clase en la que se define metodo para especificar directorio y listar archivos
class Folder:
    
    # metodo para seleccionar un directorio que devuelve listado de archivos .txt que contiene
    def list_files(self):

        self.directory = input('Ingresa un directorio: ')

        # instanciar objeto path con el que vamos a trabajar
        self.files_directory = Path(self.directory)

        # obtenemos directorio actual
        self.current_directory = Path.cwd()

        # si el directorio q introduce el usuario existe, listamos sus archivos .txt
        if self.files_directory.is_dir():

            self.file = False
            
            for dir in self.files_directory.iterdir():

                if dir.is_file() and dir.suffix == '.txt':

                    print('Nombre: ', dir.name)

                    self.file = True

            if not self.file:
                
                print('No hay archivos .txt')

        # si no existe, se usa el directorio actual por defecto
        else:
            print('El directorio introducido no existe, estamos en el directorio actual.')
            
            self.file = False

            for dir in self.current_directory.iterdir(): 

                if dir.is_file() and dir.suffix == '.txt':

                    print('Nombre: ', dir.name)
                    
                    self.file = True
            
            if not self.file:
                
                print('No hay archivos .txt')