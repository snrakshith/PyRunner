import itertools
# from itertools import *


def get_user_input():

    for i in itertools.count():
        try:
            yield i, input(' In [%d]:' % i)
        except KeyboardInterrupt:
            pass
        except EOFError:
            break


def exectution_function(user_input):
    try:
        compile(user_input, '<stdin>', 'eval')
    except SyntaxError:
        return exec
    return eval


def exec_user_input(i, user_input, user_globals):
    """
        if user_input is a Expression:
             Return eval
     else:
             Return exec
    """
    user_globals = user_globals.copy()
    try:
        return_value = exectution_function(user_input)(
            user_input, user_globals
        )
    except Exception as e:
        print("%s:%s" % (e.__class__.__name__, e))
    else:
        if return_value is not None:
            print("Op[%d]:%s" % (i, return_value))
    return user_globals


def selected_user_input(user_globals):

    return(
        (key, user_globals[key])
        for key in sorted(user_globals)
        if not key.startswith("__") or not key.endswith("__")
    )


def save_user_globals(user_globals, path='user_globals.txt'):

    with open(path, 'w') as f:
        # for key,val in user_globals.items():
        for key, val in selected_user_input(user_globals):
            f.write('%s=%s (%s)\n' % (
                key, val, val.__class__.__name__
            ))


def main():

    user_globals = {}
    save_user_globals(user_globals)
    for i, user_input in get_user_input():
        user_globals = exec_user_input(
            i, user_input, user_globals
        )
    save_user_globals(user_globals)


if __name__ == "__main__":
    main()
