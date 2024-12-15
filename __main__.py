import mods.filemanager as filemanager
import mods.git as git


def main():
    print("hello")
    filemanager.write_file("test.txt", "test")
    
if __name__ == "__main__":
    main()