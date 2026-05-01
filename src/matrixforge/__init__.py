"""
MatrixForge: Interactive learning tools for matrix mathematics.

This package provides utility functions for visualizing and working with
matrices in educational contexts.
"""

__version__ = "0.1.0"

from .plotting import plot_vector_2d, plot_transformation_2d
from .transforms import rotation_matrix_2d, scaling_matrix_2d, translation_matrix_3d

__all__ = [
    "plot_vector_2d",
    "plot_transformation_2d",
    "rotation_matrix_2d",
    "scaling_matrix_2d",
    "translation_matrix_3d",
]
