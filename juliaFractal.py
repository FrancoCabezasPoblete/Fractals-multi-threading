import numpy as np
import time
import threading
import matplotlib.pyplot as plt

def multithreadFractal (i, x_cor, y_cor, iterations, c):
    for j in range(len(y_cor)):
        z = complex(x_cor[i], y_cor[j])
        count = 0
        for k in range(iterations):
            z = (z * z) + c
            count = count + 1
            if (abs(z) > 4):
                break
        output[i,j] = count

def mandelbrot(n_rows, n_columns, iterations, cx, cy):
    x_cor = np.linspace(-2, 2, n_rows)
    y_cor = np.linspace(-2, 2, n_columns)
    x_len = len(x_cor)
    c = complex(cx, cy)
    threads = list()
    for i in range(x_len):
        threads.append(threading.Thread(target=multithreadFractal, args=(i, x_cor, y_cor, iterations, c)))
        threads[i].start()
    for i in range(x_len):
        threads[i].join()
        
n_rows = int(input("n_rows: "))
n_columns = int(input("n_columns: "))
iterations = int(input("iterations: "))
cx = float(input("Cx: "))
cy = float(input("Cy: "))
output = np.zeros((n_rows,n_columns)) # Matriz de 0's de tamaño n_rows * n_columns
init_time = time.time()
mandelbrot(n_rows,n_columns,iterations, cx, cy)
#print(output)
print(str(time.time()-init_time) + " [s]")
plt.imshow(output.T, cmap='hot')
plt.axis("on")
plt.show()