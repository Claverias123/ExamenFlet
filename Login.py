import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"

    #Ejercicio 6
    dlg = ft.AlertDialog(title=ft.Text("La contraseña es correcta"))
    def comprobacion(w):
        if tfnombre.value==tfpassword.value:
            page.dialog = dlg
            dlg.open = True
            page.update()

    #Fin --- Ejercicio 6


    #Ejercicio 2
    img = ft.Image(
        src=f"/fotos/Logo.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN)
    
    #Fin --- Ejercicio 2


    #Ejercicio 3
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.window_height=500
    page.window_width= 250
    

    #Fin --- Ejercicio 3
    



    
    #Ejercicio 4
    tfnombre = ft.TextField(label="Nombre")
    tfpassword = ft.TextField(label="Password", password=True, can_reveal_password=True)

    #Fin --- Ejercicio 4


    #Ejercicio 5
    btnEntrar=ft.ElevatedButton("Comprobar", icon="ADD", on_click=comprobacion)
    #Fin-- Ejercicio 5
    

    page.add(img,tfnombre,tfpassword,btnEntrar)
    


ft.app(target=main,assets_dir="fotos")