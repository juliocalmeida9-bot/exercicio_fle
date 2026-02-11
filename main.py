import flet as ft

def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(ft.Text("A familia em primeiro lugar"))

    page.add(
        ft.Text("Olá! Eu sou toreto!"),
        ft.Image(
            src="toreto.webp",
            height=200
        ),
        ft.Button(
            content="Acreditar!",
            on_click=mostrar_mensagem
        )
    )

ft.app(main)
