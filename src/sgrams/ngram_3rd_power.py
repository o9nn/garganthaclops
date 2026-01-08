"""
3rd Power N-Grams (Cubic N-Grams)

Formula: N₃(n) = 1 + (1 + n)³

These represent complex cubic patterns with hierarchical depth encoding.
Applications:
- Three-dimensional organizational matrices
- Tensor organizational structures
- Multi-axis decision spaces
- Volume-based resource allocation
- Hierarchical depth encoding
"""

from typing import Dict, List
from dataclasses import dataclass
from .ngram_base import NGramBase


@dataclass
class NGram3rdPower(NGramBase):
    """
    Represents a 3rd Power N-Gram (Cubic).
    
    Formula: N₃(n) = 1 + (1 + n)³
    
    These represent complex hierarchical patterns with cubic growth.
    """
    
    @property
    def symbol(self) -> str:
        """Returns the n3-notation (n3_0, n3_1, etc.)"""
        return f"n3_{self.index}"
    
    @property
    def formula(self) -> str:
        """Returns the full formula string"""
        n = self.index
        cube = (1 + n) ** 3
        result = 1 + cube
        parts = [1, 1 + n, (1 + n) ** 2, cube]
        expansion = f"1 + (1+{n})³ = 1 + {cube} = {result}"
        return f"N₃({n}) = {expansion}"
    
    def compute_value(self, n: int) -> int:
        """Compute the 3rd power value: 1 + (1 + n)³"""
        return 1 + (1 + n) ** 3
    
    def __str__(self) -> str:
        """String representation of the 3rd Power N-Gram"""
        lines = []
        lines.append("-" * 60)
        lines.append(f"3rd Power N-Gram: {self.symbol}")
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


class NGram3rdPowerFactory:
    """Factory class for creating 3rd Power N-Gram instances"""
    
    @staticmethod
    def _generate_cubic_patterns(index: int, value: int) -> Dict[str, List[int]]:
        """
        Generate fraction patterns for cubic N-Grams.
        
        For cubic patterns, we create patterns based on the cube structure.
        The patterns are more complex than linear but follow deterministic rules.
        """
        patterns = {}
        
        # Primary pattern based on the cubic structure
        # For N₃(n) = 1 + (1+n)³, we have rich patterns
        expansion = (1 + index) ** 3
        
        # Generate pattern based on divisors of the expansion
        if expansion > 1:
            # Primary cycle includes all states
            patterns[f'1/{expansion}'] = list(range(1, expansion + 1))
        
        # Add patterns for perfect cube factors
        base = 1 + index
        if base > 1:
            # Pattern for the base value
            patterns[f'1/{base}'] = list(range(1, base + 1))
            
            # Pattern for base squared
            base_sq = base ** 2
            if base_sq != expansion:
                patterns[f'1/{base_sq}'] = list(range(1, base_sq + 1, base))
        
        return patterns
    
    @staticmethod
    def create_ngram_3rd(index: int) -> NGram3rdPower:
        """
        Create a 3rd Power N-Gram for the given index.
        
        Args:
            index: The N-Gram index (0-11 recommended for consistency)
            
        Returns:
            NGram3rdPower instance
        """
        value = 1 + (1 + index) ** 3
        expansion = (1 + index) ** 3
        
        fraction_patterns = NGram3rdPowerFactory._generate_cubic_patterns(index, value)
        
        # Additional factors based on the cube structure
        additional_factors = {}
        base = 1 + index
        if base > 1:
            additional_factors['1/1'] = [expansion]
        
        return NGram3rdPower(
            index=index,
            sequence_value=value,
            formula_parts={
                'base': 1,
                'cube_base': 1 + index,
                'expansion': expansion
            },
            fraction_patterns=fraction_patterns,
            additional_factors=additional_factors
        )
    
    @classmethod
    def create_range(cls, start: int = 0, end: int = 12) -> List[NGram3rdPower]:
        """
        Create a range of 3rd Power N-Grams.
        
        Args:
            start: Starting index (inclusive)
            end: Ending index (exclusive)
            
        Returns:
            List of NGram3rdPower instances
        """
        return [cls.create_ngram_3rd(i) for i in range(start, end)]


def compute_3rd_power_sequence(max_n: int = 20) -> List[int]:
    """
    Compute the 3rd power sequence up to max_n.
    
    Args:
        max_n: Maximum index to compute
        
    Returns:
        List of 3rd power values
        
    Examples:
        >>> seq = compute_3rd_power_sequence(5)
        >>> seq
        [2, 9, 28, 65, 126]
    """
    return [1 + (1 + n) ** 3 for n in range(max_n)]
