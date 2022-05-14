import click

from menu import Menu

from folder import Folder

from files import File

# creamos grupo de comando con click y funcion group
# creamos funcion principal

@click.group()
def main():
    pass

# creamos comandos, para ejecutar el menu o una accion en concreto: python main.py nombre_comando

# saludar al usuario
@main.command()
def greet():
    print('Bienvenido/a al CLI de archivos.')

# mostrar menu de opciones
@main.command()
def start():

    menu = Menu()

    while True:
        
        option = menu.show_menu()
        
        if option == 'a':
            
            folder = Folder()
            
            folder.list_files()
            
        elif option == 'b':
            
            file_txt = File()
            
            file_txt.show_content()
            
        elif option == 'c':
            
            file_txt = File()
            
            file_txt.edit()

        elif option == 'd':
        
            file_txt = File()

            file_txt.delete()

        elif option == 'e':

            print('Hasta pronto.')

            quit()

        else:
            print('Elige una opción correcta.')

# listar archivos .txt de un directorio
@main.command()
def list():
    folder = Folder()
    folder.list_files()

# abrir documento .txt
@main.command()
def show():
    file_txt = File()
    file_txt.show_content()

# crear/editar documento .txt
@main.command()
def create():
    file_txt = File()
    file_txt.edit()

# eliminar documento .txt
@main.command()
def remove():
    file_txt = File()
    file_txt.delete()

# ver comandos
@main.command()
def help():
    print(' Listado de comandos:\nSaludar: greet\nListar archivos: list\nAbrir archivo: show\nCrear / editar archivo: create\nEliminar archivo: remove')