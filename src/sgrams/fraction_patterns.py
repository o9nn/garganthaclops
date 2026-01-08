"""
Fraction Pattern Analysis for S-Grams

This module provides tools for analyzing the fraction patterns
that emerge in S-Grams and their relationships.
"""

from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from .sgram import SGram


@dataclass
class FractionPattern:
    """
    Represents a fraction pattern within an S-Gram.
    
    Attributes:
        divisor: The divisor notation (e.g., '1/3', '2/13')
        sequence: The state sequence
        cycle_length: Length of the cycle
        is_primary: Whether this is the primary pattern
        is_additional_factor: Whether this is an additional factor
    """
    divisor: str
    sequence: List[int]
    cycle_length: int
    is_primary: bool = False
    is_additional_factor: bool = False
    
    @property
    def numerator(self) -> int:
        """Extract numerator from divisor string"""
        return int(self.divisor.split('/')[0])
    
    @property
    def denominator(self) -> int:
        """Extract denominator from divisor string"""
        return int(self.divisor.split('/')[1])
    
    def contains_state(self, state: int) -> bool:
        """Check if a state is in this pattern's sequence"""
        return state in self.sequence
    
    def get_state_index(self, state: int) -> Optional[int]:
        """Get the index of a state in the sequence, or None if not found"""
        try:
            return self.sequence.index(state)
        except ValueError:
            return None
    
    def __str__(self) -> str:
        """String representation"""
        seq_str = ' '.join(map(str, self.sequence))
        flag = " (primary)" if self.is_primary else " (additional)" if self.is_additional_factor else ""
        return f"{self.divisor} | {seq_str}{flag}"


class FractionPatternAnalyzer:
    """
    Analyzes fraction patterns across S-Grams.
    """
    
    def __init__(self, sgram: SGram):
        """
        Initialize the analyzer with an S-Gram.
        
        Args:
            sgram: The S-Gram to analyze
        """
        self.sgram = sgram
        self.patterns = self._extract_patterns()
    
    def _extract_patterns(self) -> List[FractionPattern]:
        """Extract all fraction patterns from the S-Gram"""
        patterns = []
        
        # Extract primary fraction patterns
        for i, (divisor, sequence) in enumerate(self.sgram.fraction_patterns.items()):
            patterns.append(FractionPattern(
                divisor=divisor,
                sequence=sequence,
                cycle_length=len(sequence),
                is_primary=(i == 0)
            ))
        
        # Extract additional factors
        for divisor, sequence in self.sgram.additional_factors.items():
            patterns.append(FractionPattern(
                divisor=divisor,
                sequence=sequence,
                cycle_length=len(sequence),
                is_additional_factor=True
            ))
        
        return patterns
    
    def get_primary_pattern(self) -> Optional[FractionPattern]:
        """Get the primary fraction pattern"""
        for pattern in self.patterns:
            if pattern.is_primary:
                return pattern
        return None
    
    def get_patterns_containing_state(self, state: int) -> List[FractionPattern]:
        """Get all patterns that contain a specific state"""
        return [p for p in self.patterns if p.contains_state(state)]
    
    def get_pattern_by_divisor(self, divisor: str) -> Optional[FractionPattern]:
        """Get a pattern by its divisor notation"""
        for pattern in self.patterns:
            if pattern.divisor == divisor:
                return pattern
        return None
    
    def get_all_states(self) -> set:
        """Get all unique states across all patterns"""
        states = set()
        for pattern in self.patterns:
            states.update(pattern.sequence)
        return states
    
    def get_pattern_overlap(self, divisor1: str, divisor2: str) -> List[int]:
        """
        Get the states that appear in both patterns.
        
        Args:
            divisor1: First pattern divisor
            divisor2: Second pattern divisor
            
        Returns:
            List of states that appear in both patterns
        """
        pattern1 = self.get_pattern_by_divisor(divisor1)
        pattern2 = self.get_pattern_by_divisor(divisor2)
        
        if not pattern1 or not pattern2:
            return []
        
        set1 = set(pattern1.sequence)
        set2 = set(pattern2.sequence)
        
        return sorted(set1 & set2)
    
    def analyze_cycle_relationships(self) -> Dict[str, any]:
        """
        Analyze relationships between cycle lengths.
        
        Returns:
            Dictionary with analysis results
        """
        cycle_lengths = {p.divisor: p.cycle_length for p in self.patterns}
        
        # Find GCD of all cycle lengths
        from math import gcd
        from functools import reduce
        
        lengths = list(cycle_lengths.values())
        if lengths:
            common_divisor = reduce(gcd, lengths)
        else:
            common_divisor = 1
        
        return {
            'cycle_lengths': cycle_lengths,
            'common_divisor': common_divisor,
            'max_cycle_length': max(lengths) if lengths else 0,
            'min_cycle_length': min(lengths) if lengths else 0,
            'total_patterns': len(self.patterns)
        }
    
    def get_state_distribution(self) -> Dict[int, int]:
        """
        Get the distribution of states across patterns.
        
        Returns:
            Dictionary mapping state -> number of patterns containing it
        """
        distribution = {}
        for pattern in self.patterns:
            for state in pattern.sequence:
                distribution[state] = distribution.get(state, 0) + 1
        return distribution
    
    def find_unique_states(self) -> Dict[str, List[int]]:
        """
        Find states that are unique to each pattern.
        
        Returns:
            Dictionary mapping divisor -> list of unique states
        """
        unique = {}
        all_states = [set(p.sequence) for p in self.patterns]
        
        for i, pattern in enumerate(self.patterns):
            # States in this pattern
            pattern_states = set(pattern.sequence)
            
            # States in all other patterns
            other_states = set()
            for j, other_set in enumerate(all_states):
                if i != j:
                    other_states.update(other_set)
            
            # Unique to this pattern
            unique[pattern.divisor] = sorted(pattern_states - other_states)
        
        return unique
    
    def generate_summary(self) -> str:
        """
        Generate a summary of the fraction patterns.
        
        Returns:
            Multi-line string with pattern analysis
        """
        lines = []
        lines.append(f"S-Gram {self.sgram.symbol} Fraction Pattern Analysis")
        lines.append("=" * 60)
        lines.append(f"Total Patterns: {len(self.patterns)}")
        lines.append(f"Total Unique States: {len(self.get_all_states())}")
        lines.append("")
        
        # Primary pattern
        primary = self.get_primary_pattern()
        if primary:
            lines.append(f"Primary Pattern: {primary}")
            lines.append("")
        
        # All patterns
        lines.append("All Patterns:")
        for pattern in self.patterns:
            lines.append(f"  {pattern}")
        lines.append("")
        
        # Cycle analysis
        cycle_info = self.analyze_cycle_relationships()
        lines.append("Cycle Analysis:")
        lines.append(f"  Common Divisor: {cycle_info['common_divisor']}")
        lines.append(f"  Max Cycle Length: {cycle_info['max_cycle_length']}")
        lines.append(f"  Min Cycle Length: {cycle_info['min_cycle_length']}")
        lines.append("")
        
        # State distribution
        dist = self.get_state_distribution()
        multi_pattern_states = {s: c for s, c in dist.items() if c > 1}
        if multi_pattern_states:
            lines.append("States appearing in multiple patterns:")
            for state, count in sorted(multi_pattern_states.items()):
                patterns = [p.divisor for p in self.get_patterns_containing_state(state)]
                lines.append(f"  State {state}: {count} patterns ({', '.join(patterns)})")
        
        return "\n".join(lines)


