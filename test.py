try:
    x = int("xasd")
except (ZeroDivisionError, ValueError) as err:
    print(err)