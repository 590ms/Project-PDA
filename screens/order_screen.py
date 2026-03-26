import customtkinter as ctk

class OrderScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = ctk.CTkLabel(self, text="--- ORDER MENU ---", font=("Arial", 20))
        label.pack(pady=20)
        
        # Back Button
        btn_back = ctk.CTkButton(self, text="Back to Main", 
                                 command=lambda: controller.show_frame("MainScreen"))
        btn_back.pack(pady=10)