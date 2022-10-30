# global scope
# Note 1: a global variable that's accessiable from "fn1" function and
# "fn2" function
my_global = 10


def fn1():
    # Note 2: "enclosed_v" variable that's local to "fn1" function and is accessiable
    # from the "fn2" function
    enclosed_v = 8

    def fn2():
        # Note 3: "local_v" variable that's local to the "fn2" function but "local_v"
        # is not accessiable from the "fn1" function
        local_v = 5
        print('Access to Global', my_global)
        print('Access to enclosed', enclosed_v)
    # print(local_v) # Note 4: you cannot access "local_v" variable from within "fn1"
    # function because the way scoping works is the inner most function "fn2" has access
    # to almost everything from the outside, but not the other way around.
    # In other words, the outter functions such as "fn1" do not have access to inner
    # functions like "fn2" unless you use special keywords and other mmethods that
    # will break these rules.
    fn2()


fn1()
