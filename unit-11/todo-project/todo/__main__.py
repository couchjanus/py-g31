"""Todo entry point script"""

from todo import view, __app_name__

def main():
    view.app(prog_name=__app_name__)

if __name__ == "__main__":
    # print(dir(view))
    main()
    
