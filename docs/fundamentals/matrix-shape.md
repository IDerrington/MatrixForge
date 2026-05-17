# Matrix Shape and Size

The **shape** of a matrix tells you its dimensions: how many rows and columns it has.

## Dimensions

A matrix with $m$ rows and $n$ columns is called an "$m \times n$ matrix" (read as "m by n").

$$
A = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

This is a $2 \times 3$ matrix: 2 rows, 3 columns.

## Shape in Python

```{matrixforge-runner}
:title: Inspect matrix dimensions
:packages: numpy

import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Matrix A:")
print(A)
print("Shape:", A.shape)  # (2, 3)
print("Number of rows:", A.shape[0])  # 2
print("Number of columns:", A.shape[1])  # 3
```

## Common Matrix Shapes

### Square Matrix

A matrix with the same number of rows and columns:

$$
B = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

This is a $2 \times 2$ square matrix. Square matrices have special properties we'll explore later.

### Column Vector

An $m \times 1$ matrix:

$$
\mathbf{v} = \begin{bmatrix}
1 \\
2 \\
3
\end{bmatrix}
$$

Shape: $3 \times 1$

### Row Vector

A $1 \times n$ matrix:

$$
\mathbf{u} = \begin{bmatrix}
4 & 5 & 6
\end{bmatrix}
$$

Shape: $1 \times 3$

## Why Shape Matters

The shape of a matrix determines:

1. **What operations are valid**: You can't add a $2 \times 3$ matrix to a $3 \times 2$ matrix
2. **The result of operations**: Multiplying a $2 \times 3$ matrix by a $3 \times 2$ matrix gives a $2 \times 2$ result
3. **What the matrix represents**: A $1920 \times 1080$ matrix might represent an HD image

## Shape Compatibility

For matrix addition, shapes must match exactly:

```{matrixforge-runner}
:title: Check shape compatibility for addition
:packages: numpy

import numpy as np

A = np.array([[1, 2],
              [3, 4]])  # 2x2

B = np.array([[5, 6],
              [7, 8]])  # 2x2

C = A + B  # Works! Both are 2x2

print("A shape:", A.shape)
print("B shape:", B.shape)
print("A + B:")
print(C)

D = np.array([[1, 2, 3]])  # 1x3
print("D shape:", D.shape)
print("A and D have different shapes, so A + D would fail.")
```

For matrix multiplication, the number of columns in the first matrix must equal the number of rows in the second. We'll cover this in detail in {doc}`matrix-multiplication`.

## Reshaping Matrices

Sometimes you need to change a matrix's shape:

```{matrixforge-runner}
:title: Reshape the same data
:packages: numpy

import numpy as np

# Create a 1D array
data = np.array([1, 2, 3, 4, 5, 6])

# Reshape to 2x3
A = data.reshape(2, 3)
print("2x3 matrix:")
print(A)

# Reshape to 3x2
B = data.reshape(3, 2)
print("3x2 matrix:")
print(B)
```

The total number of elements must stay the same (here, 6 elements).

## Try It

In the reshape example, try reshaping the six values into:

- `1 x 6`
- `6 x 1`
- `2 x 3`
- `4 x 2`

Which ones work? Which one fails, and why?

## Key Takeaways

- Matrix shape is written as rows by columns.
- Addition requires matching shapes.
- Matrix multiplication has a different compatibility rule.
- Reshaping changes the layout, but the total number of elements must stay the same.

## Next Steps

Now that you understand matrix shapes, let's learn about {doc}`matrix-addition`, the simplest matrix operation.
