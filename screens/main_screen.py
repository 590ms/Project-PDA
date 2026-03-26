import customtkinter as ctk
import sys


class MainScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Title Label
        self.label = ctk.CTkLabel(self, text="PDA POS SYSTEM", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # 1. Tables Button - Links to TablesScreen
        self.btn_tables = ctk.CTkButton(self, text="Available Tables",
                                        command=self.show_tables_screen,  # Single clear command
                                        height=60, font=ctk.CTkFont(size=16))
        self.btn_tables.grid(row=1, column=0, padx=40, pady=10, sticky="ew")

        # 2. Order Button - Links to FoodMenuScreen
        self.btn_order = ctk.CTkButton(self, text="Create New Order",
                                       command=self.create_order,
                                       height=60, font=ctk.CTkFont(size=16),
                                       fg_color="#2ecc71", hover_color="#27ae60")
        self.btn_order.grid(row=2, column=0, padx=40, pady=10, sticky="ew")

        # 3. Exit Button
        self.btn_exit = ctk.CTkButton(self, text="Exit System",
                                      command=self.exit_application,
                                      height=60, font=ctk.CTkFont(size=16),
                                      fg_color="#e74c3c", hover_color="#c0392b")
        self.btn_exit.grid(row=3, column=0, padx=40, pady=20, sticky="ew")

    def show_tables_screen(self):
        print("Navigating to Tables...")
        # Ensure 'TablesScreen' is the exact class name in your main controller
        self.controller.show_frame("TablesScreen")

    def create_order(self):
        print("Navigating to Menu...")
        # Ensure 'FoodMenuScreen' is the exact class name in your main controller
        self.controller.show_frame("FoodMenuScreen")

    def exit_application(self):
        self.controller.quit()
        sys.exit()