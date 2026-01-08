"""
Table Generator for S-Grams State Transformations

This module generates formatted tables for visualizing S-Gram
state transformations and patterns.
"""

from typing import List, Optional, Dict
from .sgram import SGram, SGramFactory
from .state_transformer import StateTransformer
from .fraction_patterns import FractionPatternAnalyzer


class StateTransformationTableGenerator:
    """
    Generates formatted tables for S-Gram state transformations.
    """
    
    def __init__(self, sgram: SGram):
        """
        Initialize with an S-Gram.
        
        Args:
            sgram: The S-Gram to generate tables for
        """
        self.sgram = sgram
        self.transformer = StateTransformer(sgram)
        self.analyzer = FractionPatternAnalyzer(sgram)
    
    def generate_basic_info_table(self) -> str:
        """
        Generate a table with basic S-Gram information.
        
        Returns:
            Formatted string table
        """
        lines = []
        lines.append("=" * 70)
        lines.append(f"S-GRAM {self.sgram.symbol.upper()} (Index {self.sgram.index})")
        lines.append("=" * 70)
        lines.append(f"Catalan Number:      [{self.sgram.catalan_number}]")
        lines.append(f"Fraction:            {self.sgram.fraction} -> {self.sgram.numerator}/{self.sgram.denominator}")
        lines.append(f"Symbolic Notation:   {self.sgram.symbolic_notation}")
        lines.append(f"Transformation:      {self.sgram.transformation}")
        lines.append(f"Formula:             {self.sgram.formula}")
        lines.append("=" * 70)
        return "\n".join(lines)
    
    def generate_fraction_patterns_table(self) -> str:
        """
        Generate a table showing all fraction patterns.
        
        Returns:
            Formatted string table
        """
        lines = []
        lines.append("\nFRACTION PATTERNS")
        lines.append("-" * 70)
        
        # Primary patterns
        if self.sgram.fraction_patterns:
            lines.append("Primary Patterns:")
            for divisor, sequence in self.sgram.fraction_patterns.items():
                seq_str = ' '.join(f"{s:3d}" for s in sequence)
                lines.append(f"  {divisor:>8s} | {seq_str}")
        
        # Additional factors
        if self.sgram.additional_factors:
            lines.append("\nAdditional Factors:")
            for divisor, sequence in self.sgram.additional_factors.items():
                seq_str = ' '.join(f"{s:3d}" for s in sequence)
                lines.append(f"  {divisor:>8s} | {seq_str}")
        
        lines.append("-" * 70)
        return "\n".join(lines)
    
    def generate_state_transition_table(self, pattern: Optional[str] = None) -> str:
        """
        Generate a table showing state transitions (previous <- current -> next).
        
        Args:
            pattern: The pattern to use. If None, uses the primary pattern.
            
        Returns:
            Formatted string table
        """
        if pattern is None:
            patterns = list(self.sgram.fraction_patterns.keys())
            if not patterns:
                return "No patterns available"
            pattern = patterns[0]
        
        transition_table = self.transformer.get_transition_table(pattern)
        
        lines = []
        lines.append(f"\nSTATE TRANSITION TABLE (Pattern: {pattern})")
        lines.append("-" * 70)
        lines.append(f"{'State':>8s} | {'Previous':>8s} | {'Next':>8s} | {'Resolving →':>15s} | {'← Informing':>15s}")
        lines.append("-" * 70)
        
        sequence = self.sgram.fraction_patterns.get(pattern) or \
                   self.sgram.additional_factors.get(pattern)
        
        if sequence:
            for state in sequence:
                prev_state, next_state = transition_table[state]
                lines.append(f"{state:8d} | {prev_state:8d} | {next_state:8d} | "
                           f"{state:5d} → {next_state:5d} | {prev_state:5d} ← {state:5d}")
        
        lines.append("-" * 70)
        return "\n".join(lines)
    
    def generate_cycle_info_table(self) -> str:
        """
        Generate a table with cycle information for all patterns.
        
        Returns:
            Formatted string table
        """
        lines = []
        lines.append("\nCYCLE INFORMATION")
        lines.append("-" * 70)
        lines.append(f"{'Pattern':>10s} | {'Cycle Length':>12s} | {'Type':>20s}")
        lines.append("-" * 70)
        
        for pattern in self.analyzer.patterns:
            pattern_type = "Primary" if pattern.is_primary else \
                          "Additional Factor" if pattern.is_additional_factor else \
                          "Standard"
            lines.append(f"{pattern.divisor:>10s} | {pattern.cycle_length:12d} | {pattern_type:>20s}")
        
        lines.append("-" * 70)
        
        # Summary
        cycle_info = self.analyzer.analyze_cycle_relationships()
        lines.append(f"\nCommon Divisor: {cycle_info['common_divisor']}")
        lines.append(f"Max Cycle: {cycle_info['max_cycle_length']}, Min Cycle: {cycle_info['min_cycle_length']}")
        
        return "\n".join(lines)
    
    def generate_complete_table(self) -> str:
        """
        Generate a complete table with all information.
        
        Returns:
            Formatted string with all tables
        """
        parts = [
            self.generate_basic_info_table(),
            self.generate_fraction_patterns_table(),
            self.generate_cycle_info_table(),
        ]
        
        # Add transition tables for primary patterns
        for pattern_name in list(self.sgram.fraction_patterns.keys())[:3]:  # Limit to first 3
            parts.append(self.generate_state_transition_table(pattern_name))
        
        return "\n".join(parts)


