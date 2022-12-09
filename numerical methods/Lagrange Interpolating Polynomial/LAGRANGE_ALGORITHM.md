## Theory  
First things first, we gotta get the theory of Lagrange interpolating polynomial first. Suppose we have two points in regular plane, and we wish to find the polynomial  
visits them both. There could be a lot of such polynomials, but the simplest on is a straight line. Say we wish to find the straight line between $(x_0,y_0)$ and $(x_1,y_1)$.  
We will define two functions $L_{0}(x) = \frac{x-x_1}{x_0-x_1}$ and $L_{1}(x) = \frac{x-x_0}{x_1-x_0}$ and define our straight line as $y = L_{0}(x)y_{0}+L_{1}(x)y_{1}$.  
We can confirm that this equation indeed passes through the specified points, and is also the equation of a straight line. Now all we need to do is extend this to n-points in order to fit any number of points and find the polynomial that visits all the points. As a general observation, we can say a polynomial that is to visit n points will have n-1 degree.  
The specialty of the function defined is that, for plugging in $(x_0,y_0)$, the term involving $L_{1}$ vanishes and $L_{0}$ evaluates exactly to 1, so the overall value of the polynomial turns out to be $y_{0}$. This happens for the other point too, and this is the behaviour we want to replicate in our polynomial. Breaking things down, we want a function $L_{i}(x)$ where $i\leq{n}$ such that  
1. $L_{j}(x_{i}) = 0$ whenever $j\neq{i}$  
2. $L_{j}(x_{i}) = 1$ whenever $j={i}$  
Below is a function of this form, that one could easily find by observation  
$\LARGE L_{j}(x)=\frac{\prod_{i=0,i\neq{j}}^{n}(x-x_{i})}{\prod_{i=0,i\neq{j}}^{n}(x_{j}-x_{i})}$