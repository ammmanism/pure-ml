"""
Mathematical foundations and utilities for Pure-ML.

This module provides low-level implementations of linear algebra and probability
operations used across the library.
"""

from .linear_algebra import power_iteration, gaussian_elimination, svd
from .probability import normal_pdf, sample_normal

__all__ = [
    "power_iteration",
    "gaussian_elimination",
    "svd",
    "normal_pdf",
    "sample_normal",
]
