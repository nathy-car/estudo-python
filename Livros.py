import flet as ft
import requests

# Função principal do app
def main(page: ft.Page):
    page.title = "Exemplo API com Flet"
    page.scroll = "auto"

    titulo = ft.Text("Usuários da API", size=24, weight="bold")
    lista = ft.Column()

    # Botão para buscar API
    def buscar_dados(e):
        lista.controls.clear()  # limpa lista antes de carregar novos dados

        # Chamada à API pública
        resposta = requests.get("https://jsonplaceholder.typicode.com/users")
        if resposta.status_code == 200:
            usuarios = resposta.json()
            for u in usuarios:
                lista.controls.append(
                    ft.Card(
                        content=ft.ListTile(
                            title=ft.Text(u["name"], weight="bold"),
                            subtitle=ft.Text(f"Email: {u['email']} | Cidade: {u['address']['city']}")
                        )
                    )
                )
        else:
            lista.controls.append(ft.Text("Erro ao buscar dados da API.", color="red"))

        page.update()

    botao = ft.ElevatedButton("Buscar dados", on_click=buscar_dados)

    # Adiciona elementos na tela
    page.add(titulo, botao, lista)


# Rodar app
ft.app(target=main)
