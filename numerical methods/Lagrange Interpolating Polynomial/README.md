## Fitting a curve to 9 points using Lagrange interpolating polynomial  
Suppose we wish to find the curve that goes through 9 points. The 9 points are shown below.  


![](https://raw.githubusercontent.com/yakeen15/amps/main/numerical%20methods/Lagrange%20Interpolating%20Polynomial/points.png)
  
To find this graph which would join all these points, we could use [Lagrange interpolating polynomial](https://en.wikipedia.org/wiki/Lagrange_polynomial#:~:text=In%20numerical%20analysis%2C%20the%20Lagrange,a%20given%20set%20of%20data.). Using the lagrange.cpp file, we could enter any number of points less than 100, in order to get the coefficients of Lagrange interpolating polynomial, which we could then feed into our python plotting scripts located [here](https://github.com/yakeen15/amps/tree/main/plotting%20and%20graphs) in order to plot the points and the polynomial joining them.  
We compile both polyvect.cpp, which contains the function definitions for adding and multiplying two polynomials, and lagrange.cpp to produce an executable. Run the executable and feed the data points. We will get the coefficients of the interpolating polynomial, which should be saved to a file defined in the lagrange.cpp file. The initial data points are also stored in a separate file in order to plot later.

![](https://raw.githubusercontent.com/yakeen15/amps/main/numerical%20methods/Lagrange%20Interpolating%20Polynomial/lagrange_plot.png)  

We can now use our polyplotter.py and pointplotter.py scripts to plot the polynomial and the points together on the same graph to see if we get the desired results. The polyplotter.py file contains a function definition that accepts a list of coefficient and an x value as an input to find the value of the polynomial at that specific point, while the pointplotter.py plots both the data points and the polynomial obtained from interpolation from reading the files produced by the earlier code.    

![](https://raw.githubusercontent.com/yakeen15/amps/main/plotting%20and%20graphs/lagrange_fitting.png)
