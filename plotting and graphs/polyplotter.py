def polyplot(cl,x):
    n = len(cl)-1
    xval = 0.0
    while n >-1:
        xval = xval+float(cl[len(cl)-(n+1)])*(x**n)
        n = n-1
    return xval


