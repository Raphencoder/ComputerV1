import sys

def take_arg():
    """
    First fonction called
    """
    index = len(sys.argv)
    if index != 2:
        raise OSError("Need one argument")
    if isinstance(sys.argv[1], str):
        return sys.argv[1]
    else:
        raise SyntaxError()


def clean_equation(equation):
    


def main():
    equation = take_arg()
    clean_equation(equation)   

if __name__ == "__main__":
    main()