"""
S-Grams (2nd Power N-Grams) Module

This module implements state transformation tables for S-Grams,
which represent "Resolving" and "Informing" patterns for 2nd power N-Grams
from 0 through 11.

S-Grams follow the formula: 1 + (1 + (n-1))^2
"""

from .sgram import SGram
from .state_transformer import StateTransformer
from .fraction_patterns import FractionPattern

__all__ = ['SGram', 'StateTransformer', 'FractionPattern']
