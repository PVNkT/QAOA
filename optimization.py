from scipy.optimize import minimize

class opimization:

    def __init__(self, function, parameter) -> None:
        self.function = function
        self.parameter = parameter

    def scipy_min(self, method = 'COBYLA'):
        result = minimize(self.function, self.parameter, method=method)
        return result
    
































