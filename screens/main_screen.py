import customtkinter as ctk
import sys

class MainScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Configure grid layout for the frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Title Label
        self.label = ctk.CTkLabel(self, text="PDA POS SYSTEM", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # 1. Tables Button
        self.btn_tables = ctk.CTkButton(self, text="Available Tables", 
                                        command=self.show_tables,
                                        height=60, font=ctk.CTkFont(size=16))
        self.btn_tables.grid(row=1, column=0, padx=40, pady=10, sticky="ew")

        # 2. Order Button (Primary Action)
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

        # Tables Button -> Goes to Table Floor Plan
        self.btn_tables = ctk.CTkButton(self, text="Available Tables", 
                                    command=self.show_tables_layout)
    
        # Order Button -> Goes to the Menu/Order Screen
        self.btn_order = ctk.CTkButton(self, text="Create New Order", 
                                   command=self.show_order_menu)

    def show_tables(self):
        print("Navigating to Tables...")
        self.controller.show_frame("TablesScreen")
        # self.controller.show_frame("TablesScreen")
    
    def show_tables_layout(self):
        # This must match the name of the Table class in main.py
        self.controller.show_frame("TablesScreen")

    def show_order_menu(self):
        # This must match the name of your Order/Menu class
        self.controller.show_frame("OrderScreen")

    def create_order(self):
        self.controller.show_frame("FoodMenuScreen")

    def exit_application(self):
        # Clean exit for macOS
        self.controller.quit()
        sys.exit()