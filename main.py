# from Loc import Loc


def prRed(skk): print("\033[91m {}\033[00m".format(skk))


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


def prYellow(skk): print("\033[93m {}\033[00m".format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))


def prPurple(skk): print("\033[95m {}\033[00m".format(skk))


def prCyan(skk): print("\033[96m {}\033[00m".format(skk))


def prLightGray(skk): print("\033[97m {}\033[00m".format(skk))


def prBlack(skk): print("\033[98m {}\033[00m".format(skk))


if __name__ == "__main__":

    # breakpoint()
    #
    # print("hello world")

    import os, glob

    path = 'C:\Repos\logics0\solve_files'
    for filename in glob.glob(os.path.join(path, '*')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            temp = os.path.split(filename)
            print(temp[0])
            print(f.read())
