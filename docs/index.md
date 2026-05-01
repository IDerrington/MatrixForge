# Welcome to MatrixForge

**Your interactive guide to understanding matrix mathematics.**

Matrices are everywhere in modern technology—from the graphics on your screen to the algorithms that process audio and video, from solving engineering problems to training neural networks. MatrixForge makes these concepts accessible and intuitive through clear explanations, visual examples, and hands-on Python code.

## What You'll Learn

This site guides you from the basics to real-world applications:

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} 🧮 Fundamentals
:link: fundamentals/index
:link-type: doc

Start with the basics: what matrices are, how to add and multiply them, and why they're useful. Build a solid foundation with intuition-first explanations.
:::

:::{grid-item-card} 🚀 Applications
:link: applications/index
:link-type: doc

Apply matrices to solve real problems: least squares fitting, digital signal processing, computer graphics, beamforming, and more.
:::

::::

## Why Matrices?

Matrices are compact ways to represent and manipulate data. A single matrix operation can:

- Transform 3D graphics in video games
- Process thousands of audio samples simultaneously
- Solve systems of equations from engineering problems
- Rotate, scale, and project images
- Beamform signals from antenna arrays

Instead of writing loops and tracking individual numbers, matrices let you express complex operations cleanly and compute them efficiently.

## Learning Path

```{mermaid}
graph LR
    A[What is a Matrix?] --> B[Vectors & Shapes]
    B --> C[Addition & Scaling]
    C --> D[Matrix Multiplication]
    D --> E[Transformations]
    E --> F[Applications]
    F --> G[DSP & Beamforming]
```

Start with {doc}`fundamentals/index` if you're new to matrices, or jump directly to {doc}`applications/index` if you want to see matrices in action.

## Interactive Examples

Throughout this site, you'll find executable Python code and Jupyter notebooks. Try them out, modify the parameters, and see what happens. The best way to learn is by doing.

```{code-block} python
import numpy as np

# Create a simple 2x2 matrix
A = np.array([[1, 2],
              [3, 4]])

print("Matrix A:")
print(A)
```

## Get Started

```{toctree}
:maxdepth: 2
:caption: Contents

fundamentals/index
applications/index
```

---

**Ready to start?** Head to {doc}`fundamentals/what-is-a-matrix` for your first lesson.
