def fun(**kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))


# Driver code
fun(s1='Geeks', s2='for', s3='Geeks')


def fun(arg1, **kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))
        print(arg1)


# Driver code
fun("Hi", s1='Geeks', s2='for', s3='Geeks')


def fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


fun(1, 2, 3, a=4, b=5)


def fun(*args):
    return sum(args)


print(fun(1, 2, 3, 4))
print(fun(5, 10, 15))


# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)
