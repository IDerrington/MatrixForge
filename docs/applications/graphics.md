# Computer Graphics

Matrices are the backbone of computer graphics. Every rotation, scaling, translation, and projection you see in 3D games and graphics software is a matrix operation.

## Why Matrices for Graphics?

Graphics operations need to:
- Transform objects (move, rotate, scale)
- Project 3D scenes onto 2D screens
- Combine multiple transformations efficiently
- Apply the same transformation to thousands of vertices

Matrices do all of this elegantly and efficiently.

## 2D Transformations

Let's start with simple 2D transformations. A point $(x, y)$ is represented as a vector:

$$
\mathbf{p} = \begin{bmatrix}
x \\
y
\end{bmatrix}
$$

### Scaling

To scale by factors $s_x$ and $s_y$:

$$
\begin{bmatrix}
s_x & 0 \\
0 & s_y
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
s_x \cdot x \\
s_y \cdot y
\end{bmatrix}
$$

### Rotation

To rotate by angle $\theta$ counterclockwise:

$$
\begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

```python
import numpy as np
import matplotlib.pyplot as plt

# Define a square
square = np.array([[0, 1, 1, 0, 0],
                   [0, 0, 1, 1, 0]])

# Rotation matrix (45 degrees)
theta = np.pi / 4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])

# Apply rotation
rotated_square = R @ square

# Plot
plt.figure(figsize=(8, 8))
plt.plot(square[0], square[1], 'b-', linewidth=2, label='Original')
plt.plot(rotated_square[0], rotated_square[1], 'r-', linewidth=2, label='Rotated 45°')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title('2D Rotation with Matrices')
plt.show()
```

## Homogeneous Coordinates

To handle translation (moving objects) with matrices, graphics use **homogeneous coordinates**. We add an extra dimension:

$$
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
$$

Now translation is a matrix operation:

$$
\begin{bmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
=
\begin{bmatrix}
x + t_x \\
y + t_y \\
1
\end{bmatrix}
$$

## 3D Transformations

In 3D graphics, points are $(x, y, z)$ and transformation matrices are $4 \times 4$ (using homogeneous coordinates).

### 3D Rotation (around Z-axis)

$$
R_z(\theta) = \begin{bmatrix}
\cos\theta & -\sin\theta & 0 & 0 \\
\sin\theta & \cos\theta & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

## Combining Transformations

The real power: **matrix multiplication chains transformations**. To rotate, then scale, then translate:

$$
\mathbf{p'} = T \cdot S \cdot R \cdot \mathbf{p}
$$

Compute $M = T \cdot S \cdot R$ once, then apply $M$ to all vertices. This is why matrices are so efficient for graphics.

## Projection

To display 3D scenes on a 2D screen, we use **projection matrices**. These transform 3D coordinates to 2D screen coordinates.

**Perspective projection** makes distant objects appear smaller (like a camera):

$$
P_{\text{persp}} = \begin{bmatrix}
\frac{1}{aspect \cdot \tan(\frac{fov}{2})} & 0 & 0 & 0 \\
0 & \frac{1}{\tan(\frac{fov}{2})} & 0 & 0 \\
0 & 0 & \frac{far + near}{far - near} & \frac{-2 \cdot far \cdot near}{far - near} \\
0 & 0 & 1 & 0
\end{bmatrix}
$$

## Graphics Pipeline

Modern graphics pipelines apply matrices at each stage:

1. **Model matrix**: Position objects in the scene
2. **View matrix**: Position the camera
3. **Projection matrix**: Project to screen
4. **Viewport transform**: Map to pixel coordinates

All of this is matrix multiplication.

## Applications

Matrix transformations power:

- Video games (3D rendering)
- Animation and visual effects
- CAD software
- Virtual/augmented reality
- Medical imaging visualization

## Coming Soon

Future sections will cover:
- Camera matrices
- Normal transformations
- Quaternions (alternative to rotation matrices)
- GPU optimization

## Next Steps

Check out {doc}`beamforming` for another application of matrix transformations, or explore {doc}`solving-systems` to see how graphics solves equations.
