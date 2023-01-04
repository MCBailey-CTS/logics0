import os

from Constants import Constants

if __name__ == "__main__":
    for d in dir(Constants):
        if "__" in d:
            continue
        # if "difficult" not in d:
        #     continue

        temp = getattr(Constants, d)
        result = temp()
        print(result)




