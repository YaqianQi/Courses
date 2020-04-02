# Introduction 
1. **Main topic** 
   - basic terms: numerical set , mapping and function 
   - function graph, how to get one through transitions of know graph 
   - how to properly define sequence and its limit 
2. **Numerical Set** 
   - **Numerical Set**: Various process as functions of several variables 
   - **Set**: Entity, collection of some object. 
     - object can belongs to one set or not; one object could be included in the set only one time; no order
     - Denote: X,Y,B,R capital letter. a belongs to a 
   - **Subset**: is any set of elements of the given set , 
     - empty set belongs any set. 
     - natural numbers N = {1,2,3,4..}
     - integer numbers N = {0,1,2,3,4..}
     - rational numbers Q = { m/n| m ∈ Z, n ∈ N}. 
     - real numbers R = {a0, a1, a2, ..}
       - *SQRT(2) is not rational). n^2 = 2k As a result, m and n should be number can not be divided by any other numbers*
 3. **Mapping and Quantifiers**
    - **Mapping**:ordered realtionship between elements of X and Y. (two sets X and Y)/ The rules takes an element from X and tells the set of mapped elements from Y
    - Logic notation: "for all"; "exist"
         
4. **Suplement Material** 
- Axiomatic definition
  - x+y=y+x, x⋅y=y⋅x (it is easy: the commutative rule)
  - (x+y)+z=x+(y+z), (x⋅y)⋅z=x⋅(y⋅z) (associativity)
  - (x+y)⋅z=x⋅z+y⋅z (distributivity)
  - Existence of two neutral elements 1 and 0: a⋅1=a, a+0=a.
  - Existence of the inverse elements (except 0): a+(−a)=0, a⋅a−1=1
   - Non-triviality 0≠1
- the ability to compare two numbers.
  - For any two real numbers one is able to say a>b, a<b or a=b.
  - This order is transitive: if a<b, b<c, then a<c.
- completeness. ℝ=A∪B, A∩B=∅, such as any element a∈A is smaller than any element b∈B. Then there is a pivot real number c∈ℝ that a≤c≤ b a≤c≤b for any aa and bb elements from the corresponding sets.

5. **Functions**
- **Functions**: two sets X, Y. If and only it associates each element of the X set to **exactly one** elemenmt of the Y set. X: domian/set of arguments, Y: Codomain/set of values.
  - Ways to describle function: table of values; algebraic; Graphical 
  - **Function Graph**: a certain curve on the plane, (x, f(x)), x belongs to the function domain. 
- **Arithmetic and Compostition**
  - Elementary function: constant, exponential, logarithmic, powers, trigonometric ...
    - By applying arithmetic operation +, -, *, / can changefunctions domain and codomain, but keeps the rsult in calss of elementary functions. 
  - **Compostion**: The result of consequent application of functions f and g is called a composite function or composition. g(f(x)) *F:X->Y AND Y->Z; f:map(x)-> Y and g:map(Y)-> Z
  - **Graph Transformation**:
    - Some simple example transformation 
      - **Vertical shift**: y = f(x) -> f(x) + c
      - **Horizontal shift**: y = f(x) -> f(x+c)
      - **Vertical contraction**: y = f(x) -> y = c * f(x)
      - **Horizontal contraction**: y = f(x) -> y = f(c * x)
      - **Absolute varaible**: y = f(|x|)
      - **Absolute value**: y = |f(x)|
    - *Example: −3f(2∣x∣+1)+3. Shrink in 2 times horizontally; move to left 1; scale -3 vertically and move up 3
