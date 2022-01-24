import numpy as np
import time
import threading
import matplotlib.pyplot as plt

def multithreadFractal (i, x_cor, y_cor, iterations):
    for j in range(len(y_cor)):
        c = complex(x_cor[i],y_cor[j]) # c = punto_en_x[i] + punto_en_y[j]*i
        z = complex(0, 0)
        count = 0
        for k in range(iterations):
            z = (z * z) + c # Z_n+1 = Zn^2 + C
            count = k+1 # Cantidad de iteraciones donde el numero no diverge
            if (abs(z) > 4):
                break
        output[i,j] = count
    
def mandelbrot(n_rows, n_columns, iterations):
    x_cor = np.linspace(-2,1,n_rows) # 1000 puntos entre -2 y 1 en el eje x
    y_cor = np.linspace(-2,1,n_columns) # 1000 puntos entre -2 y 1 en el eje y
    x_len = len(x_cor) # numero de puntos en eje x
    y_len = len(y_cor) # numero de puntos en eje y
    threads = list()
    for i in range(x_len):
        threads.append(threading.Thread(target=multithreadFractal, args=(i, x_cor, y_cor, iterations)))
        threads[i].start()
    for i in range(x_len):
        threads[i].join()

n_rows = int(input("n_rows: "))
n_columns = int(input("n_columns: "))
iterations = int(input("iterations: "))
output = np.zeros((n_rows,n_columns)) # Matriz de 0's de tamaño n_rows * n_columns
init_time = time.time()
mandelbrot(n_rows,n_columns,iterations)
#print(output)
print(str(time.time()-init_time) + " [s]")
plt.imshow(output.T, cmap = "hot")
plt.axis("on")
plt.show()
