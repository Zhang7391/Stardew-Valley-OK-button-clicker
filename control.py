import os
import psutil
import tkinter as tk


def is_process_running(exe_path):
    # getting all processes
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            # compare process's path
            if proc.info['exe'] and os.path.samefile(proc.info['exe'], exe_path):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def button_switch(titlebar, buttons):
    if(titlebar["fg"] == "red"):
        titlebar.config(fg="green")
    else:
        titlebar.config(fg="red")
    
    for button in buttons:
        if button["state"] == "normal":
            button.config(state="disabled")
        else:
            button.config(state="normal")

class GUI():
    _root = tk.Tk()
    
    def __init__(self):
        self._root.title("Stardew Valley Tool v0.0.7")
        self._root.geometry("320x480")

        # properties
        btn_conf = dict(width=12, height=2, relief="solid", font=("Arial", 12))
        label_conf = dict(font=("Arial", 18, "bold"), fg="red")

        # group 1
        label1 = tk.Label(self._root, text="aaa", **label_conf)
        label1.grid(row=0, column=0, columnspan=2, pady=(8, 5), sticky="n")

        buttonSet_1 = (tk.Button(self._root, text=u"\u958b\u555f",command=lambda: button_switch(label1, buttonSet_1), **btn_conf), tk.Button(self._root, text=u"\u95dc\u9589", command=lambda: button_switch(label1, buttonSet_1), state="disabled", **btn_conf))

        buttonSet_1[0].grid(row=1, column=0, padx=(0, 5), pady=5, sticky="e")  # right
        buttonSet_1[1].grid(row=1, column=1, padx=(5, 0), pady=5, sticky="w")  # left

        buttonSet_1 = tuple(buttonSet_1)

        # group 2
        label2 = tk.Label(self._root, text="aaa", **label_conf)
        label2.grid(row=2, column=0, columnspan=2, pady=(8, 5), sticky="n")

        buttonSet_2 = (tk.Button(self._root, text=u"\u958b\u555f",command=lambda: button_switch(label2, buttonSet_2), **btn_conf), tk.Button(self._root, text=u"\u95dc\u9589", command=lambda: button_switch(label2, buttonSet_2), state="disabled", **btn_conf))

        buttonSet_2[0].grid(row=3, column=0, padx=(0, 5), pady=5, sticky="e")
        buttonSet_2[1].grid(row=3, column=1, padx=(5, 0), pady=5, sticky="w")

        # group 3
        label3 = tk.Label(self._root, text="aaa", **label_conf)
        label3.grid(row=4, column=0, columnspan=2, pady=(8, 5), sticky="n")

        buttonSet_3 = (tk.Button(self._root, text=u"\u958b\u555f",command=lambda: button_switch(label3, buttonSet_3), **btn_conf), tk.Button(self._root, text=u"\u95dc\u9589", command=lambda: button_switch(label3, buttonSet_3), state="disabled", **btn_conf))

        buttonSet_3[0].grid(row=5, column=0, padx=(0, 5), pady=5, sticky="e")
        buttonSet_3[1].grid(row=5, column=1, padx=(5, 0), pady=5, sticky="w")

        # space
        self._root.grid_rowconfigure(6, minsize=80)

        # two buttons at the bottom
        bottom_btn1 = tk.Button(self._root, text=u"\u4e00\u9375\u958b\u555f", **btn_conf)
        bottom_btn1.grid(row=7, column=0, padx=(0, 5), pady=(10, 20), sticky="e")

        bottom_btn2 = tk.Button(self._root, text=u"\u4e00\u9375\u95dc\u9589", **btn_conf)
        bottom_btn2.grid(row=7, column=1, padx=(5, 0), pady=(10, 20), sticky="w")

        # center horizontally
        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_columnconfigure(1, weight=1)

        self._root.mainloop()
    
    def run(self):
        pass

if __name__ == "__main__":
    gui = GUI()
    
    gui.run()