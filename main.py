import customtkinter as ctk
from screens.tables_screen import TablesScreen
from screens.main_screen import MainScreen
from screens.order_screen import OrderScreen

class PDASystem(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.frames = {}

        # Window Setup
        self.title("PDA System")
        self.geometry("400x600") # Tall aspect ratio for PDA/Phone style
        
        # macOS specific: Set appearance
        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("blue")

        # Container to hold all screens
        self.container = ctk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        # Initialize the MainScreen
        frame = MainScreen(parent=self.container, controller=self)
        self.frames["MainScreen"] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainScreen")
        
        self.frames = {}
        for F in (MainScreen, TablesScreen): # Add more screens to this tuple as you make them
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainScreen")

        
        

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = PDASystem()
    app.mainloop()