import mods.filemanager as filemanager
import mods.git as git
import mods.gui as gui

def main():
    print("hello")
    filemanager.write_file("test.txt", "test")
    guiAPI = gui.renderGui()
    print(guiAPI)
    guiAPI["addWidget"](gui.addGame("test", lambda: print("test")))
    guiAPI["execute"]()
    
if __name__ == "__main__":
    main()