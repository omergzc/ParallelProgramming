import inspect

custom_power = lambda x=0, /, e=1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """

    :param x: First base value. (Positional-only)
    :type x: int
    :param y: Second base value. (Positional-only)
    :type y: int
    :param a: Exponent value for 'x'. (Positional-or-keyword)
    :type a: int
    :param b: Exponent value for 'y'. (Positional-or-keyword)
    :type b: int
    :param c: Divisor value for the division operation. (Keyword-only)
    :type c: int
    :return: The floating-point result of the equation.
    :rtype: float
    """
    return float((x**a + y**b) / c)

def fn_w_counter() -> tuple:
    if not hasattr(fn_w_counter, "calls"):
        fn_w_counter.calls = 0
        fn_w_counter.caller_dict = {}

    fn_w_counter.calls += 1

    caller_frame = inspect.currentframe().f_back
    caller_name = caller_frame.f_globals.get('__name__', '<unknown>')

    if caller_name not in fn_w_counter.caller_dict:
        fn_w_counter.caller_dict[caller_name] = 0
    fn_w_counter.caller_dict[caller_name] += 1

    return (fn_w_counter.calls, fn_w_counter.caller_dict)    
