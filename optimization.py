from scipy.optimize import minimize

class optimization:

    def __init__(self, function, parameter) -> None:
        # 함수와 parameter 저장
        self.function = function
        self.parameter = parameter

    def scipy_min(self, method = 'COBYLA'):
        # scipy의 최소화 함수를 사용해서 최적값을 계산한다.
        result = minimize(self.function, self.parameter, method=method)
        return result
    
































