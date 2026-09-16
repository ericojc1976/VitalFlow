import flet as ft
from datetime import datetime
import json
import os

class HealthData:
    """Gerencia dados de saúde"""
    def __init__(self, data_file="vitalflow_data.json"):
        self.data_file = data_file
        self.data = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_today_data(self):
        today = datetime.now().strftime("%Y-%m-%d")
        if today not in self.data:
            self.data[today] = {
                "water": 0,
                "steps": 0,
                "calories": 0,
                "sleep": 0,
                "exercises": []
            }
        return self.data[today]
    
    def add_water(self, amount):
        self.get_today_data()["water"] += amount
        self.save_data()
    
    def add_steps(self, steps):
        self.get_today_data()["steps"] += steps
        self.save_data()
    
    def add_calories(self, calories):
        self.get_today_data()["calories"] += calories
        self.save_data()
    
    def add_sleep(self, hours):
        self.get_today_data()["sleep"] += hours
        self.save_data()

class VitalFlow:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "VitalFlow"
        self.page.window_width = 400
        self.page.window_height = 800
        self.page.theme_mode = "dark"
        
        self.health_data = HealthData()
        self.setup_theme()
        self.show_home_screen()
        
    def setup_theme(self):
        self.page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=ft.colors.TEAL_400,
                secondary=ft.colors.CYAN_400,
            )
        )
    
    def show_home_screen(self):
        """Tela inicial com estatísticas"""
        today_data = self.health_data.get_today_data()
        
        # Atualizar dados
        water_text = ft.Text(f"{today_data['water']:.1f}L", size=28, weight="bold", color=ft.colors.TEAL_400)
        steps_text = ft.Text(f"{today_data['steps']}", size=28, weight="bold", color=ft.colors.TEAL_400)
        calories_text = ft.Text(f"{today_data['calories']}", size=28, weight="bold", color=ft.colors.TEAL_400)
        sleep_text = ft.Text(f"{today_data['sleep']:.1f}h", size=28, weight="bold", color=ft.colors.TEAL_400)
        
        def add_water_action(e):
            today_data["water"] += 0.25
            self.health_data.save_data()
            water_text.value = f"{today_data['water']:.1f}L"
            self.page.update()
        
        def add_steps_action(e):
            today_data["steps"] += 100
            self.health_data.save_data()
            steps_text.value = f"{today_data['steps']}"
            self.page.update()
        
        def add_calories_action(e):
            today_data["calories"] += 100
            self.health_data.save_data()
            calories_text.value = f"{today_data['calories']}"
            self.page.update()
        
        def add_sleep_action(e):
            today_data["sleep"] += 0.5
            self.health_data.save_data()
            sleep_text.value = f"{today_data['sleep']:.1f}h"
            self.page.update()
        
        # Cards de estatísticas
        stats = ft.Column([
            self.create_stat_card_with_button("💧 Água", water_text, "Meta: 2L", add_water_action, "+250ml"),
            self.create_stat_card_with_button("🚶 Passos", steps_text, "Meta: 10.000", add_steps_action, "+100"),
            self.create_stat_card_with_button("🔥 Calorias", calories_text, "Meta: 2.000", add_calories_action, "+100"),
            self.create_stat_card_with_button("😴 Sono", sleep_text, "Meta: 8h", add_sleep_action, "+30min"),
        ], spacing=10)
        
        # Header
        header = ft.Container(
            content=ft.Column([
                ft.Text("VitalFlow", size=32, weight="bold", color=ft.colors.TEAL_400),
                ft.Text(datetime.now().strftime("%d/%m/%Y"), size=14, color=ft.colors.GREY_400)
            ]),
            padding=20,
            bgcolor=ft.colors.SURFACE_VARIANT,
        )
        
        # Navigation bar
        nav_bar = ft.Container(
            content=ft.Row([
                ft.IconButton(ft.icons.HOME, icon_size=28, icon_color=ft.colors.TEAL_400),
                ft.IconButton(ft.icons.SHOW_CHART, icon_size=28),
                ft.IconButton(ft.icons.SETTINGS, icon_size=28),
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
            bgcolor=ft.colors.SURFACE_VARIANT,
            padding=10,
        )
        
        self.page.clean()
        self.page.add(
            ft.Column([
                header,
                ft.Container(
                    content=ft.ListView([stats], expand=True),
                    expand=True,
                    padding=10,
                ),
                nav_bar
            ], expand=True)
        )
    
    def create_stat_card_with_button(self, title, value_text, goal, on_click, button_text):
        """Cria card com botão de ação"""
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Column([
                        ft.Text(title, size=16, weight="bold"),
                        value_text,
                        ft.Text(goal, size=12, color=ft.colors.GREY_400)
                    ], spacing=5),
                    ft.ElevatedButton(
                        button_text,
                        on_click=on_click,
                        style=ft.ButtonStyle(
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.TEAL_400,
                        )
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            ], spacing=5),
            padding=15,
            bgcolor=ft.colors.SURFACE_VARIANT,
            border_radius=10,
        )

def main(page: ft.Page):
    app = VitalFlow(page)

if __name__ == "__main__":
    ft.app(main)
