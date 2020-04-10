# Week 2
1. **Introduction** 
   - Review: compute limits of sequences 
   - How does it change incase of real instead of natural domain 
   - How to compare function asymptotic point wise 
   - How does administering additional degree of freedom - second and other variable - affect limit 
## Limits of Functions: definition, arithmetic, important limits 
2. **Real domain funcion**
   - What's the difference between domains of sequences and real valued functions
     - Limit is value resembles given sequence the most as the number n gets closer to infinity 
     - There is always a natural number in any neighborbood of the infinity, that's the only point with this quality 
     - Real:  set of point +/- infinity
3. **Function Limits**
   - Function Limits 
     - for all xn -> a the squence of values f(xn) -> C
4. **Function’s Limit: Examples** 
   - |f(x) - A| < eps 
   - lim x->0 sin(1/x) = not exist 
5. **Function’s Limit: Arithmetic** 
   - sum, difference, product, division(only true if all the limits exist)
6. **Function’s Limit: Indeterminate Forms and Boundary Rule** 
   - ax^n/bx^m
     - m > n, 0
     - m < n, inif
     - m = n, a/b
  - The boundary rule 
    - Bounded and infinitesimal function in turn is infinitesimal too 
 7. **Two Important Limits**
    - lim n->inf (1+n)^n = e; lim n->0 (1+x)^1/x = e;
    - lim x->0 sinx/x = 1
## Asymptotic of functions: the tale of two O's
1. Asymptotic Notations and Big-O notation (Motivation)
   - Sometimes the functions we compare are not exactly equivalent but behavior similary and belong to the same class 
   - Sometime do not seek details of the function among its class 
   - The actual time depends on various things
   - We are interested in the number of operations
2. Big-O notation 
   - If f(x) = O(g(x)), for some neighborhood of the point x = a, one could find a constant c > 0 that |f(x)| <= c|g(x)|
3. Little-o
   - Which function is smaller or faster growing 
   - Notation: f(x) = o(g(x))
     - f(x) = a(x) * g(x), a(x)->0
     - f(x) = o(g(x)) => f(x)/g(x) -> 0
4. Asymptotic and Binomials
   - (n - l)/(k - l) > n/k, (l < k < n)
   - (n/k) <= n chose k
   - (n/k) <= n chose k <= n^k / k!
 ## Multivariate Functions
 1. **Definitions**
    - f(x1,x2,..,xn), R^n -> R. Normally, f(x,y) or f(x1, x2)
    - The concept of domain, range, support remains the same. The graph of the multivariate function exists in th R^(1+n) and is called surface. 
    - R3 as (x, y, f(x,y)) si usual three-dimensioanl surface 
    - f(x,y) = C, c: function's level or (c-level)
 2. **Limits**
   - f(x,y) = c => |f(x,y) - c| < eps
 3. **Example**
    - find all possible situation    
