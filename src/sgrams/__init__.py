"""
N-Grams Module

This module implements state transformation tables for various N-Gram orders:
- 1st Power N-Grams (Linear): N₁(n) = 1 + (1 + n)
- 2nd Power N-Grams (S-Grams/Quadratic): N₂(n) = 1 + (1 + n)²
- 3rd Power N-Grams (Cubic): N₃(n) = 1 + (1 + n)³
- 2D Catalan (Rooted Trees - OEIS A000081)
- 3D Catalan (Unlabeled Trees - OEIS A000055)
"""

from .sgram import SGram
from .state_transformer import StateTransformer
from .fraction_patterns import FractionPattern
from .ngram_base import NGramBase
from .ngram_1st_power import NGram1stPower, NGram1stPowerFactory
from .ngram_3rd_power import NGram3rdPower, NGram3rdPowerFactory
from .ngram_2d_catalan import NGram2DCatalan, NGram2DCatalanFactory
from .ngram_3d_catalan import NGram3DCatalan, NGram3DCatalanFactory, FlipTransform

__all__ = [
    # 2nd Power (S-Grams - existing)
    'SGram',
    'StateTransformer',
    'FractionPattern',
    # Base classes
    'NGramBase',
    # 1st Power
    'NGram1stPower',
    'NGram1stPowerFactory',
    # 3rd Power
    'NGram3rdPower',
    'NGram3rdPowerFactory',
    # 2D Catalan
    'NGram2DCatalan',
    'NGram2DCatalanFactory',
    # 3D Catalan
    'NGram3DCatalan',
    'NGram3DCatalanFactory',
    'FlipTransform',
]
