import tkinter as tk
from tkinter.font import Font
from random import randrange


class UploadWindow(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.controller = controller
        self.font = Font(family="Ubuntu", size=12)

        self.rowconfigure(1, weight=1)

        # Upper widgets
        self.upload_btn = tk.Button(self, text='Upload your file', relief=tk.SOLID, bd=2,
                                    command=self.pass_results,
                                    bg=self.controller.shared_data['bg'])

        self.upload_lbl = tk.Label(self, text='You can upload 4 files per minute, due to limitation of basic API',
                                   bg=self.controller.shared_data['bg'])

        # Api widgets
        self.api_frame = tk.Frame(self, bg=self.controller.shared_data['bg'])
        self.api_frame.columnconfigure(1, weight=1)
        self.api_lbl = tk.Label(self.api_frame, text='API key', bg=self.controller.shared_data['bg'], font=self.font,
                                padx=30)
        self.api_key = tk.Entry(self.api_frame, text='Insert your api key', bg=self.controller.shared_data['bg'],
                                font=self.font)
        self.api_key.insert(tk.END, 'Please enter your API key')
        self.api_key.bind("<Button-1>", self.api_clear)
        self.api_key.bind("<Leave>", self.api_fill)

        # Placing top level widgets on grid
        self.upload_btn.grid(row=0, sticky=tk.S)
        self.upload_lbl.grid(row=1, sticky=tk.N)

        # Placing API widgets on bottom of grid
        self.api_lbl.grid(row=0)
        self.api_key.grid(row=0, column=1, sticky=tk.EW)
        self.api_frame.grid(row=2, sticky=tk.EW)

    def api_clear(self, event):
        """Clearing widget responsible for entering the api key, when user clicks on it, and its still original text"""
        if self.api_key.get() == 'Please enter your API key':
            self.api_key.delete(0, tk.END)

    def api_fill(self, event):
        """When user leave empty key it goes back to original text"""
        if self.api_key.get() == '':
            self.api_key.insert(0, 'Please enter your API key')
        else:
            self.controller.shared_data["api_key"].set(self.api_key.get())

    def pass_results(self):
        """Passing result of the scan to report window, after clicking upload button, and changing actual frame for
        it """
        random = range(randrange(0, 5))
        report = [num for num in random]
        self.controller.get_page('ReportWindow').fill_details(report)
        self.controller.show_frame('ReportWindow')
