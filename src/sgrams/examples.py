"""
Example usage of the S-Grams module.

This file demonstrates how to use the S-Grams state transformation system.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from sgrams.sgram import SGramFactory
from sgrams.state_transformer import StateTransformer, MultiPatternTransformer
from sgrams.fraction_patterns import FractionPatternAnalyzer, CrossSGramAnalyzer
from sgrams.table_generator import StateTransformationTableGenerator, AllSGramsTableGenerator


def example_basic_usage():
    """Basic usage: creating and displaying an S-Gram"""
    print("=" * 80)
    print("EXAMPLE 1: Basic S-Gram Usage")
    print("=" * 80)
    
    # Create S-Gram 3 (index 3)
    sgram = SGramFactory.create_sgram(3)
    
    print(f"\nS-Gram Symbol: {sgram.symbol}")
    print(f"Catalan Number: {sgram.catalan_number}")
    print(f"Fraction: {sgram.fraction}")
    print(f"Formula: {sgram.formula}")
    print(f"\nSymbolic: {sgram.symbolic_notation}")
    print(f"Transform: {sgram.transformation}")
    
    print("\nFraction Patterns:")
    for divisor, sequence in sgram.fraction_patterns.items():
        print(f"  {divisor}: {sequence}")


def example_state_transitions():
    """Example: State transitions with resolving and informing"""
    print("\n" + "=" * 80)
    print("EXAMPLE 2: State Transitions (Resolving & Informing)")
    print("=" * 80)
    
    sgram = SGramFactory.create_sgram(3)
    transformer = StateTransformer(sgram)
    
    # Start with state 1
    current_state = 1
    pattern = '1/7'
    
    print(f"\nStarting at state {current_state} in pattern {pattern}")
    
    # Resolve (move forward) 5 times
    print("\nResolving (forward):")
    for i in range(5):
        next_state = transformer.resolve(current_state, pattern)
        print(f"  Step {i+1}: {current_state} → {next_state}")
        current_state = next_state
    
    # Inform (move backward) 3 times
    print("\nInforming (backward):")
    for i in range(3):
        prev_state = transformer.inform(current_state, pattern)
        print(f"  Step {i+1}: {prev_state} ← {current_state}")
        current_state = prev_state


def example_path_tracing():
    """Example: Tracing a path through state space"""
    print("\n" + "=" * 80)
    print("EXAMPLE 3: Path Tracing")
    print("=" * 80)
    
    sgram = SGramFactory.create_sgram(4)
    transformer = StateTransformer(sgram)
    
    # Trace forward path
    forward_path = transformer.trace_path(1, 10, pattern='1/13', reverse=False)
    print(f"\nForward path from state 1 (10 steps, pattern 1/13):")
    print(f"  {' → '.join(map(str, forward_path))}")
    
    # Trace backward path
    backward_path = transformer.trace_path(13, 8, pattern='1/13', reverse=True)
    print(f"\nBackward path from state 13 (8 steps, pattern 1/13):")
    print(f"  {' ← '.join(map(str, backward_path))}")


def example_pattern_analysis():
    """Example: Analyzing fraction patterns"""
    print("\n" + "=" * 80)
    print("EXAMPLE 4: Pattern Analysis")
    print("=" * 80)
    
    sgram = SGramFactory.create_sgram(5)
    analyzer = FractionPatternAnalyzer(sgram)
    
    print(f"\nAnalyzing S-Gram {sgram.symbol}:")
    
    # Get primary pattern
    primary = analyzer.get_primary_pattern()
    print(f"\nPrimary Pattern: {primary.divisor}")
    print(f"  Sequence: {primary.sequence}")
    print(f"  Cycle Length: {primary.cycle_length}")
    
    # Get all states
    all_states = analyzer.get_all_states()
    print(f"\nTotal Unique States: {len(all_states)}")
    
    # State distribution
    distribution = analyzer.get_state_distribution()
    multi_pattern_states = {s: c for s, c in distribution.items() if c > 1}
    print(f"\nStates in multiple patterns: {len(multi_pattern_states)}")
    for state, count in sorted(multi_pattern_states.items())[:5]:
        patterns = [p.divisor for p in analyzer.get_patterns_containing_state(state)]
        print(f"  State {state}: {count} patterns ({', '.join(patterns)})")


def example_table_generation():
    """Example: Generating formatted tables"""
    print("\n" + "=" * 80)
    print("EXAMPLE 5: Table Generation")
    print("=" * 80)
    
    # Generate table for a single S-Gram
    sgram = SGramFactory.create_sgram(2)
    generator = StateTransformationTableGenerator(sgram)
    
    print(generator.generate_basic_info_table())
    print(generator.generate_fraction_patterns_table())
    print(generator.generate_cycle_info_table())


def example_cross_sgram_analysis():
    """Example: Analyzing patterns across multiple S-Grams"""
    print("\n" + "=" * 80)
    print("EXAMPLE 6: Cross S-Gram Analysis")
    print("=" * 80)
    
    # Create several S-Grams
    sgrams = [SGramFactory.create_sgram(i) for i in range(6)]
    analyzer = CrossSGramAnalyzer(sgrams)
    
    # Compare primary patterns
    print("\nPrimary Pattern Comparison:")
    comparison = analyzer.compare_primary_patterns()
    for idx, data in comparison.items():
        print(f"  S-Gram {idx}: {data['divisor']} (cycle length: {data['cycle_length']})")
    
    # Find common patterns
    print("\nCommon Patterns Across S-Grams:")
    common = analyzer.find_common_patterns()
    for divisor, sgram_indices in common[:5]:
        print(f"  {divisor}: appears in S-Grams {sgram_indices}")
    
    # Analyze growth
    print("\nGrowth Analysis:")
    growth = analyzer.analyze_growth_pattern()
    print(f"  Catalan Numbers: {growth['catalan_numbers']}")
    print(f"  Formula Expansions: {growth['formula_expansions']}")


def example_all_sgrams_summary():
    """Example: Summary of all S-Grams"""
    print("\n" + "=" * 80)
    print("EXAMPLE 7: All S-Grams Summary")
    print("=" * 80)
    
    generator = AllSGramsTableGenerator()
    print(generator.generate_summary_table())


def example_multi_pattern_transformer():
    """Example: Multi-pattern transformations"""
    print("\n" + "=" * 80)
    print("EXAMPLE 8: Multi-Pattern Transformations")
    print("=" * 80)
    
    sgram = SGramFactory.create_sgram(6)
    multi_transformer = MultiPatternTransformer(sgram)
    
    # Find patterns containing state 6
    patterns = multi_transformer.get_pattern_for_state(6)
    print(f"\nState 6 appears in patterns: {patterns}")
    
    # Try cross-pattern transition
    if len(patterns) >= 2:
        from_pattern = patterns[0]
        to_pattern = patterns[1]
        result = multi_transformer.cross_pattern_transition(6, from_pattern, to_pattern)
        print(f"\nCross-pattern transition from {from_pattern} to {to_pattern}:")
        print(f"  State 6 in {from_pattern} → State {result} in {to_pattern}")


def main():
    """Run all examples"""
    print("\n" + "#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + "  S-GRAMS STATE TRANSFORMATION EXAMPLES".center(78) + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)
    
    examples = [
        example_basic_usage,
        example_state_transitions,
        example_path_tracing,
        example_pattern_analysis,
        example_table_generation,
        example_cross_sgram_analysis,
        example_all_sgrams_summary,
        example_multi_pattern_transformer,
    ]
    
    for example_func in examples:
        try:
            example_func()
        except Exception as e:
            print(f"\nError in {example_func.__name__}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "#" * 80)
    print("# Examples completed")
    print("#" * 80)


if __name__ == '__main__':
    main()
