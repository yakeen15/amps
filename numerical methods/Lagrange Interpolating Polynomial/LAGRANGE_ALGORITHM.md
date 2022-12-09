## Theory  
First things first, we gotta get the theory of Lagrange interpolating polynomial first. Suppose we have two points in regular plane, and we wish to find the polynomial  
visits them both. There could be a lot of such polynomials, but the simplest on is a straight line. Say we wish to find the straight line between $(x_0,y_0)$ and $(x_1,y_1)$.  
We will define two functions $L_{0}(x) = \frac{x-x_0}{x_1-x_0}$ and $L_{1}(x) = \frac{x-x_1}{x_0-x_1}$ and define our straight line as $y = L_{0}(x)y_{0}+L_{1}(x)y_{1}$.  
We can confirm that this equation indeed passes through the specified points, and is also the equation of a straight line. Now all we need to do is extend this to n-points in order to fit any number of points and find the polynomial that visits all the points. As a general observation, we can say a polynomial that is to visit n points will have n-1 degree.
