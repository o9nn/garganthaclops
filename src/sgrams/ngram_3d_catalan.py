"""
3D Catalan N-Grams (Trees with Flip Transform - OEIS A000055)

Implements symmetric tree patterns with flip transform for clustering under symmetry.
These are 3D extensions representing spherical surface mappings.

OEIS A000055: Number of unlabeled trees with n nodes
Sequence: 1, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, ...

Applications:
- Network structures with symmetry
- Peer-to-peer coordination
- Matrix organizations
- Cross-functional teams
- Symmetric organizational patterns
"""

from typing import Dict, List, Set
from dataclasses import dataclass
from .ngram_base import NGramBase


@dataclass
class NGram3DCatalan(NGramBase):
    """
    Represents a 3D Catalan N-Gram (Unlabeled Trees with Flip Transform).
    
    Maps to OEIS A000055: Number of unlabeled trees with n nodes.
    These represent symmetric network structures on a spherical surface.
    """
    
    @property
    def symbol(self) -> str:
        """Returns the ut-notation (ut0, ut1, etc.) for unlabeled trees"""
        return f"ut{self.index}"
    
    @property
    def formula(self) -> str:
        """Returns the formula description"""
        return f"A000055({self.index}) = {self.sequence_value} unlabeled trees"
    
    def compute_value(self, n: int) -> int:
        """
        Compute the number of unlabeled trees with n nodes (OEIS A000055).
        
        This accounts for symmetry via the flip transform.
        For practical purposes, we use precomputed values for n <= 20.
        """
        return NGram3DCatalanFactory.A000055_SEQUENCE[n] if n < len(NGram3DCatalanFactory.A000055_SEQUENCE) else 0
    
    def __str__(self) -> str:
        """String representation of the 3D Catalan N-Gram"""
        lines = []
        lines.append("-" * 60)
        lines.append(f"3D Catalan N-Gram (Unlabeled Trees): {self.symbol}")
        lines.append(f"Index: {self.index}")
        lines.append(f"Unlabeled Trees Count: {self.sequence_value}")
        lines.append(f"Formula: {self.formula}")
        lines.append(f"OEIS: A000055")
        lines.append(f"Note: Accounts for symmetry via flip transform")
        lines.append("-" * 60)
        
        # Add fraction patterns if they exist
        if self.fraction_patterns:
            lines.append("\nSymmetric Network Patterns:")
            for divisor, pattern in self.fraction_patterns.items():
                lines.append(f"  {divisor} | {' '.join(map(str, pattern))}")
        
        if self.additional_factors:
            lines.append("\nSymmetry Factors:")
            for divisor, pattern in self.additional_factors.items():
                lines.append(f"  {divisor} | {' '.join(map(str, pattern))}")
        
        return "\n".join(lines)


class FlipTransform:
    """
    Flip transform for clustering patterns under symmetry.
    
    The flip transform identifies equivalent structures under graph isomorphism,
    reducing the state space for symmetric organizational patterns.
    """
    
    @staticmethod
    def apply_flip(pattern: List[int]) -> List[int]:
        """
        Apply flip transform to create equivalence class.
        
        For organizational structures, this represents:
        - Role symmetry (interchangeable positions)
        - Geographic symmetry (identical regional structures)
        - Temporal symmetry (repeating patterns)
        
        Args:
            pattern: Input pattern to transform
            
        Returns:
            Canonical form of the pattern under flip
        """
        # Simple flip: reverse and return minimum lexicographic order
        reversed_pattern = list(reversed(pattern))
        return min(pattern, reversed_pattern)
    
    @staticmethod
    def cluster_by_symmetry(patterns: List[List[int]]) -> Dict[str, List[List[int]]]:
        """
        Cluster patterns that are equivalent under flip.
        
        Args:
            patterns: List of patterns to cluster
            
        Returns:
            Dictionary mapping canonical forms to equivalent patterns
        """
        clusters = {}
        
        for pattern in patterns:
            canonical = tuple(FlipTransform.apply_flip(pattern))
            if canonical not in clusters:
                clusters[canonical] = []
            clusters[canonical].append(pattern)
        
        return {str(k): v for k, v in clusters.items()}


