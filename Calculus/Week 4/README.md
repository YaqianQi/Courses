# Week 4
## Partial Derivatives and Differentiability 
1. Introduction: 
   - Multivariate case: Extrapolate the differentiability from straight line to hyperplane 
2. **Tangent Plane** (*tangent line -> tanget plane*)
   - Definition: **tangent plane** can be defined as a limit of all secant planes. 
3. **Partial Derivatives: Definition**
   - f(x,y) in (a,b). Assume cross section by plane y = b. f(x,y) turns into the curve f(x,b). The tangent plan turns line.  
   - The slope is called **partial** 
   - pf/px = lim x->a (f(x,b) - f(a,b))/(x - a) = (f(x,b))'x|x = a
4. **Partial Derivatives: Examples**
   - schema: 
     - substitute y = b -> find a derivative at x = a or 
     - substitute y = b -> find a derivative at every point -> substitude x = a 
5. **Tangent Plane: Definition**
   - z = f(a,b) + f'x*(x - a) + f'y*(y-b) 
6. **Differentiability of Multivariate Function**
  - *to be differentiable* = to be *"fitted"* with plane object 
  - f(x, y) is called differentiable at point (a, b) if it is close to its tangent plane 
    - f(x,y) = f(a,b) + f'x*(x - a) + f'y*(y - b) + R(x, y)
    - R(x,y) = o((x-a)^2 + (y - n)^2
7. **Differentiability of Multivariate Function: Example**
   - Differentiability 
     - Single-variate function: differentiable = has a derivative
     - Multi-variate functions: differentiable >> has partial derivative 
8. **Differentiability: Sufficient Condition**
   - **Sufficient condition**: if both derivaties f'x(x,y) and f'y(x,y) as functions of two variables (paritial derivatives at every point of real plane) are continuous at (a, b), then the function f(x,y) is differentiable at this point. 
9. Short Scheme
   - Check whether or not the function is bad enough already: does it have a discontinuity at the point of interest?
     - lim(x,y)→(a,b)f(x,y)≠f(a,b). If this inequality holds, then there is certainly no differentiability.
   - We need to compute partial derivatives at the point of interest. 
       - f′x(a,b)=(f(x,b))′∣x=a; f′y(a,b)=(f(a,y))′∣y=b. If any of them does not exist then there is no differentiability.
   - **sufficient condition**: instead of partial derivatives only at the point (a,b), you can find them at every point (x,y) and then check for discontinuities at the point (a,b). If both partial derivatives have no discontinuities at this point, then your function is differentiable at the point of interest.
   - Another way (and the way if your previous attempt failed) is to check the definition:
     - Δf=df+o(ρ)
     - df=f′x(a,b)(x−a)+f′y(a,b)(y−b)
     - check: f(x,y)−f(a,b)−df/ sqrt((x−a)^2+(y−b)^2) -> 0 
 10. **Basic Geometry and Gradient**
    - **Vector Space** : a set of vectors 
      - v belongs to V. a * v belongs to V
      - x, y belongs to V. x + y belongs to V
    - **Scalar product**: 
      - (a,b) = ax * bx + ay * by + az * az
      - length = sqrt((a,a))
      - orthogonality: a vertical b = (a, b) = 0 
    - **gradient point wise concpet**



