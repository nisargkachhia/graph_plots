'''import timeit
import matplotlib.pyplot as plt
import numpy as np

# Task 1: Function f(n) for runtime analysis
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1
    return x

# Task 2: Time the function for various n and plot the time vs n
def time_function():
    n_values = list(range(1, 101))  # Choose a suitable range for n
    times = []

    # Measure execution time for each n
    for n in n_values:
        time_taken = timeit.timeit(lambda: f(n), number=10)
        times.append(time_taken)

    # Plotting the time vs n
    plt.plot(n_values, times, label='Execution Time')
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title('Time vs n for function f(n)')
    plt.legend()
    plt.show()

    return n_values, times

# Task 3: Fit a polynomial and find bounds
def fit_polynomial(n_values, times):
    # Fit a polynomial curve
    coefficients = np.polyfit(n_values, times, 2)  # Fitting a quadratic curve
    polynomial = np.poly1d(coefficients)

    # Plot the original data and the fitted curve
    plt.plot(n_values, times, label='Original Time Data')
    plt.plot(n_values, polynomial(n_values), label='Fitted Polynomial Curve', linestyle='--')
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title('Time vs n with Polynomial Fit')
    plt.legend()
    plt.show()

    # Upper and lower bounds (Big-O, Big-Omega)
    print(f"Polynomial coefficients: {coefficients}")
    return coefficients

# Task 4: Zoom into the plot to find n₀
def find_n0(n_values, times):
    plt.plot(n_values, times, label='Execution Time')
    plt.xlim(0, 50)  # Zooming in on the lower range of n
    plt.ylim(0, max(times[:50]))  # Limiting the y-axis for zoom
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title('Zoomed Time vs n')
    plt.legend()
    plt.show()

# Modified function analysis
def modified_f(n):
    x = 1
    y = 1
    for i in range(n):
        for j in range(n):
            x += 1
            y = i + j  # Extra operation
    return x

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Testing merge sort on the array
def test_merge_sort():
    arr = [5, 2, 4, 7, 1, 3, 2, 6]
    print(f"Original Array: {arr}")
    merge_sort(arr)
    print(f"Sorted Array: {arr}")

if __name__ == "__main__":
    print("Timing function f(n)...")
    n_values, times = time_function()

    print("Fitting a polynomial to the data...")
    fit_polynomial(n_values, times)

    print("Zooming in to find n₀...")
    find_n0(n_values, times)

    print("Testing merge sort on array [5, 2, 4, 7, 1, 3, 2, 6]...")
    test_merge_sort()
'''

import timeit
import matplotlib.pyplot as plt
import numpy as np

# Task 1: Function f(n) for runtime analysis
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1
    return x

# Task 2: Time the function for various n and plot the time vs n
def time_function():
    n_values = list(range(1, 101))  # Choose a suitable range for n
    times = []

    # Measure execution time for each n
    for n in n_values:
        time_taken = timeit.timeit(lambda: f(n), number=10)
        times.append(time_taken)

    return n_values, times

# Task 3: Fit a polynomial and find bounds
def fit_polynomial(n_values, times):
    # Fit a polynomial curve
    coefficients = np.polyfit(n_values, times, 2)  # Fitting a quadratic curve
    polynomial = np.poly1d(coefficients)
    
    return polynomial, coefficients

# Task 4: Zoom into the plot to find n₀
def find_n0_plot(n_values, times):
    return n_values[:50], times[:50]

# Modified function analysis (if needed)
def modified_f(n):
    x = 1
    y = 1
    for i in range(n):
        for j in range(n):
            x += 1
            y = i + j  # Extra operation
    return x

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Testing merge sort on the array
def test_merge_sort():
    arr = [5, 2, 4, 7, 1, 3, 2, 6]
    merge_sort(arr)
    return arr

if __name__ == "__main__":
    print("Timing function f(n)...")
    n_values, times = time_function()

    print("Fitting a polynomial to the data...")
    polynomial, coefficients = fit_polynomial(n_values, times)

    print("Zooming in to find n₀...")
    n_zoomed, times_zoomed = find_n0_plot(n_values, times)

    print("Testing merge sort on array [5, 2, 4, 7, 1, 3, 2, 6]")
    sorted_arr = test_merge_sort()

    # Plotting all in one figure
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))  # 3 subplots in one figure

    # Plot 1: Time vs n
    axs[0].plot(n_values, times, label='Execution Time', color='blue')
    axs[0].set_title('Time vs n for function f(n)')
    axs[0].set_xlabel('n')
    axs[0].set_ylabel('Time (seconds)')
    axs[0].legend()

    # Plot 2: Time vs n with polynomial fit
    axs[1].plot(n_values, times, label='Original Time Data', color='blue')
    axs[1].plot(n_values, polynomial(n_values), label='Fitted Polynomial Curve', linestyle='--', color='red')
    axs[1].set_title('Time vs n with Polynomial Fit')
    axs[1].set_xlabel('n')
    axs[1].set_ylabel('Time (seconds)')
    axs[1].legend()

    # Plot 3: Zoomed view for n₀
    axs[2].plot(n_zoomed, times_zoomed, label='Zoomed Execution Time', color='green')
    axs[2].set_title('Zoomed Time vs n (Finding n₀)')
    axs[2].set_xlabel('n')
    axs[2].set_ylabel('Time (seconds)')
    axs[2].legend()

    # Adjust layout for better readability
    plt.tight_layout()
    plt.show()

    print(f"Sorted Array using Merge Sort: {sorted_arr}")
