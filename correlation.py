# -*- coding: utf-8 -*-

# copied+adapted from scipy.stats
# https://github.com/scipy/scipy/blob/v0.14.0/scipy/stats/stats.py#L2392

import numpy as np
import math

def pearsonr(x, y, pretty=False):
    """
    Calculates a Pearson correlation coefficient and the p-value for testing
    non-correlation.
    The Pearson correlation coefficient measures the linear relationship
    between two datasets. Strictly speaking, Pearson's correlation requires
    that each dataset be normally distributed. Like other correlation
    coefficients, this one varies between -1 and +1 with 0 implying no
    correlation. Correlations of -1 or +1 imply an exact linear
    relationship. Positive correlations imply that as x increases, so does
    y. Negative correlations imply that as x increases, y decreases.
    The p-value roughly indicates the probability of an uncorrelated system
    producing datasets that have a Pearson correlation at least as extreme
    as the one computed from these datasets. The p-values are not entirely
    reliable but are probably reasonable for datasets larger than 500 or so.
    Parameters
    ----------
    x : (N,) array_like
        Input
    y : (N,) array_like
        Input
    Returns
    -------
    (Pearson's correlation coefficient,
     2-tailed p-value)
    References
    ----------
    http://www.statsoft.com/textbook/glosp.html#Pearson%20Correlation
    """
    # x and y should have same length.
    x = np.asarray(x)
    y = np.asarray(y)
    n = len(x)
    mx = x.mean()
    my = y.mean()
    xm, ym = x-mx, y-my
    r_num = np.add.reduce(xm * ym)
    r_den = np.sqrt(ss(xm) * ss(ym))
    r = r_num / r_den

    # Presumably, if abs(r) > 1, then it is only some small artifact of floating
    # point arithmetic.
    r = max(min(r, 1.0), -1.0)
    df = n-2
    if abs(r) == 1.0:
        prob = 0.0
    else:
        t_squared = r*r * (df / ((1.0 - r) * (1.0 + r)))
        prob = betai(0.5*df, 0.5, df / (df + t_squared))

    r_z = np.arctanh(r)
    se = 1/np.sqrt(x.shape[0]-3)
    alpha = 0.05
    z = norm_ppf(1-alpha/2)
    lo_z, hi_z = r_z-z*se, r_z+z*se
    lo, hi = np.tanh((lo_z, hi_z))

#    import pdb; pdb.set_trace()
    
    
    if pretty:
        threshold=0.05
        for exponent in range(2, 10):
            if prob<10**(-exponent):
                threshold=10**(-exponent)

        print(prob, threshold)
        prob=("%.3g"%prob).lstrip("0")
        r=("%.2g"%r).lstrip("0")
        lo=("%.2g"%lo).lstrip("0")
        hi=("%.2g"%hi).lstrip("0")
        pretty="r=%s, "%(r)
        pretty+="p=%s\n"%(prob)
        pretty+="95%% CI: [%s,%s]"%(lo, hi) #
        return pretty
    return r, prob

def ss(a, axis=0):
    """
    Squares each element of the input array, and returns the sum(s) of that.
    Parameters
    ----------
    a : array_like
        Input array.
    axis : int or None, optional
        The axis along which to calculate. If None, use whole array.
        Default is 0, i.e. along the first axis.
    Returns
    -------
    ss : ndarray
        The sum along the given axis for (a**2).
    See also
    --------
    square_of_sums : The square(s) of the sum(s) (the opposite of `ss`).
    Examples
    --------
    >>> from scipy import stats
    >>> a = np.array([1., 2., 5.])
    >>> stats.ss(a)
    30.0
    And calculating along an axis:
    >>> b = np.array([[1., 2., 5.], [2., 5., 6.]])
    >>> stats.ss(b, axis=1)
    array([ 30., 65.])
    """
    return np.sum(a*a, axis)

def betai(a, b, x):
    """
    Returns the incomplete beta function.
    I_x(a,b) = 1/B(a,b)*(Integral(0,x) of t^(a-1)(1-t)^(b-1) dt)
    where a,b>0 and B(a,b) = G(a)*G(b)/(G(a+b)) where G(a) is the gamma
    function of a.
    The standard broadcasting rules apply to a, b, and x.
    Parameters
    ----------
    a : array_like or float > 0
    b : array_like or float > 0
    x : array_like or float
        x will be clipped to be no greater than 1.0 .
    Returns
    -------
    betai : ndarray
        Incomplete beta function.
    """
    x = np.asarray(x)
    x = np.where(x < 1.0, x, 1.0)  # if x > 1 then return 1.0
    return betainc(a, b, x)

def betainc(a, b, x):
    coefficient=math.gamma(a+b)/(math.gamma(a)*math.gamma(b))
    N=1000
    t=np.linspace(0,x,N)
    dt=x/N
    f=(t**(a-1))*((1-t)**(b-1))
    integral=np.sum(f*dt)
    return coefficient*integral
def norm_ppf(t):
    """returns the value of x such that t=P(N<x) where N~unit normal"""
    # this value confirmed by running scipy.special.ndtri
    if t==(1-0.05/2):
        return 1.959963984540054
    assert False, "need to precompute norm_ppf/scipy.special.ndtri: %f"%t
    
