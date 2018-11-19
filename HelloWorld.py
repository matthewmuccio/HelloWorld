#!/usr/bin/env python3


if __name__ == "__main__": print("".join([" {}".format(x) if x.isupper() and i > 0 else x for i, x in enumerate(__import__("os").path.basename(__file__)[:-3])]))
