# example: python argparse_example.py -s Hello -n 100 -b -l 1 10 2

import argparse

if __name__ == '__main__':
    # Initialize argparser
    parser = argparse.ArgumentParser(description="Put your description here")
    
    # Add arguments
    parser.add_argument("--string-arg", "-s", default=["Howdy"],
                        help="String argument.",
                        type=str, nargs=1)
    parser.add_argument("--number_arg","-n", default=[0],
                        help="Integer argument.",
                        type=int, nargs=1)
    parser.add_argument("--list_arg","-l", default=[1,2,3,4],
                        help="A list of ints",
                        type=int, nargs='+')  # use nargs='+' to require at least one value
    parser.add_argument("--bool_arg","-b", default=False,
                        help="Boolean argument.",
                        action="store_true")

    # Parse and access arguments
    # string and numbers are given as lists
    # bools are not
    args = parser.parse_args()
    # or use as:
    # args = parser.parse_args(['-s', 'test', '-n', '12', '-l', '3', '1', '4', '-b'])
    s = args.string_arg[0]
    l = args.list_arg
    n = args.number_arg[0]
    b = args.bool_arg
    
    print("Here you go!")
    print("s:", s)
    print("l:", l)
    print("n:", n)
    print("b:", b)
    print("All done!")
