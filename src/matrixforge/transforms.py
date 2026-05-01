"""
Matrix transformation utilities for 2D and 3D operations.
"""

import numpy as np


def rotation_matrix_2d(angle: float, degrees: bool = False) -> np.ndarray:
    """
    Create a 2D rotation matrix.

    Parameters
    ----------
    angle : float
        Rotation angle
    degrees : bool
        If True, angle is in degrees. Otherwise radians.

    Returns
    -------
    R : np.ndarray
        2x2 rotation matrix
    """
    if degrees:
        angle = np.deg2rad(angle)

    c = np.cos(angle)
    s = np.sin(angle)

    return np.array([
        [c, -s],
        [s, c]
    ])


def scaling_matrix_2d(sx: float, sy: float) -> np.ndarray:
    """
    Create a 2D scaling matrix.

    Parameters
    ----------
    sx : float
        Scaling factor in x direction
    sy : float
        Scaling factor in y direction

    Returns
    -------
    S : np.ndarray
        2x2 scaling matrix
    """
    return np.array([
        [sx, 0],
        [0, sy]
    ])


def translation_matrix_3d(tx: float, ty: float, tz: float = 0) -> np.ndarray:
    """
    Create a 3D translation matrix using homogeneous coordinates.

    Parameters
    ----------
    tx : float
        Translation in x direction
    ty : float
        Translation in y direction
    tz : float
        Translation in z direction

    Returns
    -------
    T : np.ndarray
        4x4 translation matrix
    """
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])


def rotation_matrix_3d_z(angle: float, degrees: bool = False) -> np.ndarray:
    """
    Create a 3D rotation matrix around the z-axis (homogeneous coordinates).

    Parameters
    ----------
    angle : float
        Rotation angle
    degrees : bool
        If True, angle is in degrees. Otherwise radians.

    Returns
    -------
    R : np.ndarray
        4x4 rotation matrix
    """
    if degrees:
        angle = np.deg2rad(angle)

    c = np.cos(angle)
    s = np.sin(angle)

    return np.array([
        [c, -s, 0, 0],
        [s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def rotation_matrix_3d_x(angle: float, degrees: bool = False) -> np.ndarray:
    """
    Create a 3D rotation matrix around the x-axis (homogeneous coordinates).

    Parameters
    ----------
    angle : float
        Rotation angle
    degrees : bool
        If True, angle is in degrees. Otherwise radians.

    Returns
    -------
    R : np.ndarray
        4x4 rotation matrix
    """
    if degrees:
        angle = np.deg2rad(angle)

    c = np.cos(angle)
    s = np.sin(angle)

    return np.array([
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s, c, 0],
        [0, 0, 0, 1]
    ])


def rotation_matrix_3d_y(angle: float, degrees: bool = False) -> np.ndarray:
    """
    Create a 3D rotation matrix around the y-axis (homogeneous coordinates).

    Parameters
    ----------
    angle : float
        Rotation angle
    degrees : bool
        If True, angle is in degrees. Otherwise radians.

    Returns
    -------
    R : np.ndarray
        4x4 rotation matrix
    """
    if degrees:
        angle = np.deg2rad(angle)

    c = np.cos(angle)
    s = np.sin(angle)

    return np.array([
        [c, 0, s, 0],
        [0, 1, 0, 0],
        [-s, 0, c, 0],
        [0, 0, 0, 1]
    ])
