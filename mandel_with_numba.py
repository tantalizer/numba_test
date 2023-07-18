# With Numba
from matplotlib.pylab import imshow, ion
import numpy as np
from matplotlib import pyplot as plt
import time
from numba import jit

@jit
def mandel(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    i = 0
    c = complex(x,y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i

    return 255

@jit
def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color

    return image

image = np.zeros((1000 * 2, 1500 * 2), dtype=np.uint8)
#%timeit create_fractal(-2.0, 1.0, -1.0, 1.0, image, 20)
start = time.time()
img = create_fractal(-2.5, 1.25, -1.25, 1.25, image, 50)
end = time.time()
print("Took %f ms" % ((end - start) * 1000.0))
plt.imshow(img)
plt.show()
