import tkinter as tk
import upload_window as uw
import report_window as rw


class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Variable for changing background for whole App
        self.shared_data = {
            "bg": "white",
            "url": "https://www.virustotal.com/vtapi/v2/file",
            "api_key": tk.StringVar()
        }

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}
        for F in (uw.UploadWindow, rw.ReportWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self, bg=self.shared_data["bg"])
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky=tk.NSEW)
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure(0, weight=1)

        self.show_frame("UploadWindow")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Virus scanner')
    root.geometry("600x400")
    Main(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()
