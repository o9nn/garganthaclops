#!/usr/bin/env python3
"""
S-Grams CLI Tool

Command-line interface for exploring S-Gram state transformations.

Usage:
    python sgrams_cli.py summary                    # Show summary of all S-Grams
    python sgrams_cli.py show <index>              # Show details for S-Gram at index
    python sgrams_cli.py transition <index> <state> # Show state transitions
    python sgrams_cli.py compare                    # Compare all S-Grams
    python sgrams_cli.py export                     # Export all tables to markdown
"""

import sys
import argparse
from pathlib import Path

# Add the src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sgrams import SGram
from sgrams.sgram import SGramFactory
from sgrams.state_transformer import StateTransformer
from sgrams.fraction_patterns import FractionPatternAnalyzer, CrossSGramAnalyzer
from sgrams.table_generator import (
    StateTransformationTableGenerator,
    AllSGramsTableGenerator,
    generate_all_markdown_tables
)


def cmd_summary(args):
    """Display summary of all S-Grams"""
    generator = AllSGramsTableGenerator()
    print(generator.generate_summary_table())


def cmd_show(args):
    """Show detailed information for a specific S-Gram"""
    try:
        sgram = SGramFactory.create_sgram(args.index)
        generator = StateTransformationTableGenerator(sgram)
        print(generator.generate_complete_table())
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0


def cmd_transition(args):
    """Show state transitions for a specific state"""
    try:
        sgram = SGramFactory.create_sgram(args.index)
        transformer = StateTransformer(sgram)
        
        print(f"\nState Transitions for S-Gram {sgram.symbol}, State {args.state}")
        print("=" * 70)
        
        # Find which patterns contain this state
        patterns_with_state = []
        for pattern_name, sequence in sgram.get_all_patterns().items():
            if args.state in sequence:
                patterns_with_state.append(pattern_name)
        
        if not patterns_with_state:
            print(f"State {args.state} not found in any pattern of S-Gram {sgram.symbol}")
            return 1
        
        print(f"State {args.state} appears in patterns: {', '.join(patterns_with_state)}")
        print()
        
        # Show transitions for each pattern
        for pattern in patterns_with_state:
            try:
                next_state = transformer.resolve(args.state, pattern)
                prev_state = transformer.inform(args.state, pattern)
                
                print(f"Pattern {pattern}:")
                print(f"  Inform (←):  {prev_state} ← {args.state}")
                print(f"  Current:     {args.state}")
                print(f"  Resolve (→): {args.state} → {next_state}")
                print()
            except ValueError:
                continue
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0


def cmd_compare(args):
    """Compare patterns across all S-Grams"""
    generator = AllSGramsTableGenerator()
    print(generator.generate_comparison_table())
    
    # Cross-S-Gram analysis
    sgrams = SGramFactory.create_all_sgrams()
    analyzer = CrossSGramAnalyzer(sgrams)
    
    print("\nCommon Patterns Across S-Grams:")
    print("=" * 70)
    common = analyzer.find_common_patterns()
    for divisor, sgram_indices in common[:10]:  # Top 10
        print(f"  {divisor}: appears in S-Grams {sgram_indices}")


def cmd_export(args):
    """Export all tables to markdown file"""
    output_file = args.output or "SGRAMS_TABLES.md"
    
    content = generate_all_markdown_tables()
    
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"Exported S-Grams tables to {output_file}")
    return 0


def cmd_trace(args):
    """Trace a path through state space"""
    try:
        sgram = SGramFactory.create_sgram(args.index)
        transformer = StateTransformer(sgram)
        
        pattern = args.pattern
        if pattern is None:
            # Use primary pattern
            pattern = list(sgram.fraction_patterns.keys())[0]
        
        path = transformer.trace_path(
            args.state, 
            args.steps, 
            pattern=pattern,
            reverse=args.reverse
        )
        
        direction = "Informing (←)" if args.reverse else "Resolving (→)"
        print(f"\nPath Trace for S-Gram {sgram.symbol}")
        print(f"Pattern: {pattern}, Starting State: {args.state}, Direction: {direction}")
        print("=" * 70)
        
        for i, state in enumerate(path):
            prefix = "Start: " if i == 0 else f"Step {i}: "
            print(f"{prefix:>10s}{state}")
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="S-Grams State Transformation Explorer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s summary
  %(prog)s show 3
  %(prog)s transition 3 5
  %(prog)s trace 3 1 --steps 10
  %(prog)s compare
  %(prog)s export --output my_tables.md
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Summary command
    subparsers.add_parser('summary', help='Display summary of all S-Grams')
    
    # Show command
    show_parser = subparsers.add_parser('show', help='Show details for specific S-Gram')
    show_parser.add_argument('index', type=int, help='S-Gram index (0-11)')
    
    # Transition command
    trans_parser = subparsers.add_parser('transition', help='Show state transitions')
    trans_parser.add_argument('index', type=int, help='S-Gram index (0-11)')
    trans_parser.add_argument('state', type=int, help='State value')
    
    # Trace command
    trace_parser = subparsers.add_parser('trace', help='Trace path through state space')
    trace_parser.add_argument('index', type=int, help='S-Gram index (0-11)')
    trace_parser.add_argument('state', type=int, help='Starting state')
    trace_parser.add_argument('--steps', type=int, default=10, help='Number of steps (default: 10)')
    trace_parser.add_argument('--pattern', type=str, help='Pattern to use (e.g., 1/3)')
    trace_parser.add_argument('--reverse', action='store_true', help='Trace backward (inform)')
    
    # Compare command
    subparsers.add_parser('compare', help='Compare patterns across all S-Grams')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export tables to markdown')
    export_parser.add_argument('--output', '-o', help='Output file (default: SGRAMS_TABLES.md)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Dispatch to appropriate command
    commands = {
        'summary': cmd_summary,
        'show': cmd_show,
        'transition': cmd_transition,
        'trace': cmd_trace,
        'compare': cmd_compare,
        'export': cmd_export,
    }
    
    return commands[args.command](args)


if __name__ == '__main__':
    sys.exit(main())
