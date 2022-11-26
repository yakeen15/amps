# Fourier Series for Periodic Functions
There is a way of approximating a function at any given point using *Taylor* series. There is a beautiful visualization of how *Taylor* series works by the great ***3Blue1Brown***. You can watch the amazing video [here](https://www.youtube.com/watch?v=3d6DsjIBzJ4).

The issue with *Taylor* series is that when the function has discontinuities, it doesn't work. Also, when approximating functional values further away from the center, we need to add more terms to the polynomial to get accurate results.

To avoid these issues, *Fourier* series comes in. We can approximate a function with great accuracy using *Fourier* series. At points of discontinuities, the *Fourier* series gives the average of the left-hand and right-hand limit of the function at those points. Since *Fourier* series has nearly identical repeating terms (only the indext varreis), it is easier to add newer terms to get more accurate results. Read more about *Fourier* series [here](https://en.wikipedia.org/wiki/Fourier_series).

My goal here was to write a program to create a visualization of the *Fourier* series of any periodic function. The plot here shows the functions and the *Fourier* series of that function at the same time in the interval (-10, 10). When running the code, the terminal will ask for the lower limit and the upper limit of the domain of the periodic function. After that, it will ask for the number of terms you want to use here. The higher the number of temrs, the closely the *Fourier* series will approximate the function. However, there is a limitation to how big the value of n can be. The *integrate* function is capped in terms of accuracy, meaning that a very big value of n, say 1000 won't give any more accurate results than, say 500. I could be wrong about this.
Next, the terminal will ask for the funtion. Here, you have to follow certain conditions. If you want to enter *sin(x)* as the function, you have to enter `np.sin(x)`. If the function is the *absolute value of x*, enter `abs(x)`. If the function is *x<sup>5</sup>*, einter `x**5`, and so on. 

The following gifs are graphs of the period functions *x<sup>3</sup>*, *x<sup>2</sup>*, and *absolute value of x* between the interval (-3, 4) with the number of terms 10.

**Inputs**

<img src="https://github.com/yakeen15/amps/blob/main/complex%20analysis/images%20and%20videos/inputs.png" width="300" height="300">

**GIFs**

![](https://github.com/yakeen15/amps/blob/main/complex%20analysis/images%20and%20videos/x%20cubed.gif)
![](https://github.com/yakeen15/amps/blob/main/complex%20analysis/images%20and%20videos/x%20squared.gif)
![](https://github.com/yakeen15/amps/blob/main/complex%20analysis/images%20and%20videos/absolute%20value%20of%20x.gif)

We can input piecewise functions as well. Following is the result of of the following inputs.

<img src="https://github.com/yakeen15/amps/blob/main/complex%20analysis/images%20and%20videos/piece%20inputs.PNG" width="600" height="120">

The function is -1 for *-2<x<0* and 1 for *0<x<1*. Following is the result:
![](https://github.com/yakeen15/amps/blob/main/complex%20analysis/images%20and%20videos/piece.gif)
