# Numeric Analysis
This project contains implementations of several numerical methods for solving systems of equations and finding roots of functions. The methods included are:
* Gaussian Elimination
* Bisection Method
* Newton-Raphson Method
* Secant Method
## Gaussian Elimination
The Gaussian Elimination method is used to solve systems of linear equations by using operations of matrix row manipulations. Given a coefficient matrix A and a right-hand side vector b, this method will return the solution vector x of the system of equations A * x = b. The method starts by transforming the coefficient matrix into an upper-triangular matrix by applying a sequence of row operations. Then it will perform back substitution to find the solution of the system.
## Bisection Method
The Bisection Method is a root-finding algorithm that uses the Intermediate Value Theorem to find a root of a function f(x) within an interval [a, b]. The method starts by finding the midpoint c of the interval, and then checks whether f(c) is close to zero or changes sign on either side of c. Depending on the sign of f(c), the method will then repeat the process on the left or right subinterval. The process is repeated until a root is found within the desired tolerance. The function returns the approximate root x and the number of iterations taken to find the root.
## Newton-Raphson Method
The Newton-Raphson Method is a root-finding algorithm that uses the first-order Taylor series expansion of a function f(x) to find a root. It starts with an initial guess x0 and then iteratively computes the next guess x1 = x0 - f(x0)/f'(x0). It uses the derivative of the function f(x) to find the slope of the tangent line at x0, and then finds the x-intercept of this line as the next approximation to the root. The process is repeated until a root is found within the desired tolerance. The function returns the approximate root x and the number of iterations taken to find the root.
## Secant Method
The Secant Method is a root-finding algorithm that uses a succession of roots of secant lines to better approximate a root of a function f(x). It starts with two initial guesses x0 and x1, then it use these points to compute the slope of the secant line between these points, and then finds the x-intercept of this line as the next approximation to the root. The process is repeated until a root is found within the desired tolerance. The function returns the approximate root x and the number of iterations taken to find the root

Please be aware that, these are iterative methods, and not always guarantee to find the root, and also depending on the function and the initial
