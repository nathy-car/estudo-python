import flet as ft

def main(page: ft.Page):

    def add_task(e):
        print(new_task.value)
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ''
        page.update()
        

    new_task = ft.TextField(hint_text="Insira uma tarefa")
    new_button = ft.FloatingActionButton (icon = ft.Icons.ADD, on_click= add_task)

    page.add(new_task, new_button)

ft.app (target = main)