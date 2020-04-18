# Week 3: Derivatives 
## The derivative and Differentiability 
1. **Derivative Definition** 
   - **Tangent Line**: The limit of secant lines 
      - f'(a) = lim x->a (f(x) - f(a))/(x-a)
2. **Differentiability** 
   - **Differential**: The linear part of the function's change 
      - delta_func = df + o(x-a) 
3. **Important Example of Derivatives** 
   - **Approach by definition**: f'(a) = lim x->a (f(x) - f(a))/(x-a)
     - (x^2)' = 2x
     - (x^n)' = n * x^(n-1)
     - (lnx)' = 1/x
     - (e^x)' = e^x
     - (a^x)' = a^x * lna
     - (sinx)' = cosx
     - (cosx)' = -sinx
     - (arctg)' = (tan)' = 1/(1+x^2)
 4. **Arithmetic of Derivatives**
    - **Sum**: (f + g)' = f' + g' 
    - **Difference**: (f - g)' = f' - g'
    - **Multiplication by number**: (Cf)' = Cf' 
    - **Multiplication**: (fg)' = f'g + fg' 
    - **Division**: (f / g)' = (f'g - fg')/g^2
 5. **Derivative: chain rule**
    - f(g(x))' = f'(g(x)) * g'(x)
 6. **Log euquotion**
    - find a tangent line: y = x ^ x, x = 1/e
      - Hint: y = f(a) + f'(a) * (x-a)
 7. **Inverse Function**
    - y = tanx 
## Linear Objects Associated with Differentiability 
1. **Tangent Line: Equation**
   - y = f(a) + f'(a) * (x-a)
   - Example x^x
2. **Linear Approximations**
  - Example: calculate sin 29 degree
    - Approach: use sin30 to approach by f(x) = f(a) + f'(x)*(x-a) + o(x-a); a = pi/6, x = pi/6 - pi/180 
3. **Mean Value Theorem**
  - f(x) is continuous on the closed interval [a,b]
  - f(x) is differentiable on the open interval (a,b)
  - there is a number c such a < c < b and f(b)-f(a) = f'(c)(b-a) 
  ## Derivatives of Higher Order
1. **Second Derivatives**
   - How fast and the trend 
   - Definition: x = a adn assume that f(x) is differentiable in a neighborhood of x = a. Then f''(a) is called the second derivative in this point if 
      - f''(a) = lim x->a (f'(x) - f'(a)) / (x-a) 
      - Example x^2, e^x
2. **Convexity**
   - **Convex**: f(x), if a segment between two points of the graph lies (strictly) above the curve i. 
     - Example: f(x) = x^2
   - **Concave**: The opposite layout - a segment below the graph 
3. **Extrema and First Derivative**
   - **local extremum**
   - **global extremum** 
4. **Extrema and Second Derivative**
   - **Happy Smile**: f(x) on the segment[a, b]. if f''(x) > 0 at every point of the segments, then the function is **convex**. In other word, if the slope of the first derivative keep increasing, then it's convex function. 
   - If f''(x) < 0, at every point of the segment, then the function is **concave**. 
   - since the convexity indicates monotonic rise(fall) of the first derivative, there can be only one extremum. 
6. **Extrema: Clearning the Air**
   - The extremum is locally greatest (or lowest value). The definition itself does not call for any differentiability.
   - If the function is differentiable in the extremum point, then f′(a)=0.
   - The inverse is not necessarily true: if the function has f′(a)=0 it does not imply the extremum at this very point; example f(x)=x^3
   - Similar thing applies for the differentiability: the differentiability is not a necessity for the extremum, example: f(x)=|x|
   - You can come up with a workaround for the latter case: assume that you find an extremum not via the value of the derivative in the point, but via changing the sign of the derivative as argument passes through given point (thus monotonic behaviour changes)
   - It is still not enough: one can come up with a function with no certain monotonicity in either left or right neighbourhoods (any). Think of the function exploiting sin1/x.

