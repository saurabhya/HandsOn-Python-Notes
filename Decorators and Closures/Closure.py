"""
    In the blogosphere, closures are sometimes confused with anonymous functions. the reason why many confuse them is
    historic: defining functions inside functions is not so common, until you start using anonumous functions.
    And closures only matter when you have nested functions. So alot of people learn both concepts at the same time.

    Actually a closure is a function with an extended scope that encompasses nonglobal variables referenced in the
    body of the function but not defined there. It does not matter whether the function is anonymous or not; what matter
    is that it can access nonglboal variables that are defined outside of its body.
    This is a challenging concept to grasp, ad is better approached through an example.

    Comsider an avg function to compute the mean of an ever-increasing series of values; for example,
    the average closing price of a commodity over its entire history. Every day a new price is added and
    the average is recomputed taking into account all prices so far.
"""
# A class to calculate a running average
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

avg1 = Averager()
print(avg1(10))
print(avg1(11))
print(avg1(12))

# A higher-order function to calculate a running average
def make_average():
    series = []

    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return average

print("\n using higher-order function to calculate the running average\n")
avg2 = make_average()
print(avg2(10))
print(avg2(11))
print(avg2(12))

"""
    it's obvious where the avg of the Averager calss keeps the history: the self.series instance attribute.
    But where does the avg function in the second example find the series?

    Note that series is a local varaiable of make_averager because the intialixation series = []
    happens in the body of that function. But when avg2(10) is called, make_average has already returned, and its scope is long gone.
    Within average, series is a free variable. this is a technical term meaning a variable that is not bound in the local scope.


    Inspecting the returned averager object shows how Python keeps the names of local and free variables in the
    __code__ aattribute that represents the compiled body of the function.
"""
print(avg2.__code__.co_varnames)
print(avg2.__code__.co_freevars)
"""
    The binding for series is kept the __closure__ atrribute of the returned function avg2. Each time in avg2.__closure__
    corresponds to a name in ag2.__code.co_vars. These items are cells, and they have an attribute called cell_contents where the
    actual value can be found.
"""
print(avg2.__closure__)
print(avg2.__closure__[0].cell_contents)

"""
    to summarize: a closure is a function that retains the bindings of free variable that exist when the function is defined,
    so that they can be used later when the function is invoked and the defining scope is no longer available.

    Note that the only situation in which a function may need to deal with ecternal variables that are nonglobal is
    when it is nested in another function.
"""