class AllSGramsTableGenerator:
    """
    Generates comprehensive tables for all S-Grams (0-11).
    """
    
    def __init__(self):
        """Initialize with all S-Grams"""
        self.sgrams = SGramFactory.create_all_sgrams()
        self.generators = [StateTransformationTableGenerator(sg) for sg in self.sgrams]
    
    def generate_summary_table(self) -> str:
        """
        Generate a summary table of all S-Grams.
        
        Returns:
            Formatted string table
        """
        lines = []
        lines.append("=" * 100)
        lines.append("S-GRAMS SUMMARY (0-11)")
        lines.append("=" * 100)
        lines.append(f"{'Index':>5s} | {'Symbol':>6s} | {'Catalan':>8s} | {'Fraction':>10s} | "
                    f"{'Formula Result':>14s} | {'Patterns':>8s}")
        lines.append("-" * 100)
        
        for sgram in self.sgrams:
            result = 1 + (1 + sgram.index) ** 2
            num_patterns = len(sgram.fraction_patterns) + len(sgram.additional_factors)
            lines.append(f"{sgram.index:5d} | {sgram.symbol:>6s} | {sgram.catalan_number:8d} | "
                        f"{sgram.fraction:>10s} | {result:14d} | {num_patterns:8d}")
        
        lines.append("=" * 100)
        return "\n".join(lines)
    
    def generate_all_tables(self) -> str:
        """
        Generate complete tables for all S-Grams.
        
        Returns:
            Formatted string with all tables
        """
        lines = [self.generate_summary_table(), "\n"]
        
        for generator in self.generators:
            lines.append("\n" + "=" * 100 + "\n")
            lines.append(generator.generate_complete_table())
        
        return "\n".join(lines)
    
    def generate_comparison_table(self) -> str:
        """
        Generate a comparison table showing patterns across S-Grams.
        
        Returns:
            Formatted comparison table
        """
        lines = []
        lines.append("=" * 100)
        lines.append("S-GRAMS PATTERN COMPARISON")
        lines.append("=" * 100)
        
        # Compare primary pattern cycle lengths
        lines.append("\nPrimary Pattern Cycle Lengths:")
        lines.append("-" * 100)
        for sgram in self.sgrams:
            if sgram.fraction_patterns:
                first_pattern = list(sgram.fraction_patterns.values())[0]
                cycle_len = len(first_pattern)
                divisor = list(sgram.fraction_patterns.keys())[0]
                lines.append(f"  {sgram.symbol}: {divisor} -> Cycle Length = {cycle_len}")
        
        # Compare total unique states
        lines.append("\nTotal Unique States per S-Gram:")
        lines.append("-" * 100)
        for sgram in self.sgrams:
            all_states = set()
            for seq in sgram.fraction_patterns.values():
                all_states.update(seq)
            for seq in sgram.additional_factors.values():
                all_states.update(seq)
            lines.append(f"  {sgram.symbol}: {len(all_states)} unique states")
        
        lines.append("=" * 100)
        return "\n".join(lines)


def generate_markdown_table(sgram: SGram) -> str:
    """
    Generate a Markdown-formatted table for an S-Gram.
    
    Args:
        sgram: The S-Gram to format
        
    Returns:
        Markdown formatted table string
    """
    lines = []
    lines.append(f"## S-Gram {sgram.symbol} (Index {sgram.index})")
    lines.append("")
    lines.append("### Basic Information")
    lines.append("")
    lines.append("| Property | Value |")
    lines.append("|----------|-------|")
    lines.append(f"| Catalan Number | {sgram.catalan_number} |")
    lines.append(f"| Fraction | {sgram.fraction} |")
    lines.append(f"| Formula | {sgram.formula} |")
    lines.append(f"| Symbolic Notation | {sgram.symbolic_notation} |")
    lines.append(f"| Transformation | {sgram.transformation} |")
    lines.append("")
    
    lines.append("### Fraction Patterns")
    lines.append("")
    lines.append("| Divisor | Sequence |")
    lines.append("|---------|----------|")
    
    for divisor, sequence in sgram.fraction_patterns.items():
        seq_str = ', '.join(map(str, sequence))
        lines.append(f"| {divisor} | {seq_str} |")
    
    if sgram.additional_factors:
        lines.append("")
        lines.append("### Additional Factors")
        lines.append("")
        lines.append("| Divisor | Sequence |")
        lines.append("|---------|----------|")
        for divisor, sequence in sgram.additional_factors.items():
            seq_str = ', '.join(map(str, sequence))
            lines.append(f"| {divisor} | {seq_str} |")
    
    lines.append("")
    return "\n".join(lines)


def generate_all_markdown_tables() -> str:
    """
    Generate Markdown tables for all S-Grams.
    
    Returns:
        Complete Markdown document
    """
    lines = []
    lines.append("# S-Grams State Transformation Tables")
    lines.append("")
    lines.append("Complete reference for S-Grams (2nd Power N-Grams) from 0 to 11.")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    sgrams = SGramFactory.create_all_sgrams()
    for sgram in sgrams:
        lines.append(generate_markdown_table(sgram))
        lines.append("---")
        lines.append("")
    
    return "\n".join(lines)
