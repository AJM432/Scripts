from numba import jit
from tqdm import tqdm
import numpy as np
from PIL import Image
import time

# normal
MIN_X = -1.5
MAX_X = 0.5
MIN_Y = -1
MAX_Y = 1

X_INTERVAL = 0.001
Y_INTERVAL = 0.001
MAGNIFICATION = 1000
MAX_ITERATIONS = 200 # number of times to compute if number in set
HEIGHT = WIDTH = MAGNIFICATION*3


image = Image.new(mode='RGB', size=(WIDTH, HEIGHT))


@jit(nopython=True) # speeds up function
def num_Iterations_Mandelbrot(c): # c is a complex number
    i=z=0 # i is the iteration counter
    while z.real+z.imag < 4.0 and i < MAX_ITERATIONS: # number of iterations before determining if c in mandelbrot set
        i+=1
        z = z*z + c # iterate the function
    return i


@jit(nopython=True)
def create_Mandelbrot():
    coord_array = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8) # create an empty three dimensional array
    for x in np.arange(MIN_X, MAX_X, X_INTERVAL):
        for y in np.arange(MIN_Y , MAX_Y, Y_INTERVAL):
            # iterations = int(convert_range(inMandelbrot(c), 0, MAX_ITERATIONS, 0, 255)) # for color
            iterations = num_Iterations_Mandelbrot(complex(x, y))

            # numpy array stores as (y, x) pairs so must assign coords as (imag, real)
            if not iterations == MAX_ITERATIONS: # only plot if not in set, default color is black so not in set will always remain black
                coord_array[int(y*MAGNIFICATION+HEIGHT/2), int(x*MAGNIFICATION+WIDTH/1.5), 0:] = [iterations, iterations, iterations*5]
    return coord_array


start = time.perf_counter()
array = create_Mandelbrot()

image = Image.fromarray(array, mode='RGB')
image.show()
print(f"Execution time: {time.perf_counter()-start} seconds")
