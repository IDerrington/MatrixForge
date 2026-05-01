# What is a Matrix?

A **matrix** is simply a rectangular grid of numbers. That's it. Nothing scary.

## The Simplest Example

Here's a matrix with 2 rows and 3 columns:

$$
A = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

You can think of it like a small spreadsheet or a table of data.

## Why Use Matrices?

Imagine you're tracking temperatures at three locations over two days:

| Location 1 | Location 2 | Location 3 |
|------------|------------|------------|
| 22°C       | 25°C       | 19°C       |
| 24°C       | 23°C       | 21°C       |

This is a matrix! The numbers are organized in a way that makes them easy to work with. In Python, we represent this as:

```python
import numpy as np

temperatures = np.array([[22, 25, 19],
                         [24, 23, 21]])

print(temperatures)
```

## Real-World Examples

Matrices show up everywhere:

- **Images**: Every digital image is a matrix where each number represents a pixel's brightness or color
- **Audio**: Sound processing uses matrices to filter and transform audio signals
- **Graphics**: 3D games use matrices to rotate, scale, and position objects
- **Data**: Spreadsheets, databases, and datasets are all matrices
- **Networks**: Social networks and web pages can be represented as matrices

## Notation

We typically use capital letters for matrices: $A$, $B$, $M$, etc.

Individual elements (the numbers inside) are written with subscripts. The element in row $i$, column $j$ of matrix $A$ is written as $a_{ij}$ or $A_{ij}$.

For our temperature matrix:
- $a_{11} = 22$ (row 1, column 1)
- $a_{12} = 25$ (row 1, column 2)  
- $a_{23} = 21$ (row 2, column 3)

## Key Insight

**Matrices let you work with many numbers at once.** Instead of writing separate operations for each temperature, location, or pixel, you can apply operations to the entire matrix. This makes code cleaner and computations faster.

## Next Steps

Now that you know what a matrix is, let's explore {doc}`vectors`, which are special types of matrices with just one row or one column.
