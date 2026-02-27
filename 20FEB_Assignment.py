#Assignment Name : NumPy Speed Test
#Description : Compare Python lists vs NumPy arrays with 1M numbers, measure execution time, write 3 observations.
import numpy as np
import time
# Creating a list of 1 million numbers
python_list = list(range(1, 1000001))
# Creating a NumPy array of 1 million numbers
numpy_array = np.arange(1, 1000001)
# Timing the Python list operation (summing the list)
start_time = time.time()
list_sum = sum(python_list)
end_time = time.time()
print(f"Python list sum: {list_sum}, Time taken: {end_time - start_time:.4f} seconds")
# Timing the NumPy array operation (summing the array)
start_time = time.time()
numpy_sum = np.sum(numpy_array)
end_time = time.time()
print(f"NumPy array sum: {numpy_sum}, Time taken: {end_time - start_time:.4f} seconds")
# Observations:
# 1. The NumPy array operation is significantly faster than the Python list operation due to optimized C and Fortran code under the hood.
# 2. NumPy arrays are more memory efficient than Python lists, which can lead to better performance, especially with large datasets.
# 3. For numerical computations, using NumPy is generally recommended over Python lists for better performance and ease of use, as it provides a wide range of mathematical functions and operations.
