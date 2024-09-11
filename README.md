# Time Complexity Analysis and Merge Sort Project

## Overview

This project involves analyzing the runtime complexity of a function, fitting a polynomial curve to the data, and implementing the **Merge Sort** algorithm. The project is divided into two main tasks:

1. **Runtime Analysis of a Nested Loop Function:**
   - Analyze the time complexity of a nested loop function `f(n)`.
   - Time the function for various values of `n`.
   - Fit a polynomial curve to the timing data and determine the time complexity.
   - Find the approximate value of `n₀` where the polynomial fit starts to diverge from the timing data.

2. **Merge Sort Implementation:**
   - Implement the Merge Sort algorithm.
   - Test Merge Sort on an example array.

## Project Structure

### Files':'

- **`main.py`:**
  - Contains the timing analysis for function `f(n)`, polynomial fitting, and plotting.
  - Calls the `test_merge_sort()` function from `merge_sort.py`.
  
- **`merge_sort.py`:**
  - Contains the implementation of the Merge Sort algorithm.
  - Includes a test function to run Merge Sort on the array `[5, 2, 4, 7, 1, 3, 2, 6]`.

## Requirements

To run this project, you will need the following Python packages:

- `matplotlib`: For plotting the execution time and polynomial fits.
- `numpy`: For fitting a polynomial to the timing data.

You can install these using `pip`
