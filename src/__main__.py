import sys

if __name__ == "__main__":
    # TODO: Use a `main()` function that returns an exit code
    exit_code = 0
    try:
        print("Hello, World!")
    except:
        exit_code = 1
    sys.exit(exit_code)
