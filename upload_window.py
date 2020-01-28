import tkinter as tk
from tkinter.font import Font


class UploadWindow(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.controller = controller
        self.font = Font(family="Ubuntu", size=12)

        self.rowconfigure(1, weight=1)

        # Upper widgets
        self.upload_btn = tk.Button(self, text='Upload your file', relief=tk.SOLID, bd=2,
                                    command=lambda: controller.show_frame('ReportWindow'), bg=self.controller.bg)

        self.upload_lbl = tk.Label(self, text='You can upload 4 files per minute, due to limitation of basic API',
                                   bg=self.controller.bg)

        # Api widgets
        self.api_frame = tk.Frame(self, bg=self.controller.bg)
        self.api_frame.columnconfigure(1, weight=1)
        self.api_lbl = tk.Label(self.api_frame, text='API key', bg=self.controller.bg, font=self.font, padx=30)
        self.api_key = tk.Entry(self.api_frame, text='Insert your api key', bg=self.controller.bg, font=self.font)
        self.api_key.insert(tk.END, 'Please enter your API key')

        # Placing top level widgets on grid
        self.upload_btn.grid(row=0, sticky=tk.S)
        self.upload_lbl.grid(row=1, sticky=tk.N)

        # Placing API widgets on bottom of grid
        self.api_lbl.grid(row=0)
        self.api_key.grid(row=0, column=1, sticky=tk.EW)
        self.api_frame.grid(row=2, sticky=tk.EW)
