from tkinter import *
from ventana import *



def main():
    root = Tk()
    root.wm_title("Registro de farmacia")
    app = ventana(root)
    app.mainloop()


if __name__ == "__main__":
    main()