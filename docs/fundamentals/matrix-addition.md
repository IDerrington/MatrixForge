# Matrix Addition

Matrix addition is simple: add corresponding elements together.

## The Basic Idea

To add two matrices, add each element with its partner in the same position:

$$
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
+
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
=
\begin{bmatrix}
1+5 & 2+6 \\
3+7 & 4+8
\end{bmatrix}
=
\begin{bmatrix}
6 & 8 \\
10 & 12
\end{bmatrix}
$$

## Element-by-Element

More formally, if $C = A + B$, then each element $c_{ij}$ is:

$$
c_{ij} = a_{ij} + b_{ij}
$$

The element in row $i$, column $j$ of $C$ equals the sum of the corresponding elements from $A$ and $B$.

## In Python

```{matrixforge-runner}
:title: Add two matrices element by element
:packages: numpy

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = A + B

print("A + B =")
print(C)
```

## Requirements

**The matrices must have the same shape.** You can't add a $2 \times 3$ matrix to a $3 \times 2$ matrix.

```{matrixforge-runner}
:title: See why shape compatibility matters
:packages: numpy

import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])  # 2x3

B = np.array([[7, 8],
              [9, 10]])  # 2x2

print("A shape:", A.shape)
print("B shape:", B.shape)

try:
    C = A + B
except ValueError as error:
    print("Addition failed:")
    print(error)
```

## Scalar Multiplication (Scaling)

You can also multiply a matrix by a single number (a scalar). This scales every element:

$$
3 \times \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
=
\begin{bmatrix}
3 & 6 \\
9 & 12
\end{bmatrix}
$$

In Python:

```{matrixforge-runner}
:title: Scale every element in a matrix
:packages: numpy

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = 3 * A

print("3 * A =")
print(B)
```

## Real-World Example

Imagine you have sales data for two quarters:

```{matrixforge-runner}
:title: Combine quarterly sales data
:packages: numpy

import numpy as np

# Sales in Q1 (rows: products, columns: regions)
Q1 = np.array([[100, 150, 200],
               [80, 120, 90]])

# Sales in Q2
Q2 = np.array([[110, 140, 210],
               [85, 130, 95]])

# Total sales across both quarters
total = Q1 + Q2

print("Total sales (Q1 + Q2):")
print(total)
```

## Properties

Matrix addition has nice properties:

- **Commutative**: $A + B = B + A$
- **Associative**: $(A + B) + C = A + (B + C)$
- **Identity**: $A + 0 = A$ (where $0$ is a matrix of all zeros)

These work just like regular number addition.

## Subtraction

Matrix subtraction works the same way—subtract corresponding elements:

$$
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
-
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
=
\begin{bmatrix}
4 & 4 \\
4 & 4
\end{bmatrix}
$$

```{matrixforge-runner}
:title: Subtract corresponding entries
:packages: numpy

import numpy as np

A = np.array([[5, 6],
              [7, 8]])

B = np.array([[1, 2],
              [3, 4]])

C = A - B

print("A - B =")
print(C)
```

## Try It

In the addition example, change one value in `A` and predict exactly which value in `A + B` will change.

Then try changing the scalar in the scaling example from `3` to `-2`. What happens to every entry?

## Key Takeaways

- Matrix addition works element by element.
- Matrix subtraction also works element by element.
- Addition and subtraction require matching shapes.
- Scalar multiplication scales every entry in the matrix.

## Next Steps

Addition is straightforward because it works element-by-element. But matrix {doc}`matrix-multiplication` is different—and much more powerful. Let's explore it next.