class CrossSGramAnalyzer:
    """
    Analyzes patterns across multiple S-Grams.
    """
    
    def __init__(self, sgrams: List[SGram]):
        """
        Initialize with a list of S-Grams.
        
        Args:
            sgrams: List of S-Grams to analyze
        """
        self.sgrams = sorted(sgrams, key=lambda s: s.index)
        self.analyzers = {sg.index: FractionPatternAnalyzer(sg) for sg in sgrams}
    
    def compare_primary_patterns(self) -> Dict[int, Dict]:
        """
        Compare primary patterns across S-Grams.
        
        Returns:
            Dictionary with comparison data
        """
        comparison = {}
        for sgram in self.sgrams:
            analyzer = self.analyzers[sgram.index]
            primary = analyzer.get_primary_pattern()
            if primary:
                comparison[sgram.index] = {
                    'divisor': primary.divisor,
                    'cycle_length': primary.cycle_length,
                    'sequence': primary.sequence
                }
        return comparison
    
    def find_common_patterns(self) -> List[Tuple[str, List[int]]]:
        """
        Find divisor patterns that appear in multiple S-Grams.
        
        Returns:
            List of (divisor, [sgram_indices]) tuples
        """
        divisor_to_sgrams = {}
        
        for sgram in self.sgrams:
            analyzer = self.analyzers[sgram.index]
            for pattern in analyzer.patterns:
                divisor = pattern.divisor
                if divisor not in divisor_to_sgrams:
                    divisor_to_sgrams[divisor] = []
                divisor_to_sgrams[divisor].append(sgram.index)
        
        # Filter to only patterns appearing in multiple S-Grams
        common = [(d, indices) for d, indices in divisor_to_sgrams.items() 
                 if len(indices) > 1]
        
        return sorted(common, key=lambda x: len(x[1]), reverse=True)
    
    def analyze_growth_pattern(self) -> Dict[str, List[int]]:
        """
        Analyze how pattern properties grow across S-Grams.
        
        Returns:
            Dictionary with growth data
        """
        return {
            'catalan_numbers': [sg.catalan_number for sg in self.sgrams],
            'denominators': [sg.denominator for sg in self.sgrams],
            'formula_expansions': [sg.formula_parts['expansion'] for sg in self.sgrams],
            'total_states': [len(self.analyzers[sg.index].get_all_states()) 
                           for sg in self.sgrams]
        }
