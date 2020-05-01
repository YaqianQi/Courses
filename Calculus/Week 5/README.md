# Week 5
## Anti-derivative and Indefinite Integral: Definition and Calculation 
1. **Introduction** 
   - inverse operation to differentiation - integration 
   - Integral can be seen as continuous summation 
2. **Antiderivative: Definition**
   - **antiderivative**: F'(x) = f(x)
   - **indefinite integral**: antiderivatives of f(x): can be described as all possible vertical shift. integral f(x) = F(x) + c
3. **Antiderivative: Table of Integrals**
   - Table of integrals 
4. **Change of Variable and Integration by Parts**
   - replace high order variable with low 
     - Example: Intg x/(1+x^2)dx
   - Integral by part: Intg f' * g = f * g - intg f * g'dx
   - Example Intg arctag x dx 
5. **Antiderivative: Examples**
   - intg |x|dx = |x|* x /2 + c
   - intg 1/x dx = ln|x| + c, x > 0; = ln(-x) + c, x < 0
6. **Integrability in Elementary Functions**
   - **Integrable in elementary function**: if it's indefinite integral can be written by the fininite number of arithmetic operation and compositions of elementary function.
   - **Rational Fraction**: R(x) = P(x)/Q(x). p(x) and Q(x) are rational polynomials. 
     - Rational functions are always integrable 
## Definite Integral: Area Under Curve and Fundamental Theorem of Calculus 
1. **Definite Integral**
   - Definite integral: lim d->0 S(t, f, t) = Integral f(x) dx exists independently from t and actual partition
2. **Definite Integral: Existence**
   - lower sum < S(t,f,t) < Upper sum and they all get the same sum. Then exist 
3. **Definite Integral: Sufficient Conditions**
   - The function monotonically rises or fall for all the segment 
   - The function has no discountinuations for all the segment 
   - Example: f(x) = x^2, [a,b] = [1,0] calculate the under line area 
4. **Fundamental Theorem of Calculus**
   - Intg (a,b)f(x)dx = F(b) - F(a)
5. **Improper Integrals**
   - integral from a to +inf f(x)dx = lim b->+inf f(x)dx 
      - converges: exist limit 
      - not converge: non-existence or +inf
   - Example: integral 0 to +inf e^(-ax) dx 
6. **Improper Integrals: Examples and Comparison Rule**
   - Example: integral 1 to +inf x^(-a)dx, 
     - a > 1, converge; otherwise, not converge 
7. **Numerical Methods of Integration**
   - **midpoint rule**: integral a to b f(x)dx = (b-a)*f((a+b)/2)
   - **Trapezoidal rule**: integral a to b f(x)dx = (b-a)((f(a)+f(b))/2)
   - **simpson's rule**: integral a to b f(x)dx = (b-a)/6*(f(a)+f(b)+4*f((a+b)/2)) 
 