class NGram3DCatalanFactory:
    """Factory class for creating 3D Catalan N-Gram instances (Unlabeled Trees)"""
    
    # OEIS A000055: Number of unlabeled trees with n nodes
    # https://oeis.org/A000055
    A000055_SEQUENCE = [
        1,      # n=0 (empty tree)
        1,      # n=1
        1,      # n=2
        1,      # n=3
        2,      # n=4
        3,      # n=5
        6,      # n=6
        11,     # n=7
        23,     # n=8
        47,     # n=9
        106,    # n=10
        235,    # n=11
        551,    # n=12
        1301,   # n=13
        3159,   # n=14
        7741,   # n=15
        19320,  # n=16
        48629,  # n=17
        123867, # n=18
        317955, # n=19
        823065, # n=20
    ]
    
    @staticmethod
    def _generate_symmetric_patterns(index: int, tree_count: int) -> Dict[str, List[int]]:
        """
        Generate symmetric network patterns for unlabeled trees.
        
        These patterns account for symmetry and represent different
        ways to organize symmetric team structures.
        """
        patterns = {}
        
        if tree_count == 0:
            patterns['1/1'] = [0]
            return patterns
        
        # Primary pattern: all symmetric structures
        if tree_count > 0:
            patterns[f'1/{tree_count}'] = list(range(1, tree_count + 1))
        
        # For symmetric structures, we often have fewer patterns
        # due to equivalence under flip transform
        if tree_count > 1:
            # Generate patterns that respect symmetry
            half = (tree_count + 1) // 2
            if half > 1:
                # Pattern representing symmetric pairs
                patterns[f'1/{half}'] = list(range(1, tree_count + 1, 2))
        
        return patterns
    
    @staticmethod
    def create_ngram_3d_catalan(index: int) -> NGram3DCatalan:
        """
        Create a 3D Catalan N-Gram (Unlabeled Tree) for the given index.
        
        Args:
            index: The N-Gram index (0-20 supported)
            
        Returns:
            NGram3DCatalan instance
        """
        if index >= len(NGram3DCatalanFactory.A000055_SEQUENCE):
            raise ValueError(f"Index {index} exceeds supported range (0-{len(NGram3DCatalanFactory.A000055_SEQUENCE)-1})")
        
        tree_count = NGram3DCatalanFactory.A000055_SEQUENCE[index]
        fraction_patterns = NGram3DCatalanFactory._generate_symmetric_patterns(index, tree_count)
        
        # Additional factors represent symmetry properties
        additional_factors = {}
        if tree_count > 1:
            additional_factors['1/1'] = [tree_count]
        elif tree_count == 1:
            additional_factors['1/1'] = [1]
        
        return NGram3DCatalan(
            index=index,
            sequence_value=tree_count,
            formula_parts={
                'unlabeled_trees': tree_count,
                'index': index,
                'symmetry': 'flip_transform'
            },
            fraction_patterns=fraction_patterns,
            additional_factors=additional_factors
        )
    
    @classmethod
    def create_range(cls, start: int = 0, end: int = 12) -> List[NGram3DCatalan]:
        """
        Create a range of 3D Catalan N-Grams.
        
        Args:
            start: Starting index (inclusive)
            end: Ending index (exclusive)
            
        Returns:
            List of NGram3DCatalan instances
        """
        max_idx = min(end, len(cls.A000055_SEQUENCE))
        return [cls.create_ngram_3d_catalan(i) for i in range(start, max_idx)]


def get_unlabeled_trees_sequence(max_n: int = 20) -> List[int]:
    """
    Get the unlabeled trees sequence (OEIS A000055) up to max_n.
    
    Args:
        max_n: Maximum index to return
        
    Returns:
        List of unlabeled tree counts
        
    Examples:
        >>> seq = get_unlabeled_trees_sequence(10)
        >>> seq[:6]
        [1, 1, 1, 1, 2, 3]
    """
    return NGram3DCatalanFactory.A000055_SEQUENCE[:max_n + 1]
