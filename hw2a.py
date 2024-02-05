import math
def Gauss_Norm_PDF(x, mu, sigma):
    """
    This function  calculates the probability density function of a Gaussian
    (or normal) distribution.
    :param x: x = mu - 5 * sigma (point where the probability function is calculated)
    :param mu: mean of the distribution
    :param sigma: standard deviation of the distribution
    :return: returns the probability density at "x" for a Gaussian distribution with mean "mu"
    and standard deviation "sigma." This is not a probability, but a density of probability.
    The probability of "x" falling in a small interval around the input value "x" is roughly
    proportional to Gauss_Norm_PDF(x, mu, sigma) * dx where dx is the width of the interval.
    part 1: (1/sigma*math.sqrt(math.pi)) is the constant factor that makes the area under the
    curve of f(x) from -infinity to infinity equal to 1.
    part 2:  math.exp((1/2)*((x-mu)/sigma) ** 2) provides the bell-shape of the
    Gaussian distribution which is symmetric with respect to x = mu because the exponent is
    quadratic.
    chatgpt assisted in developing this function
    """
    return (1/ (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def simp_rule(f, a, b, n):
    """
    Simpsons 1/3 rule is a numerical integration process to calculate the area
    under the curve.
    Simpsons 1/3 rule is being used to approximate the integral of the PFD from
    "x = mu-5*sigma" to "c".
    Simpsons 1/3 rule divides the area into "n" intervals, and approximates the
    area of each interval with a parabola, the area of each parabola is then
    summed to give the total area.
    :param f(a) function value at the start of the interval
    :param f(b) function value at the end of the interval
    :param  n   is the end of range or stop value.
    chatgpt assisted in developing this function
    """
    h = (b-a) / n
    return (h/3) * (f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1,n,2)) + 2 * sum(
        f(a + i * h) for i in range (2,n,2)))

def Probability(PDF, args, c, GT = True):
    """
    The Probability function is used to calculate the probability
    that a random vairable falls within a certain range.
    :param PDF: call-back function that specifies the Gaussian
    (or normal) density function to be used in the calculation.
    The parent function "
    :param args: tuple containing mu and sigma
    :param c: point up to which the probability is calculated to.
    :param GT: boolean, if true the function calculates the
    probability that the random number is greater than "c", if
    false it calculates the probability that a random number is
    less than c.
    :return: if GT is true, it returns the complement of the integral
    (1 - integral) which gives the probability the number is greater
    than "c".
    chatgpt assisted in developing this function
    """
    mu, sigma = args
    n = 1000
    a = mu - 5 * sigma
    b = c
    integral = simp_rule(lambda x: PDF(x, mu, sigma), a, b, n)
    return 1 - integral if GT else integral

def main():
    """
    This function defines parameters for 2 different Gaussian distributions
    falling between certain ranges, then prints the results to the CLI.
    chatgpt assisted in developing this function
    """
    # for Probability x is less than c
    mu, sigma = 100, 12.5
    c = 105
    print(f"P(x<{c}|N({mu},{sigma}))={Probability(Gauss_Norm_PDF, (mu, sigma), c, GT=False):.2f}")

    # for Probability x is greater than c2
    mu2, sigma2 = 100, 3
    c2 = mu2 + 2 * sigma2
    print(f"P(x>{mu2+2*sigma2}|N({mu2},{sigma2})={Probability(Gauss_Norm_PDF, (mu2,sigma2), c2, GT = True):.2f}")

main()