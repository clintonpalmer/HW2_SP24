import math
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Secant method is a root finding algorithm that uses a succession
    of roots of secant lines combined with the method of bisection to
    approximate the root of a function.
    where the
    :param fcn: is the function to be evaluated by the secant method
    :param x0: is the initial approximation.
    :param x1: is the initial approximation.
    :param maxiter: is the maximun number of iterations, if this function is
    reached the last x will be returned, giving the best estimate for the
    root.
    :param xtol: tolerance for the convergence of the method. It is used as a
    stopping criterion for the iteration process. If the absolute difference
    between the current estimate and the previous is less than xtol, the function
    assumes that it has found the root and stops iterating.
    :retuns: returns estimated root
    chatgpt assisted in developing this function
    """
    i = 0 #Initialize iteration counter to 0
    while i <= maxiter:  #While iteration counter is less than maxiter
        f0 = fcn(x0)
        f1 = fcn(x1)
        if abs(f1) < xtol: #If absolute value of f1 is less than xtol
            return x1  # return x1 (root found)
        else:
            new_guess = x1 - f1 * (x1 - x0) / (f1 - f0)
            x0 = x1 #Set x0 to x1
            x1 = new_guess # x1 to new guess
        i += 1  #Increment iteration counter
    return x1

def main():
    """
    Defines the mathematical functions to be used by the secant method
    to approximate the root.
    After, the root is returned and printed.
    chatgpt assisted in developing this function
    """
    def fcn(x):
        """
        Defines the function and sends the parameters to the secant function
        """
        return x - 3 * math.cos(x) #Define the function for which we want to find the root
    root = Secant(fcn, 1, 2, 5, 1e-4) #parameters to send to Secant function
    print(f"x - 3cos(x) = 0; when x = {root:.4f}") #print to CLI
    def fcn(x):
        """
        Defines the function and sends the parameters to the secant function
        """
        return math.cos(2*x) * (x ** 3) #Define the function for which we want to find the root
    root = Secant(fcn, 1, 2, 15, 1e-8)
    print(f"cos(2x)\u22C5x\u00B3  = 0; when x = {root:.8f}")
    def fcn(x):
        """
        Defines the function and sends the parameters to the secant function
        """
        return math.cos(2*x) * (x ** 3) #Define the function for which we want to find the root
    root = Secant(fcn, 1, 2, 3, 1e-8)
    print(f"cos(2x)\u22C5x\u00B3  = 0; when x = {root:.8f}")

main()


