def bad():
    # 'Oh no,' ... is accessible as IndexError.args when caught
    raise IndexError('Oh no, out of index!')

if __name__ == "__main__":
    try:
        bad()
    except IndexError as err:
        print(err.args)
        print("Heck, let's do something else then.")
        # "raise" so the error still comes out
        raise
    finally:
        # use this block if extra code is needed to return to a consistent
        # state, e.g. by cleaning up files
        pass

