import customtkinter as ctk

class TablesScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title at the top
        self.label = ctk.CTkLabel(self, text="STORE FLOOR PLAN", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        # The "Floor" area (a sub-frame where we place tables)
        self.floor_area = ctk.CTkFrame(self, fg_color="transparent")
        self.floor_area.pack(fill="both", expand=True, padx=20, pady=20)

        # --- MANUAL DESIGN AREA ---
        # Syntax: self.create_table(number, x_pos, y_pos, width, height)
        
        # Round tables near the entrance
        self.create_table("1", x=40, y=50, w=60, h=60, corner=30)
        self.create_table("2", x=40, y=150, w=60, h=60, corner=30)

        # Large rectangular booths against the wall
        self.create_table("B1", x=200, y=50, w=120, h=50)
        self.create_table("B2", x=200, y=120, w=120, h=50)
        self.create_table("B3", x=200, y=190, w=120, h=50)

        # Large center party table
        self.create_table("VIP", x=80, y=300, w=200, h=80)

        # Back Button to return to Main
        self.btn_back = ctk.CTkButton(self, text="← Back", width=100,
                                      command=lambda: controller.show_frame("MainScreen"))
        self.btn_back.place(x=10, y=10)

    def create_table(self, label, x, y, w, h, corner=6):
        """Helper to spawn a table button at a specific spot"""
        btn = ctk.CTkButton(self.floor_area, 
                            text=f"T-{label}", 
                            width=w, 
                            height=h, 
                            corner_radius=corner,
                            command=lambda: self.table_clicked(label))
        btn.place(x=x, y=y)

    def table_clicked(self, table_id):
        print(f"Table {table_id} selected. Opening order info...")
        # Here you would call your backend.py to check if table is occupied