import numpy as np
from scipy import optimize, stats

MIN_b = 0.0001  # Minimum hyperbolic decline exponent, b
MAX_b = 10.0  # Maximum hyperbolic decline exponent, b
MIN_di = -2.0  # Set lower limit for decline rate

class DeclineObj:
    """Find best fit (hyperbolic or exponential) to rate-time data
    ...
    (rest of the docstring remains the same)
    ...
    """
    def __init__(self, x, y, guess=None, model=None):
        """Initialize instance and check input"""
        self.x = x
        self.y = y
        self.offset = None
        self.x_best = None
        self.y_best = None
        self.used = None
        self.success = None
        self.parameters = None
        if guess is None:
            self.guess = [y.max(), 1.0, -0.5]
        else:
            # check the input for problems
            qi, b, di = guess
            if qi <= 0.0:
                raise ValueError("qi must be > 0")
            if b == 0.0:
                raise ValueError("Decline exponent, b, = 0, use exponential")
            if b < 0.0 or b > 5.0:
                raise ValueError("Decline exponent, b, out of range")
            if abs(di) > 1.0:
                di = di / 100.0
            if di < -1.0 or di > 1.0:
                raise ValueError("Decline rate, di, out of range")
            if di > 0:
                # assume user input the decline rate in the
                # commonly used sense of negative slope, i.e., declining rate
                di *= -1.0
            self.guess = [qi, b, di]
        self.model = None  # set default model
        if model is not None:
            if model.upper() in ['EXP', 'HYP']:
                self.model = model.upper()
            else:
                raise ValueError("Model specified is not 'EXP' or 'HYP'")

    def __call__(self, *args, **kwargs):
        """Do optimization and find best fit parameters
        ...
        (rest of the method remains the same)
        ...
        """

    def hypfunc(self, p, x):
        """Evaluate hyperbolic function with parameters
        ...
        (rest of the method remains the same)
        ...
        """
        qi, b, di = p
        return qi * (1.0 - b * di * x) ** (-1.0 / b)

    def expfunc(self, p, x):
        """Evaluate exponential function with parameters
        ...
        (rest of the method remains the same)
        ...
        """
        qi, di = p
        return qi * np.exp(di * x)

    def _r2(self, x, y, p):
        """calculate the final correlation coefficient
        ...
        (rest of the method remains the same)
        ...
        """

    def _report_err(self):
        if self.success is not 1:
            print("Error reported =", self.success)
        return

    def _find_best(self, *args, **kwargs):
        """Iterate over start periods and see if the best fit can be improved
        ...
        (rest of the method remains the same)
        ...
        """

    def _print_str(self):
        if self.used == 'HYP':
            qi, b, di = self.parameters
            return f"HYP: qt = {qi:.2f}*(1.0 -{b:.3f}*({di:.3f})*t)**(-1.0 /{b:.3f})\nr2={self.r2:.4f}"
        else:
            qi, di = self.parameters
            return f"EXP: qt = {qi:.2f}*np.exp({di:.3f}*t)\nr2={self.r2:.4f}"

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
