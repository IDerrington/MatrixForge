"""
Plotting utilities for visualizing vectors and transformations.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Optional


def plot_vector_2d(
    vector: np.ndarray,
    origin: np.ndarray = np.array([0, 0]),
    color: str = 'blue',
    label: Optional[str] = None,
    ax: Optional[plt.Axes] = None
) -> plt.Axes:
    """
    Plot a 2D vector as an arrow.

    Parameters
    ----------
    vector : np.ndarray
        2D vector to plot, shape (2,)
    origin : np.ndarray
        Starting point of the vector, shape (2,)
    color : str
        Color of the arrow
    label : str, optional
        Label for the vector
    ax : plt.Axes, optional
        Matplotlib axes to plot on. If None, creates new figure.

    Returns
    -------
    ax : plt.Axes
        The axes object
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))

    ax.quiver(
        origin[0], origin[1], vector[0], vector[1],
        angles='xy', scale_units='xy', scale=1,
        color=color, width=0.006, label=label
    )

    # Set reasonable limits
    max_val = max(abs(vector[0] + origin[0]), abs(vector[1] + origin[1]))
    margin = max_val * 0.2
    ax.set_xlim(-margin, max_val + margin)
    ax.set_ylim(-margin, max_val + margin)

    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_aspect('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    if label:
        ax.legend()

    return ax


def plot_transformation_2d(
    points: np.ndarray,
    matrix: np.ndarray,
    title: str = "2D Transformation",
    original_color: str = 'blue',
    transformed_color: str = 'red'
) -> plt.Figure:
    """
    Plot original and transformed points under a 2D linear transformation.

    Parameters
    ----------
    points : np.ndarray
        Original points, shape (2, n) where n is number of points
    matrix : np.ndarray
        2x2 transformation matrix
    title : str
        Plot title
    original_color : str
        Color for original points
    transformed_color : str
        Color for transformed points

    Returns
    -------
    fig : plt.Figure
        The figure object
    """
    transformed_points = matrix @ points

    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot original shape
    ax.plot(points[0], points[1], 'o-', color=original_color,
            linewidth=2, markersize=6, label='Original')

    # Plot transformed shape
    ax.plot(transformed_points[0], transformed_points[1], 'o-',
            color=transformed_color, linewidth=2, markersize=6,
            label='Transformed')

    # Set equal aspect and grid
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    # Set limits to show both shapes
    all_points = np.hstack([points, transformed_points])
    max_val = np.max(np.abs(all_points))
    margin = max_val * 0.2
    ax.set_xlim(-max_val - margin, max_val + margin)
    ax.set_ylim(-max_val - margin, max_val + margin)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(title)
    ax.legend()

    return fig
