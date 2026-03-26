import customtkinter as ctk
from screens.main_screen import MainScreen
# 1. IMPORT your other screens here
from screens.tables_screen import TablesScreen
from screens.food_menu import FoodMenuScreen


class PDASystem(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("PDA System")
        self.geometry("400x600")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Container to hold all screens
        self.container = ctk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # 2. INITIALIZE ALL SCREENS
        # We loop through the classes to save space and avoid repeating code
        for F in (MainScreen, TablesScreen, FoodMenuScreen):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start with the Main Screen
        self.show_frame("MainScreen")

    def show_frame(self, page_name):
        # Now "TablesScreen" and "FoodMenuScreen" exist in this dictionary!
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = PDASystem()
    app.mainloop()