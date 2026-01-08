"""
Base classes for N-Grams (1st, 2nd, 3rd power and Catalan extensions).

This module provides the foundation for all N-Gram types including:
- 1st Power (Linear)
- 2nd Power (Quadratic - S-Grams)
- 3rd Power (Cubic)
- 2D Catalan (Rooted Trees - OEIS A000081)
- 3D Catalan (Trees - OEIS A000055)
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class NGramBase(ABC):
    """
    Abstract base class for all N-Gram types.
    
    Attributes:
        index: The N-Gram index
        sequence_value: The value from the relevant sequence (Catalan, etc.)
        formula_parts: Parts of the formula calculation
        fraction_patterns: Dictionary mapping divisors to sequence patterns
        additional_factors: Optional additional factor patterns
    """
    index: int
    sequence_value: int
    formula_parts: Dict[str, int]
    fraction_patterns: Dict[str, List[int]] = field(default_factory=dict)
    additional_factors: Dict[str, List[int]] = field(default_factory=dict)
    
    @property
    @abstractmethod
    def symbol(self) -> str:
        """Returns the symbolic notation"""
        pass
    
    @property
    @abstractmethod
    def formula(self) -> str:
        """Returns the full formula string"""
        pass
    
    @abstractmethod
    def compute_value(self, n: int) -> int:
        """Compute the N-Gram value for index n"""
        pass
    
    def get_state_sequence(self, divisor: Optional[str] = None) -> List[int]:
        """
        Get the state sequence for a specific divisor.
        
        Args:
            divisor: The divisor key (e.g., '1/3', '1/7'). If None, returns primary pattern.
            
        Returns:
            List of integers representing the state sequence
        """
        if divisor is None:
            if self.fraction_patterns:
                return list(self.fraction_patterns.values())[0]
            return []
        return self.fraction_patterns.get(divisor, [])
    
    def get_all_patterns(self) -> Dict[str, List[int]]:
        """Returns all fraction patterns including additional factors"""
        all_patterns = dict(self.fraction_patterns)
        all_patterns.update(self.additional_factors)
        return all_patterns
    
    def _gcd(self, a: int, b: int) -> int:
        """Calculate greatest common divisor"""
        while b:
            a, b = b, a % b
        return a