6. **Sequence** 
   - **Sequence**: function of natural domain.(Some number set of real numbers) 
     - The domain of the sequence is discrete 
     - The sequence is the set of couted real numbers 
     - The sequence's domain does not necessarily include all N 
     - The number of elements in the sequences is infinite 
   - **limits of sequence**
     - Definition: The real number that resembles the sequence the most as the element's number infinitely grows(approach infinity)
       - Notation: *lim(an) = c: if c is the limit, we guarantee that the sequence stops to deviate significantly from it starting from some point.*
     - Examples: 
       - EX1: an = 1/ n. lim(an) = 0. The sequence has limits equals to 0, it's called **infinitesimal**
       - EX2: an = cos(x)/n. lim(an) = 0The product of bounded and infinitesimal is infinitesimal 
       - EX3: an = 2n + 1. limm(an) = +infinite. The sequence is unbounded and approaches to positive infinite. 
       - EX4: an = sin(pi * n) = (-1) ^ n. The sequence has no limit or it does not converge. 
     - **Limit of Sequences: Arithmetic Rules**
       - Some rules: note that's only true if all right side limits exist  
          - sum / difference: lim an = lim(bn +/- cn) 
          - product: lim (bn * cn)
          - division: lim(bn / cn)
       - Ex1: an = (n^2 + n)/ (2n^2 - 6n + 5) = numerate/n^2/denominator/n^2 = 1/2  
       - Ex2: an = (5 * 4^1/n + 2^1/n -6) / (4^1/n - 6 * 2^1/2 + 5)(*hint lim(2^1/n) = 1 = t) =  5 * t + 6 / (t - 5) = -11/4
     - **Newton's binomial theorem**
       - (a + b) ^ n = nC0 * a^ n + nC1 * a^ (n-1) * b + nC2 * a^ (n-2) * b^2+...+ nCn * b^n
     - **Series**
       - Sn = a1 + a2 + a3 +..+ an. The limit of sn is called the sum of the series(Upon its existence the series is called convergent).
         - EX1: Sn = 1 + 1/2 + 1/3 + ...+ 1/n.This series is not converge. 
         - EX2: Sn = 1 + p + p^2 + ... + p^n *(geometrical progression等比数列)* (1-p^(n+1))/(1-p) 
           - if p < 1, convergent; sn = 1/(1-p)
           - if p > 1, divergent. 
         - EX3: Sn = p + 2p^2 + ...+ np^n
           - col0: p + p^2 + p^3 + ...+p^n -> sn = p /(1-p)
           - col1: p^2 + p^3 + .. + p^n -> sn = p^2/(1-p)
           - sum = 1/(1-p) + p^2/(1-p) + p^3/ (1-p) +... = p/(1-p)^2 
      - ** The Definition of e**
        - en = (1+ 1/n) ^ n; lim(n->+inf) en = e 
        - **Monotone(单调）convergence theorem**:if a sequence increases and an has upper boundary, then it converges. Same applies for the case of decreasing squence with lower boudary.   
        - **Prove en is Monotone and bounded** 
     - The indeterminate forms 
       - **Indeterminate form**:inf/inf, 0/0, 1^inf, 0^0, inf-inf, 0 * inf, 0 * inf. 
         - The apprearance of the indeterminate forms doesn't give an answer. It only implies necessity of further transformations. 
       - EX1: an = (n^2 + 1)/ n = (n + 1/n) = +inf.
       - EX2: an = (n+1)/n^2 = (1/n + 1)/n = 0
     - Comparison between Polynomial(n^k), Exponential(a^n) and Logarithmic (lnn)^k Functions
       - **prove**: lim(n->+inf) n^k/a^n = 0; (ln(n))^k / n^k = 0
     - **limit of recurrence sequence
       - **revurrence sequence**: define n-th element through it's previous values. Xn+1 = f(xn,n) or Xn+1 = f(Xn, Xn-1..,n)
         - EX1: Fibonacci sequqnece x1 = x2 = 1, xn+1 = xn + xn-1, xn = 1/sqrt(5) * ((1+sqrt(5))/2 ^n - ((1-sqrt(5))/2)^n)
         - EX2: **Babylonian algorithm**: 
           - Monotone convergence theorem. 
           - make an initial guess; iterate: Xn+1 = (Xn + A/Xn)/2
           - set lim Xn = C, c = 1/2(C + A/C)
           - c = +/-sqrt(A)
         - EX3: Sn = (-1)^n, s1 = 1, sn+1 = 1-sn, c = 1 - c => c = 1/2. However, we know there is no limit for this sequence. This happpens because we assume the limit exist. So before we do the recurrent sequence estimation, we needs to prove the sequence is monotonic and  bounded.  
       
  

