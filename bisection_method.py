import math
def bisection_method(func, lower, upper, tolerence, max_iterations):

    if func(lower) * func(upper) > 0:
        print("Bisection method will fail.")
    else:
        mid = (lower + upper) / 2.0
        iterations = 0
        while (upper - lower) / 2.0 > tolerence and iterations <= max_iterations:
            current_iteration_print = "Iteration: {0},".format(iterations)
            if func(mid) == 0:
                return mid
            elif func(lower) * func(mid) < 0:
                upper = mid
            else:
                lower = mid
            mid = (lower + upper) / 2.0
            current_iteration_print += " Current root approximation: {0},".format(mid)
            print(current_iteration_print)
            iterations = iterations + 1
        print("Final approximation: {0}".format(mid))
        return mid

def q2(func, lower, upper, mikta):
    error = ((math.log((0.0001)/(upper-lower),10)) / (math.log(2,10))) * (-1)
    print("the error is:" , error)
    l = lower
    while l <= upper:
        if func(l) * func(l+mikta) < 0:
            bisection_method(func,l,l+mikta,0.0001,int(error+1))
        l = l + mikta


#def f1(x):
#    return x + 1

#def f2(x):
#    return x ** 3

def f3(x):
    return x ** 2 - 4

#bisection_method(f1, -2.6, -0.1, 0.000001, 30)
#bisection_method(f2, -0.4, 2, 0.0001, 30)
q2(f3,-5,5,0.1)