# Vectors

A **vector** is a special matrix with just one row or one column. Vectors are the building blocks of matrix operations.

## Column Vectors

A column vector is a matrix with one column:

$$
\mathbf{v} = \begin{bmatrix}
1 \\
2 \\
3
\end{bmatrix}
$$

This is a 3-element column vector. We often use bold lowercase letters for vectors.

## Row Vectors

A row vector is a matrix with one row:

$$
\mathbf{u} = \begin{bmatrix}
4 & 5 & 6
\end{bmatrix}
$$

## Vectors in Python

```{matrixforge-runner}
:title: Create vectors and inspect their shape
:packages: numpy

import numpy as np

# Column vector (shape: 3x1)
v = np.array([[1],
              [2],
              [3]])

# Or more commonly, as a 1D array
v = np.array([1, 2, 3])

print("Vector v:", v)
print("Shape:", v.shape)
```

## What Do Vectors Represent?

Vectors have many interpretations:

- **Points in space**: A 2D vector $[x, y]$ represents a point or position
- **Directions**: Vectors show direction and magnitude (like velocity or force)
- **Data samples**: A list of measurements (temperatures, prices, sensor readings)
- **Features**: In machine learning, a vector can represent features of an object

## Geometric Intuition

A 2D vector $\mathbf{v} = [3, 2]$ can be visualized as an arrow from the origin to the point $(3, 2)$:

```{matrixforge-runner}
:title: Draw a 2D vector
:packages: numpy, matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Define a vector
v = np.array([3, 2])

# Plot
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.006)
plt.xlim(-1, 4)
plt.ylim(-1, 3)
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vector v = [3, 2]')
plt.show()
```

## Vector Operations

Just like numbers, we can add, subtract, and scale vectors:

```{matrixforge-runner}
:title: Add and scale vectors
:packages: numpy

import numpy as np

u = np.array([1, 2])
v = np.array([3, 1])

# Addition
w = u + v
print("u + v =", w)  # [4, 3]

# Scaling (multiply by a number)
scaled = 2 * u
print("2 * u =", scaled)  # [2, 4]
```

## Why Vectors Matter

Vectors are everywhere in matrix mathematics:

- Matrices can be thought of as collections of column or row vectors
- Matrix multiplication combines vectors in powerful ways
- Many transformations act on vectors to produce new vectors

Understanding vectors is essential for understanding what matrices do.

## Try It

In the vector plot, change `v = np.array([3, 2])` to a few different vectors:

- `[-2, 3]`
- `[4, -1]`
- `[0, 3]`

Before running each one, predict the direction of the arrow.

## Key Takeaways

- A vector is a one-dimensional list of values.
- Vectors can represent points, directions, measurements, or features.
- Adding vectors combines their components.
- Scaling a vector changes its length without changing its basic direction, unless the scale is negative.

## Next Steps

Now let's look at {doc}`matrix-shape` to understand how matrices are sized and structured.
