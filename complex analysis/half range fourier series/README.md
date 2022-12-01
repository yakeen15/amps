# Half Range Fourier Series
In the case of half range *Fourier* series, we turn a given function into an [*even function*](https://www.cuemath.com/calculus/even-function/) or an [*odd function*](https://www.cuemath.com/calculus/odd-functions/) and then turn it into a *fourier* series. In the case of [*half range cosie series*](https://www.intmath.com/fourier-series/4-fourier-half-range-functions.php), we use even functions. In the case of [*half range sine series*](https://www.intmath.com/fourier-series/4-fourier-half-range-functions.php), we turn the function into an odd function. In both cases in the program, the lower limit is 0. The program asks for the upper limit, the number of terms to be computed, and the function. 

The gifs here are the result of the following inputs:

***Inputs:***

<img src="https://github.com/yakeen15/amps/blob/main/complex%20analysis/half%20range%20fourier%20series/images%20and%20videos/inputs.PNG" width="600" height="100">

***Sine Series:***

![](https://github.com/yakeen15/amps/blob/main/complex%20analysis/half%20range%20fourier%20series/images%20and%20videos/sine.gif)

***Cosine Series:***

![](https://github.com/yakeen15/amps/blob/main/complex%20analysis/half%20range%20fourier%20series/images%20and%20videos/cosine.gif)

The code uses **imageio** and **os** modules to create a gif and save the file in the same directory as the code. It creates each frame as a png file, then merges the photos together to create the gif. This is a heavy task, and the execution time depends on the specification of the system. Therefore, proceed at your own risk. You can omit the following blocks of code to skip the saving part:
```
        filename = f'{i}.png'
        filenames.append(filename)
        plt.savefig(filename)
    with imageio.get_writer('x cubed.mp4', fps=60) as writer:
        for filename in filenames:
            image = imageio.v2.imread(filename)
            writer.append_data(image)
    
    for filename in set(filenames):
        os.remove(filename)
```
