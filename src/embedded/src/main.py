import sys
# from machine import freq
# freq(160000000)

sys.path.append('Script')  # Add the path to the script folder

if __name__ == '__main__':
    import modules.controller as Controller

    Controller.main()
