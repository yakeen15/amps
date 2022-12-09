## Theory  
First things first, we gotta get the theory of Lagrange interpolating polynomial first. Suppose we have two points in regular plane, and we wish to find the polynomial  
visits them both. There could be a lot of such polynomials, but the simplest on is a straight line. Say we wish to find the straight line between $(x_0,y_0)$ and $(x_1,y_1)$.  
We will define two functions $L_{0}(x) = \frac{x-x_1}{x_0-x_1}$ and $L_{1}(x) = \frac{x-x_0}{x_1-x_0}$ and define our straight line as $y = L_{0}(x)y_{0}+L_{1}(x)y_{1}$.  
We can confirm that this equation indeed passes through the specified points, and is also the equation of a straight line. Now all we need to do is extend this to n+1 points in order to fit any number of points and find the polynomial that visits all the points. As a general observation, we can say a polynomial that is to visit n+1 points will have n degree.  
The specialty of the function defined is that, for plugging in $(x_0,y_0)$, the term involving $L_{1}$ vanishes and $L_{0}$ evaluates exactly to 1, so the overall value of the polynomial turns out to be $y_{0}$. This happens for the other point too, and this is the behaviour we want to replicate in our polynomial. Breaking things down, we want a function $L_{i}(x)$ where $i\leq{n}$ such that  
1. $L_{j}(x_{i}) = 0$ whenever $j\neq{i}$  
2. $L_{j}(x_{i}) = 1$ whenever $j={i}$  


Below is a function of this form, that one could easily find by observation     

$\LARGE L_{j}(x)=\frac{\pi_{i=0,i\neq{j}}^{n}{(x-x_{i})}}{\pi_{i=0,i\neq{j}}^{n}{(x_{j}-x_{i})}}$  
Where $\pi$ is the product notation. Now we define our polynomial as $$y = \sum_{i=0}^{n} L_{i}(x)y_i$$  
And now we are done with the theory part. Since we have the functions defined, all that is left to do is to take the n+1 points and use those as input to calculate the coefficient functions and then we find the polynomial. We will do a practice run to see how well our formula works in pen and paper.  
## Test  
We have four points, $(1,3) , (2,9) , (3,10)$ and $(4,-1)$. We find the functions $L_{i}(x)$ using the formula.  
$\large L_{0}=\frac{(x-2)(x-3)(x-4)}{(1-2)(1-3)(1-4)}=\frac{-x^3}{6}+\frac{3x^2}{2}-\frac{13x}{2}+4$  
  
$\large L_{1}=\frac{(x-1)(x-3)(x-4)}{(2-1)(2-3)(1-4)}=\frac{x^3}{2}-4x^2+\frac{19x}{2}-6$  
  
$\large L_{2}=\frac{(x-1)(x-2)(x-4)}{(3-2)(3-2)(3-4)}=\frac{-x^3}{2}+\frac{7x^2}{2}-7x+4$  
  
$\large L_{3}=\frac{(x-1)(x-2)(x-3)}{(4-1)(4-2)(4-3)}=\frac{x^3}{6}-x^2+\frac{11x}{6}-1$  

Then for the formula of $y$ we get  
  
$y=L_{0}(x)y_0+L_{1}(x)y_1+L_{2}(x)y_2+L_{3}(x)y_3$  

We get four different polynomials from the three coefficient functions, and if we combine them all, we arrive at $y = \frac{7x^3}{6}+\frac{5x^2}{2}+\frac{x}{6}+-1$  
Whether you realize it or not, it was a huge task to compute 4 different polynomials and then combine them all to finally get a resultant polynomial. However, it would be incredibly tedious to do if one had to do this manually. Indeed, when doing on paper, it is better to find the value of $y$ at a certain point instead of calculating the whole polynomial.  
But what could we do if we wanted to know the form of the polynomial? Would it be a good idea to calculate all of it manually? Certainly not, when programming exists! Next we are going to discuss about the algorithm used to produce the coefficient of the polynomial.  

##Algorithm
