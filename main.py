import flet as ft
from datetime import datetime
import json
import os

class VitalFlow:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "VitalFlow"
        self.page.window_width = 400
        self.page.window_height = 800
        self.page.theme_mode = "dark"
        
        # Data storage file
        self.data_file = "vitalflow_data.json"
        self.data = self.load_data()
        
        # Setup theme
        self.setup_theme()
        
        # Create UI
        self.create_ui()
        
    def setup_theme(self):
        """Setup app theme colors"""
        self.page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=ft.colors.TEAL_400,
                secondary=ft.colors.CYAN_400,
            )
        )
        
    def load_data(self):
        """Load data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return self.get_empty_data()
        return self.get_empty_data()
    
    def get_empty_data(self):
        """Return empty data structure"""
        today = datetime.now().strftime("%Y-%m-%d")
        return {
            today: {
                "water": 0,
                "steps": 0,
                "calories": 0,
                "sleep": 0,
                "exercises": []
            }
        }
    
    def save_data(self):
        """Save data to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_today_data(self):
        """Get today's data"""
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
    
    def create_ui(self):
        """Create the main UI"""
        self.page.clean()
        
        # Header
        header = ft.Container(
            content=ft.Column([
                ft.Text("VitalFlow", size=32, weight="bold", color=ft.colors.TEAL_400),
                ft.Text(datetime.now().strftime("%d de %B, %Y"), size=14, color=ft.colors.GREY_400)
            ]),
            padding=20,
            bgcolor=ft.colors.SURFACE_VARIANT,
        )
        
        # Stats cards
        stats_column = ft.Column([
            self.create_stat_card("💧 Água", "0 L", "Meta: 2L"),
            self.create_stat_card("🚶 Passos", "0", "Meta: 10.000"),
            self.create_stat_card("🔥 Calorias", "0 kcal", "Meta: 2.000"),
            self.create_stat_card("😴 Sono", "0h", "Meta: 8h"),
        ])
        
        # Input section
        input_section = ft.Container(
            content=ft.Column([
                ft.Text("Registrar Atividades", size=20, weight="bold"),
                ft.Divider(),
                
                # Water input
                ft.Row([
                    ft.TextField(label="Água (L)", width=200),
                    ft.IconButton(ft.icons.ADD_CIRCLE, icon_size=30, icon_color=ft.colors.TEAL_400)
                ]),
                
                # Steps input
                ft.Row([
                    ft.TextField(label="Passos", width=200),
                    ft.IconButton(ft.icons.ADD_CIRCLE, icon_size=30, icon_color=ft.colors.TEAL_400)
                ]),
                
                # Calories input
                ft.Row([
                    ft.TextField(label="Calorias (kcal)", width=200),
                    ft.IconButton(ft.icons.ADD_CIRCLE, icon_size=30, icon_color=ft.colors.TEAL_400)
                ]),
                
                # Sleep input
                ft.Row([
                    ft.TextField(label="Sono (horas)", width=200),
                    ft.IconButton(ft.icons.ADD_CIRCLE, icon_size=30, icon_color=ft.colors.TEAL_400)
                ]),
                
                ft.Divider(),
                ft.ElevatedButton(
                    "Salvar Dados",
                    width=300,
                    height=50,
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.TEAL_400,
                    )
                )
            ]),
            padding=20,
        )
        
        # Navigation
        navigation = ft.Row([
            ft.IconButton(ft.icons.HOME, selected=True, icon_color=ft.colors.TEAL_400),
            ft.IconButton(ft.icons.SHOW_CHART),
            ft.IconButton(ft.icons.SETTINGS),
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
        
        # Main layout
        self.page.add(
            ft.Column([
                header,
                ft.Divider(height=1),
                ft.ListView([
                    stats_column,
                    input_section,
                ], expand=True),
                ft.Divider(height=1),
                navigation
            ], expand=True)
        )
    
    def create_stat_card(self, title, value, goal):
        """Create a statistics card"""
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=16, weight="bold"),
                ft.Text(value, size=24, weight="bold", color=ft.colors.TEAL_400),
                ft.Text(goal, size=12, color=ft.colors.GREY_400)
            ], spacing=5),
            padding=15,
            margin=10,
            bgcolor=ft.colors.SURFACE_VARIANT,
            border_radius=10,
        )

def main(page: ft.Page):
    app = VitalFlow(page)

ft.app(main)
