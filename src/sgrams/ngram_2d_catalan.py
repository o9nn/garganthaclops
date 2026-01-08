"""
2D Catalan N-Grams (Rooted Trees - OEIS A000081)

Implements rooted tree patterns representing planar surface transformations.
These are 2D extensions of the 1D Catalan numbers.

OEIS A000081: Number of rooted trees with n nodes
Sequence: 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766, ...

Applications:
- Organizational hierarchy mapping
- Decision tree pathways
- Strategic planning trees
- Hierarchical department structures
"""

from typing import Dict, List
from dataclasses import dataclass
from .ngram_base import NGramBase


@dataclass
class NGram2DCatalan(NGramBase):
    """
    Represents a 2D Catalan N-Gram (Rooted Trees).
    
    Maps to OEIS A000081: Number of rooted trees with n nodes.
    These represent hierarchical organizational structures on a planar surface.
    """
    
    @property
    def symbol(self) -> str:
        """Returns the rt-notation (rt0, rt1, etc.) for rooted trees"""
        return f"rt{self.index}"
    
    @property
    def formula(self) -> str:
        """Returns the formula description"""
        return f"A000081({self.index}) = {self.sequence_value} rooted trees"
    
    def compute_value(self, n: int) -> int:
        """
        Compute the number of rooted trees with n nodes (OEIS A000081).
        
        This uses a recursive formula based on the generating function.
        For practical purposes, we use precomputed values for n <= 20.
        """
        return NGram2DCatalanFactory.A000081_SEQUENCE[n] if n < len(NGram2DCatalanFactory.A000081_SEQUENCE) else 0
    
    def __str__(self) -> str:
        """String representation of the 2D Catalan N-Gram"""
        lines = []
        lines.append("-" * 60)
        lines.append(f"2D Catalan N-Gram (Rooted Trees): {self.symbol}")
        lines.append(f"Index: {self.index}")
        lines.append(f"Rooted Trees Count: {self.sequence_value}")
        lines.append(f"Formula: {self.formula}")
        lines.append(f"OEIS: A000081")
        lines.append("-" * 60)
        
        # Add fraction patterns if they exist
        if self.fraction_patterns:
            lines.append("\nHierarchy Patterns:")
            for divisor, pattern in self.fraction_patterns.items():
                lines.append(f"  {divisor} | {' '.join(map(str, pattern))}")
        
        if self.additional_factors:
            lines.append("\nStructural Factors:")
            for divisor, pattern in self.additional_factors.items():
                lines.append(f"  {divisor} | {' '.join(map(str, pattern))}")
        
        return "\n".join(lines)


class NGram2DCatalanFactory:
    """Factory class for creating 2D Catalan N-Gram instances (Rooted Trees)"""
    
    # OEIS A000081: Number of rooted trees with n nodes
    # https://oeis.org/A000081
    A000081_SEQUENCE = [
        0,      # n=0 (conventionally 0, some sources use 1)
        1,      # n=1
        1,      # n=2
        2,      # n=3
        4,      # n=4
        9,      # n=5
        20,     # n=6
        48,     # n=7
        115,    # n=8
        286,    # n=9
        719,    # n=10
        1842,   # n=11
        4766,   # n=12
        12486,  # n=13
        32973,  # n=14
        87811,  # n=15
        235381, # n=16
        634847, # n=17
        1721159, # n=18
        4688676, # n=19
        12826228, # n=20
    ]
    
    @staticmethod
    def _generate_tree_patterns(index: int, tree_count: int) -> Dict[str, List[int]]:
        """
        Generate hierarchy patterns for rooted trees.
        
        These patterns represent different ways to traverse or organize
        the hierarchical structure.
        """
        patterns = {}
        
        if tree_count == 0:
            return patterns
        
        # Primary pattern: all possible tree structures
        if tree_count > 0:
            patterns[f'1/{tree_count}'] = list(range(1, tree_count + 1))
        
        # For indices that have interesting factorizations
        # we add patterns for sub-hierarchies
        if tree_count > 1:
            # Find factors and create patterns
            factors = []
            for i in range(2, min(tree_count, 10) + 1):
                if tree_count % i == 0:
                    factors.append(i)
            
            for factor in factors[:3]:  # Limit to first 3 factors
                step = tree_count // factor
                patterns[f'{factor}/{tree_count}'] = list(range(factor, tree_count + 1, step))
        
        return patterns
    
    @staticmethod
    def create_ngram_2d_catalan(index: int) -> NGram2DCatalan:
        """
        Create a 2D Catalan N-Gram (Rooted Tree) for the given index.
        
        Args:
            index: The N-Gram index (0-20 supported)
            
        Returns:
            NGram2DCatalan instance
        """
        if index >= len(NGram2DCatalanFactory.A000081_SEQUENCE):
            raise ValueError(f"Index {index} exceeds supported range (0-{len(NGram2DCatalanFactory.A000081_SEQUENCE)-1})")
        
        tree_count = NGram2DCatalanFactory.A000081_SEQUENCE[index]
        fraction_patterns = NGram2DCatalanFactory._generate_tree_patterns(index, tree_count)
        
        # Additional factors represent structural properties
        additional_factors = {}
        if tree_count > 1:
            additional_factors['1/1'] = [tree_count]
        
        return NGram2DCatalan(
            index=index,
            sequence_value=tree_count,
            formula_parts={
                'rooted_trees': tree_count,
                'index': index
            },
            fraction_patterns=fraction_patterns,
            additional_factors=additional_factors
        )
    
    @classmethod
    def create_range(cls, start: int = 0, end: int = 12) -> List[NGram2DCatalan]:
        """
        Create a range of 2D Catalan N-Grams.
        
        Args:
            start: Starting index (inclusive)
            end: Ending index (exclusive)
            
        Returns:
            List of NGram2DCatalan instances
        """
        max_idx = min(end, len(cls.A000081_SEQUENCE))
        return [cls.create_ngram_2d_catalan(i) for i in range(start, max_idx)]


def get_rooted_trees_sequence(max_n: int = 20) -> List[int]:
    """
    Get the rooted trees sequence (OEIS A000081) up to max_n.
    
    Args:
        max_n: Maximum index to return
        
    Returns:
        List of rooted tree counts
        
    Examples:
        >>> seq = get_rooted_trees_sequence(10)
        >>> seq[:6]
        [0, 1, 1, 2, 4, 9]
    """
    return NGram2DCatalanFactory.A000081_SEQUENCE[:max_n + 1]
