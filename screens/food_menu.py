import customtkinter as ctk


# ── Menu Data ────────────────────────────────────────────────────────────────
MENU = {
    "☕ Espresso": [
        {"name": "Espresso",          "price": 1.80},
        {"name": "Double Espresso",   "price": 2.50},
        {"name": "Freddo Espresso",   "price": 2.20},
        {"name": "Ristretto",         "price": 1.80},
        {"name": "Lungo",             "price": 2.00},
    ],
    "🥛 Milk Coffees": [
        {"name": "Cappuccino",        "price": 3.00},
        {"name": "Latte",             "price": 3.20},
        {"name": "Flat White",        "price": 3.00},
        {"name": "Macchiato",         "price": 2.50},
        {"name": "Cortado",           "price": 2.80},
    ],
    "🧊 Cold Coffees": [
        {"name": "Freddo Cappuccino", "price": 2.80},
        {"name": "Iced Latte",        "price": 3.50},
        {"name": "Cold Brew",         "price": 3.80},
        {"name": "Frappe",            "price": 3.50},
    ],
    "🍵 Other Drinks": [
        {"name": "Hot Chocolate",     "price": 3.20},
        {"name": "Green Tea",         "price": 2.50},
        {"name": "Chamomile Tea",     "price": 2.20},
        {"name": "Fresh Orange Juice","price": 3.80},
    ],
}


class FoodMenuScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # ── State ──────────────────────────────────────────────────────────
        self.order_items = []          # list of dicts: {name, price, qty}
        self.active_category = list(MENU.keys())[0]

        # ── Layout: 3 rows ─────────────────────────────────────────────────
        self.grid_rowconfigure(0, weight=0)   # header
        self.grid_rowconfigure(1, weight=1)   # body (categories + items)
        self.grid_rowconfigure(2, weight=0)   # order summary + actions
        self.grid_columnconfigure(0, weight=1)

        self._build_header()
        self._build_body()
        self._build_footer()

    # ── Header ─────────────────────────────────────────────────────────────
    def _build_header(self):
        hdr = ctk.CTkFrame(self, corner_radius=0, fg_color="#1a1a2e")
        hdr.grid(row=0, column=0, sticky="ew")
        hdr.grid_columnconfigure(1, weight=1)

        back_btn = ctk.CTkButton(
            hdr, text="← Back", width=70, height=34,
            font=ctk.CTkFont(size=13),
            fg_color="#2c2c54", hover_color="#3d3d6b",
            command=self._go_back,
        )
        back_btn.grid(row=0, column=0, padx=(10, 4), pady=10)

        title = ctk.CTkLabel(
            hdr, text="Menu",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#e0e0ff",
        )
        title.grid(row=0, column=1, pady=10)

        ctk.CTkLabel(hdr, text="", width=74).grid(row=0, column=2)

    # ── Body: categories (left strip) + item list (right) ─────────────────
    def _build_body(self):
        body = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        body.grid(row=1, column=0, sticky="nsew")
        body.grid_rowconfigure(0, weight=1)
        body.grid_columnconfigure(0, weight=0)
        body.grid_columnconfigure(1, weight=1)

        # ── Category strip ──────────────────────────────────────────────
        self.cat_frame = ctk.CTkFrame(body, width=105, corner_radius=0, fg_color="#16213e")
        self.cat_frame.grid(row=0, column=0, sticky="nsew")
        self.cat_frame.grid_propagate(False)

        self.cat_buttons = {}
        for cat in MENU:
            btn = ctk.CTkButton(
                self.cat_frame,
                text=cat,
                width=105,
                height=60,
                corner_radius=0,
                font=ctk.CTkFont(size=11, weight="bold"),
                anchor="center",
                text_color="#b0b0d0",
                fg_color="#16213e",
                hover_color="#1f2f5a",
                command=lambda c=cat: self._select_category(c),
            )
            btn.pack(fill="x", pady=(0, 1))
            self.cat_buttons[cat] = btn

        # ── Item list ────────────────────────────────────────────────────
        self.item_frame = ctk.CTkScrollableFrame(
            body, corner_radius=0, fg_color="#0f0f23",
            scrollbar_button_color="#2c2c54",
            scrollbar_button_hover_color="#3d3d6b",
        )
        self.item_frame.grid(row=0, column=1, sticky="nsew", padx=0)
        self.item_frame.grid_columnconfigure(0, weight=1)

        self._select_category(self.active_category)

    def _select_category(self, category):
        self.active_category = category

        for cat, btn in self.cat_buttons.items():
            if cat == category:
                btn.configure(fg_color="#0f3460", text_color="#ffffff")
            else:
                btn.configure(fg_color="#16213e", text_color="#b0b0d0")

        for widget in self.item_frame.winfo_children():
            widget.destroy()

        for item in MENU[category]:
            self._build_item_row(item)

    def _build_item_row(self, item):
        row = ctk.CTkFrame(
            self.item_frame,
            corner_radius=10,
            fg_color="#1a1a35",
            border_width=1,
            border_color="#2a2a50",
        )
        row.pack(fill="x", padx=8, pady=4)
        row.grid_columnconfigure(0, weight=1)

        info = ctk.CTkFrame(row, fg_color="transparent")
        info.grid(row=0, column=0, sticky="ew", padx=10, pady=(8, 4))
        info.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            info, text=item["name"],
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#dcdcff", anchor="w",
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(
            info, text=f"EUR {item['price']:.2f}",
            font=ctk.CTkFont(size=13),
            text_color="#7eb8f7", anchor="w",
        ).grid(row=1, column=0, sticky="w")

        controls = ctk.CTkFrame(row, fg_color="transparent")
        controls.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 8))

        qty_var = ctk.StringVar(value="1")

        ctk.CTkButton(
            controls, text="-", width=30, height=28,
            font=ctk.CTkFont(size=16),
            fg_color="#2c2c54", hover_color="#3d3d6b",
            command=lambda v=qty_var: self._change_qty(v, -1),
        ).pack(side="left")

        ctk.CTkLabel(
            controls, textvariable=qty_var,
            width=34, font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#ffffff",
        ).pack(side="left")

        ctk.CTkButton(
            controls, text="+", width=30, height=28,
            font=ctk.CTkFont(size=16),
            fg_color="#2c2c54", hover_color="#3d3d6b",
            command=lambda v=qty_var: self._change_qty(v, +1),
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            controls, text="Add to Order", height=28,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#2ecc71", hover_color="#27ae60",
            text_color="#000000",
            command=lambda i=item, v=qty_var: self._add_to_order(i, v),
        ).pack(side="left", fill="x", expand=True)

    @staticmethod
    def _change_qty(var, delta):
        current = int(var.get())
        var.set(str(max(1, current + delta)))

    # ── Footer ─────────────────────────────────────────────────────────────
    def _build_footer(self):
        self.footer = ctk.CTkFrame(
            self, corner_radius=0, fg_color="#1a1a2e",
            border_width=1, border_color="#2a2a50",
        )
        self.footer.grid(row=2, column=0, sticky="ew")
        self.footer.grid_columnconfigure(0, weight=1)

        self.summary_label = ctk.CTkLabel(
            self.footer,
            text="No items yet",
            font=ctk.CTkFont(size=12),
            text_color="#a0a0c0",
            anchor="w",
            wraplength=260,
        )
        self.summary_label.grid(row=0, column=0, padx=12, pady=(8, 2), sticky="ew")

        self.total_label = ctk.CTkLabel(
            self.footer,
            text="Total: EUR 0.00",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#2ecc71",
            anchor="w",
        )
        self.total_label.grid(row=1, column=0, padx=12, pady=(0, 4), sticky="ew")

        actions = ctk.CTkFrame(self.footer, fg_color="transparent")
        actions.grid(row=2, column=0, sticky="ew", padx=10, pady=(2, 10))
        actions.grid_columnconfigure(0, weight=1)
        actions.grid_columnconfigure(1, weight=1)

        ctk.CTkButton(
            actions, text="Clear",
            height=38, font=ctk.CTkFont(size=13),
            fg_color="#4a4a4a", hover_color="#5a5a5a",
            command=self._clear_order,
        ).grid(row=0, column=0, padx=(0, 4), sticky="ew")

        # ── TABLE INTEGRATION HOOK ─────────────────────────────────────
        # Your friend's TablesScreen should:
        #   1. Call  food_menu_screen.get_order()  to read the order list
        #   2. Let the user pick a table number
        #   3. Call  food_menu_screen.submit_to_table(table_no)  to finalise
        self.send_btn = ctk.CTkButton(
            actions, text="Send to Table ->",
            height=38, font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#0f3460", hover_color="#1a4a80",
            command=self._on_send_to_table,
        )
        self.send_btn.grid(row=0, column=1, padx=(4, 0), sticky="ew")

    # ── Order Logic ────────────────────────────────────────────────────────
    def _add_to_order(self, item, qty_var):
        qty = int(qty_var.get())
        for existing in self.order_items:
            if existing["name"] == item["name"]:
                existing["qty"] += qty
                self._refresh_summary()
                qty_var.set("1")
                return
        self.order_items.append({"name": item["name"], "price": item["price"], "qty": qty})
        self._refresh_summary()
        qty_var.set("1")

    def _clear_order(self):
        self.order_items.clear()
        self._refresh_summary()

    def _refresh_summary(self):
        if not self.order_items:
            self.summary_label.configure(text="No items yet")
            self.total_label.configure(text="Total: EUR 0.00")
            return
        lines = [f"{o['qty']}x {o['name']}" for o in self.order_items]
        self.summary_label.configure(text=",  ".join(lines))
        total = sum(o["price"] * o["qty"] for o in self.order_items)
        self.total_label.configure(text=f"Total: EUR {total:.2f}")

    # ── Table Integration API ──────────────────────────────────────────────
    def get_order(self):
        """Returns current order: [{'name': str, 'price': float, 'qty': int}, ...]"""
        return list(self.order_items)

    def submit_to_table(self, table_number: int):
        """
        Call this from TablesScreen after the user picks a table.
        Replace the print() with your actual table-saving logic.
        """
        if not self.order_items:
            return
        # TODO: save order to table_number in your database / state
        print(f"[ORDER] -> Table {table_number}")
        for o in self.order_items:
            print(f"  {o['qty']}x {o['name']}  @ EUR {o['price']:.2f}")
        print(f"  Total: EUR {sum(o['price']*o['qty'] for o in self.order_items):.2f}")
        self._clear_order()

    def _on_send_to_table(self):
        """
        Wire this to TablesScreen once it exists:
            self.controller.show_frame("TablesScreen")
        TablesScreen then calls get_order() / submit_to_table(n).
        """
        if not self.order_items:
            self._flash_label("Add items first!", "#e74c3c")
            return
        # self.controller.show_frame("TablesScreen")   # <- uncomment when ready
        self._flash_label("Tables coming soon!", "#f39c12")

    def _flash_label(self, msg, color):
        orig_text  = self.summary_label.cget("text")
        orig_color = self.summary_label.cget("text_color")
        self.summary_label.configure(text=msg, text_color=color)
        self.after(1800, lambda: self.summary_label.configure(
            text=orig_text, text_color=orig_color))

    def _go_back(self):
        self.controller.show_frame("MainScreen")
