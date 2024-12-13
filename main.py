from gui import *

def main() -> None:
    """
    Shows main window
    """
    window_remote = Tk()
    window_remote.title("Remote")
    window_remote.geometry('210x400+590+450')
    window_remote.resizable(False, False)
    Gui(window_remote)
    window_remote.mainloop()

if __name__=="__main__":
    main()