import tkinter as tk


class ReportWindow(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.controller = controller
        self.parent = parent

        # Define space for each frame
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)

        # Creating widgets for next decision after scan
        self.result_frame = tk.Frame(self, bd=2, bg=self.controller.shared_data['bg'], relief=tk.SOLID)
        self.result_frame.columnconfigure(0, weight=1)
        self.result_frame.columnconfigure(1, weight=1)
        self.result_frame.rowconfigure(0, weight=1)
        self.result_frame.rowconfigure(1, weight=1)
        self.report_lbl = tk.Label(self.result_frame,
                                   text="",
                                   bg=self.controller.shared_data['bg'])
        self.scan_next_btn = tk.Button(self.result_frame, text='Scan next file', relief=tk.SOLID, borderwidth=2,
                                       command=lambda: controller.show_frame('UploadWindow'),
                                       bg=self.controller.shared_data['bg'])
        self.delete_file_btn = tk.Button(self.result_frame, text='Delete and scan next file', relief=tk.SOLID, bd=2,
                                         command=lambda: controller.show_frame('UploadWindow'),
                                         bg=self.controller.shared_data['bg'])

        # Creating widgets for detailed result section
        self.details_frame = tk.Frame(self, bd=2, bg=self.controller.shared_data['bg'], relief=tk.SOLID)
        self.details_frame.columnconfigure(0, weight=1)
        self.report_details_lbl = tk.Label(self.details_frame, text='Details', bg=self.controller.shared_data['bg'],
                                           relief=tk.FLAT)

        # Placing widgets for next decision after scan on grid
        self.result_frame.grid(row=0, sticky=tk.NSEW)
        self.report_lbl.grid(row=0, columnspan=2, sticky=tk.S)
        self.scan_next_btn.grid(row=1, column=0, sticky=tk.N)
        self.delete_file_btn.grid(row=1, column=1, sticky=tk.N)

        # Placing widgets for detailed result section on grid
        self.details_frame.grid(row=0, sticky=tk.NSEW, column=1)
        self.report_details_lbl.grid(sticky=tk.N, pady=(10, 0))

    def fill_details(self, scan_result):
        """Showing scan result on grid"""
        self.controller.shared_data['antivirus_counter'] = len(scan_result)
        # Clearing grid from previous scans
        for i in range(self.details_frame.grid_size()[1] - 1):
            self.details_frame.grid_slaves(i + 1, 0)[0]['text'] = ''

        # Filling cleaned grid with new scans
        for i, scan in enumerate(scan_result):
            if scan_result[scan]['detected']:
                self.controller.shared_data['detected_counter'] += 1
            scan_txt = f"{i + 1}. {scan} - detected: {scan_result[scan]['detected']}"
            detail = tk.Label(self.details_frame, text=scan_txt, bg=self.controller.shared_data['bg'], relief=tk.FLAT)
            detail.grid(row=i + 1, sticky=tk.W)

        self.report_lbl['text'] = f"Detected by {self.controller.shared_data['detected_counter']}/{self.controller.shared_data['antivirus_counter']}\n What do you want to do with this file?"

