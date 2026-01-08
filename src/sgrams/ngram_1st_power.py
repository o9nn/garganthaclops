"""
1st Power N-Grams (Linear N-Grams)

Formula: N₁(n) = 1 + (1 + n)

These represent simple linear progressions with minimal complexity.
Applications:
- Simple linear workflows
- Sequential processes
- Single-threaded execution
- Basic state machines
"""

from typing import Dict, List
from dataclasses import dataclass
from .ngram_base import NGramBase


@dataclass
class NGram1stPower(NGramBase):
    """
    Represents a 1st Power N-Gram (Linear).
    
    Formula: N₁(n) = 1 + (1 + n) = 2 + n
    
    These represent the simplest N-Gram patterns with linear growth.
    """
    
    @property
    def symbol(self) -> str:
        """Returns the n1-notation (n1_0, n1_1, etc.)"""
        return f"n1_{self.index}"
    
    @property
    def formula(self) -> str:
        """Returns the full formula string"""
        n = self.index
        result = 1 + (1 + n)
        return f"N₁({n}) = 1 + (1 + {n}) = {result}"
    
    def compute_value(self, n: int) -> int:
        """Compute the 1st power value: 1 + (1 + n)"""
        return 1 + (1 + n)
    
    def __str__(self) -> str:
        """String representation of the 1st Power N-Gram"""
        lines = []
        lines.append("-" * 60)
        lines.append(f"1st Power N-Gram: {self.symbol}")
        lines.append(f"Index: {self.index}")
        lines.append(f"Value: {self.sequence_value}")
        lines.append(f"Formula: {self.formula}")
        lines.append("-" * 60)
        
        # Add fraction patterns if they exist
        if self.fraction_patterns:
            lines.append("\nFraction Patterns:")
            for divisor, pattern in self.fraction_patterns.items():
                lines.append(f"  {divisor} | {' '.join(map(str, pattern))}")
        
        if self.additional_factors:
            lines.append("\nAdditional Factors:")
            for divisor, pattern in self.additional_factors.items():
                lines.append(f"  {divisor} | {' '.join(map(str, pattern))}")
        
        return "\n".join(lines)


class NGram1stPowerFactory:
    """Factory class for creating 1st Power N-Gram instances"""
    
    @staticmethod
    def create_ngram_1st(index: int) -> NGram1stPower:
        """
        Create a 1st Power N-Gram for the given index.
        
        Args:
            index: The N-Gram index (0-11 recommended for consistency)
            
        Returns:
            NGram1stPower instance
        """
        value = 1 + (1 + index)
        
        # For 1st power, patterns are very simple
        # The value itself forms a trivial cycle
        fraction_patterns = {
            f'1/{value}': list(range(1, value + 1))
        }
        
        return NGram1stPower(
            index=index,
            sequence_value=value,
            formula_parts={'base': 1, 'increment': 1 + index},
            fraction_patterns=fraction_patterns,
            additional_factors={}
        )
    
    @classmethod
    def create_range(cls, start: int = 0, end: int = 12) -> List[NGram1stPower]:
        """
        Create a range of 1st Power N-Grams.
        
        Args:
            start: Starting index (inclusive)
            end: Ending index (exclusive)
            
        Returns:
            List of NGram1stPower instances
        """
        return [cls.create_ngram_1st(i) for i in range(start, end)]


def compute_1st_power_sequence(max_n: int = 20) -> List[int]:
    """
    Compute the 1st power sequence up to max_n.
    
    Args:
        max_n: Maximum index to compute
        
    Returns:
        List of 1st power values
    """
    return [1 + (1 + n) for n in range(max_n)]
