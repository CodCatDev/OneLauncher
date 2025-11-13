import flet as ft
import os
import pyperclip

class LauncherConfig:
    PATH = "D:\\Projects\\Flet-Ui\\OneLauncher\\"
    DATA_DIR = "data\\"
    SAVE_FILE = "saved.json"

class Error:
    def __init__(self, page: ft.Page, text: str, logs: str = ""):
        self.page = page
        self.text = text
        self.logs = logs
        self.content = ft.Container(
            content=ft.Column([
                ft.Text("Произошла ошибка запуска", size=30, weight=ft.FontWeight.BOLD),
                ft.Text(self.text, size=20, weight=ft.FontWeight.NORMAL),
                ft.Row([
                    ft.TextButton("Закрыть", on_click=lambda e: self.page.window.close()),
                    ft.ElevatedButton("Скопировать логи", on_click=lambda e: pyperclip.copy(self.logs))
                ])
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            border_radius=25,
            width=500,
            height=150,
            bgcolor="red",
            border=ft.border.all(3, ft.Colors.RED_900)
        )
    
    def build(self):
        self.page.add(self.content)
        self.page.update()

class Launcher:
    def __init__(self, page: ft.Page):
        self.page = page

        self.logs = ""
        self.logs += "Start logging.\n"

        self.title = "Onelauncher"
        self.updateTitle()
        self.page.window.width = 800
        self.page.window.height = 600
        self.page.window.resizable = False
        self.page.window.maximizable = False
        self.page.window.center()
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.on_route_change = self.routeChanged
        result = self.checkInstalling()
        if result:
            pass
        else:
            self.sendError("No saved data")
            return
        self.update()

    def update(self):
        self.page.update()

    def sendError(self, text: str = "Error"):
        Error(self.page, text, self.logs).build()

    def updateTitle(self):
        self.page.title = self.title
        self.update()

    def checkInstalling(self):
        if os.path.exists(LauncherConfig.PATH):
            dat = self.readSave()
            if dat is not None:
                data = str(dat)
                return True
            else:
                return False

    def readSave(self):
        try:
            with open(LauncherConfig.PATH + LauncherConfig.DATA_DIR + LauncherConfig.SAVE_FILE, "r") as f:
                return f.read()
        except:
            self.logs += "Error reading saved data\n"
            return None

    def routeChanged(self, route: ft.RouteChangeEvent):
        self.updateTitle()
        print(route)