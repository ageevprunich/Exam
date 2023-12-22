class ArithmeticProgression:
    def __init__(self, first, difference):
        self.first = first
        self.difference = difference

    def calculate_sum(self, n):
        if n == int(n):

            # Обчислення суми арифметичної прогресії за формулою: S_n = n/2 * [2a + (n-1)d]
            sum_of_prog = n / 2 * (2 * self.first + (n - 1) * self.difference)
            return sum_of_prog
        raise Exception("TypeError")