"""Todo entry point script"""
# from todo import __app_name__, view

# def main():
#     # print(__app_name__)
#     view.app(prog_name=__app_name__)

# if __name__ == "__main__":
#     main()

from todo import view, __app_name__

def main():
    view.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()
