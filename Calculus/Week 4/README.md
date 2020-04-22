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
## Chain Rule for Multivariate Case 
1. **Chain Rule: One Independent Variable**
   - df/dt = pdf/pdx * dx/dt + pdf/pdy * dy/dt
2. **Chain Rule: Vector Form**
   - f(x,y), g(t) = (x(t), y(t))
   - g'(t) = (x'(t),y'(t))
   - df/dt = pdf/pdx * dx/dt + pdf/pdy * df/dt = (pdf, g'(t))
3. **Chain Rule: several independent variables**
   - Example: f(x,y) = x * y^2, x(u,v) = u + v, y(t) = u - v
4. Implicit Derivative 
5. Change Variables 
   - Cartesian coordinates and Polar coordicnates 
     - x = r * sin(ita), y = r * cos(ita) 
 ## Second Partial Derivatives 
 1. Second Partial Derivatives
    - f''(x,y)(x,y) = (f'x(x,y))'y
    - Example: x^y^2.
 2. Second Partial Derivatives: order of derivatives
    - Order matters 
    - **Clairaut's theorem**: one can construct a function with two existent but not coinciding second derivatives. 
    - The sufficient condition is **continuality** of compared derivatives. More narrow and simpler idea: the existence of higher derivative. 
3. **Differentials of Multivariate Functions**
   - Concept of differentials
     - **singlevariate functions**: the change of function if it were its tangent line 
     - **multivariate functions**: the change of function if it were it's tangent hyperplane. df = f'x * dx + f'x * dy
     - f'' = f''xy + 2 * f''xx+ f''yy
     - Example: 
       - f(x, y, z)
       - f(x,y) = e^(a * x + b * y)
 4. **Convexity**
    - f(a * x + (1-a) * y) < a * f(x) + (1 - a) * f(y)
    - Example: f = x^2 + y^2 
 5. **Second Partial Derivatives: Convexity**
    - f'' = f''xx * dx^2 + 2 * f''xydydx + f''yydy^2 
    - D = f''xx * f''yy - (f''xy)^2 
    - D > 0(no root) and f'xx > 0, convex
    - D > 0(no root) and f'xx < 0, concave 
  6. Quadratic forms and convext 
     
     
       
    
   

