# Standard convention to import NumPy as np
import numpy as np

# 1D NumPy ndarray: homogeneous, contiguous memory enabling vectorized math
sensor_data = np.array([24.5, 25.1, 26.3, 27.0, 28.2, 29.1, 27.8, 26.5, 25.7, 30.2])

print("Sensor Data:", sensor_data)
# Arithmetic mean (average) across all elements
print("Mean       :", round(np.mean(sensor_data), 2))
# Middle value when sorted (less sensitive to outliers than mean)
print("Median     :", round(np.median(sensor_data), 2))
print("Minimum    :", np.min(sensor_data))
print("Maximum    :", np.max(sensor_data))
# Population standard deviation (ddof=0 by default); measures spread around mean
print("Std. Dev.  :", round(np.std(sensor_data), 2))

threshold = 28.0
# `sensor_data > threshold` creates a boolean mask; indexing filters matching elements
high_values = sensor_data[sensor_data > threshold]
print("Values above", threshold, ":", high_values)