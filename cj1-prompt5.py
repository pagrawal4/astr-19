import math
import numpy as np
from tabulate import tabulate

x = np.linspace(0, 2*math.pi, 1000)
y = np.sin(x)

table_data = [(a, b) for a, b in zip(x, y)]

table_headers = ["x", "sin(x)"]
python_table = tabulate(table_data, tablefmt="grid", headers=table_headers,
    floatfmt=".3f")

def main():
    print(python_table)

if __name__ == '__main__':
    main()