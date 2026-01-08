#!/usr/bin/env python3
"""
N-Grams CLI Tool

Command-line interface for exploring N-Gram state transformations.
Supports 1st Power, 2nd Power (S-Grams), 3rd Power, 2D Catalan, and 3D Catalan.

Usage:
    python sgrams_cli.py summary [--type TYPE]         # Show summary of N-Grams
    python sgrams_cli.py show <index> [--type TYPE]    # Show details for N-Gram at index
    python sgrams_cli.py transition <index> <state>    # Show state transitions (S-Grams only)
    python sgrams_cli.py compare [--type TYPE]         # Compare N-Grams
    python sgrams_cli.py export [--type TYPE]          # Export tables to markdown
    python sgrams_cli.py types                         # List all available N-Gram types
"""

import sys
import argparse
from pathlib import Path

# Add the src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sgrams import (
    SGram,
    NGram1stPower, NGram1stPowerFactory,
    NGram3rdPower, NGram3rdPowerFactory,
    NGram2DCatalan, NGram2DCatalanFactory,
    NGram3DCatalan, NGram3DCatalanFactory,
    FlipTransform
)
from sgrams.sgram import SGramFactory
from sgrams.state_transformer import StateTransformer
from sgrams.fraction_patterns import FractionPatternAnalyzer, CrossSGramAnalyzer
from sgrams.table_generator import (
    StateTransformationTableGenerator,
    AllSGramsTableGenerator,
    generate_all_markdown_tables
)


NGRAM_TYPES = {
    '1st': '1st Power (Linear)',
    '2nd': '2nd Power (S-Grams/Quadratic)',
    '3rd': '3rd Power (Cubic)',
    '2d': '2D Catalan (Rooted Trees)',
    '3d': '3D Catalan (Unlabeled Trees)',
}


def get_ngram_factory(ngram_type: str):
    """Get the appropriate factory for the N-Gram type"""
    factories = {
        '1st': NGram1stPowerFactory,
        '2nd': SGramFactory,
        '3rd': NGram3rdPowerFactory,
        '2d': NGram2DCatalanFactory,
        '3d': NGram3DCatalanFactory,
    }
    return factories.get(ngram_type)


def cmd_types(args):
    """List all available N-Gram types"""
    print("\nAvailable N-Gram Types:")
    print("=" * 70)
    for key, description in NGRAM_TYPES.items():
        print(f"  {key:5s} : {description}")
    print("\nUse --type <TYPE> to specify which N-Gram type to use")
    print("Default is '2nd' (S-Grams)")
    return 0


def cmd_summary(args):
    """Display summary of N-Grams"""
    ngram_type = args.type if hasattr(args, 'type') and args.type else '2nd'
    
    if ngram_type == '2nd':
        # Use existing S-Grams summary
        generator = AllSGramsTableGenerator()
        print(generator.generate_summary_table())
    else:
        # Generate summary for other types
        factory = get_ngram_factory(ngram_type)
        if not factory:
            print(f"Error: Unknown N-Gram type '{ngram_type}'", file=sys.stderr)
            return 1
        
        print(f"\n{NGRAM_TYPES[ngram_type]} Summary")
        print("=" * 70)
        
        try:
            ngrams = factory.create_range(0, 12)
            print(f"\n{'Index':<8} {'Symbol':<12} {'Value':<10} {'Formula'}")
            print("-" * 70)
            for ng in ngrams:
                print(f"{ng.index:<8} {ng.symbol:<12} {ng.sequence_value:<10} {ng.formula}")
        except Exception as e:
            print(f"Error generating summary: {e}", file=sys.stderr)
            return 1
    
    return 0


def cmd_show(args):
    """Show detailed information for a specific N-Gram"""
    ngram_type = args.type if hasattr(args, 'type') and args.type else '2nd'
    factory = get_ngram_factory(ngram_type)
    
    if not factory:
        print(f"Error: Unknown N-Gram type '{ngram_type}'", file=sys.stderr)
        return 1
    
    try:
        if ngram_type == '2nd':
            sgram = factory.create_sgram(args.index)
            generator = StateTransformationTableGenerator(sgram)
            print(generator.generate_complete_table())
        elif ngram_type == '1st':
            ngram = factory.create_ngram_1st(args.index)
            print(ngram)
        elif ngram_type == '3rd':
            ngram = factory.create_ngram_3rd(args.index)
            print(ngram)
        elif ngram_type == '2d':
            ngram = factory.create_ngram_2d_catalan(args.index)
            print(ngram)
        elif ngram_type == '3d':
            ngram = factory.create_ngram_3d_catalan(args.index)
            print(ngram)
    except (ValueError, IndexError) as e:
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
    """Compare patterns across N-Grams"""
    ngram_type = args.type if hasattr(args, 'type') and args.type else '2nd'
    
    if ngram_type == '2nd':
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
    else:
        # Generate comparison for other types
        factory = get_ngram_factory(ngram_type)
        if not factory:
            print(f"Error: Unknown N-Gram type '{ngram_type}'", file=sys.stderr)
            return 1
        
        print(f"\n{NGRAM_TYPES[ngram_type]} Comparison")
        print("=" * 70)
        
        try:
            ngrams = factory.create_range(0, 12)
            
            print(f"\n{'Index':<8} {'Value':<12} {'Growth Rate':<15} {'Patterns'}")
            print("-" * 70)
            
            prev_value = 0
            for ng in ngrams:
                growth = ng.sequence_value - prev_value if prev_value > 0 else 0
                pattern_count = len(ng.fraction_patterns)
                print(f"{ng.index:<8} {ng.sequence_value:<12} {growth:<15} {pattern_count}")
                prev_value = ng.sequence_value
                
        except Exception as e:
            print(f"Error generating comparison: {e}", file=sys.stderr)
            return 1
    
    return 0


def cmd_export(args):
    """Export all tables to markdown file"""
    ngram_type = args.type if hasattr(args, 'type') and args.type else '2nd'
    output_file = args.output or f"NGRAMS_{ngram_type.upper()}_TABLES.md"
    
    if ngram_type == '2nd':
        content = generate_all_markdown_tables()
    else:
        # Generate markdown for other types
        factory = get_ngram_factory(ngram_type)
        if not factory:
            print(f"Error: Unknown N-Gram type '{ngram_type}'", file=sys.stderr)
            return 1
        
        try:
            ngrams = factory.create_range(0, 12)
            
            content = f"# {NGRAM_TYPES[ngram_type]} Tables\n\n"
            content += f"Generated tables for {NGRAM_TYPES[ngram_type]}\n\n"
            content += "## Summary\n\n"
            content += "| Index | Symbol | Value | Formula |\n"
            content += "|-------|--------|-------|----------|\n"
            
            for ng in ngrams:
                content += f"| {ng.index} | {ng.symbol} | {ng.sequence_value} | {ng.formula} |\n"
            
            content += "\n## Detailed Information\n\n"
            
            for ng in ngrams:
                content += f"### {ng.symbol} (Index {ng.index})\n\n"
                content += f"**Value:** {ng.sequence_value}\n\n"
                content += f"**Formula:** {ng.formula}\n\n"
                
                if ng.fraction_patterns:
                    content += "**Patterns:**\n\n"
                    for divisor, pattern in ng.fraction_patterns.items():
                        content += f"- {divisor}: {' '.join(map(str, pattern))}\n"
                    content += "\n"
                
                content += "---\n\n"
        
        except Exception as e:
            print(f"Error generating export: {e}", file=sys.stderr)
            return 1
    
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"Exported {NGRAM_TYPES[ngram_type]} tables to {output_file}")
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
        description="N-Grams State Transformation Explorer (1st, 2nd, 3rd Power and Catalan)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s types
  %(prog)s summary --type 1st
  %(prog)s summary --type 3rd
  %(prog)s show 3 --type 2d
  %(prog)s show 5 --type 3d
  %(prog)s transition 3 5
  %(prog)s trace 3 1 --steps 10
  %(prog)s compare --type 1st
  %(prog)s export --type 3rd --output cubic_tables.md
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Types command
    subparsers.add_parser('types', help='List all available N-Gram types')
    
    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Display summary of N-Grams')
    summary_parser.add_argument('--type', choices=NGRAM_TYPES.keys(), default='2nd',
                                help='N-Gram type (default: 2nd)')
    
    # Show command
    show_parser = subparsers.add_parser('show', help='Show details for specific N-Gram')
    show_parser.add_argument('index', type=int, help='N-Gram index (0-11)')
    show_parser.add_argument('--type', choices=NGRAM_TYPES.keys(), default='2nd',
                            help='N-Gram type (default: 2nd)')
    
    # Transition command (S-Grams only)
    trans_parser = subparsers.add_parser('transition', help='Show state transitions (S-Grams only)')
    trans_parser.add_argument('index', type=int, help='S-Gram index (0-11)')
    trans_parser.add_argument('state', type=int, help='State value')
    
    # Trace command (S-Grams only)
    trace_parser = subparsers.add_parser('trace', help='Trace path through state space (S-Grams only)')
    trace_parser.add_argument('index', type=int, help='S-Gram index (0-11)')
    trace_parser.add_argument('state', type=int, help='Starting state')
    trace_parser.add_argument('--steps', type=int, default=10, help='Number of steps (default: 10)')
    trace_parser.add_argument('--pattern', type=str, help='Pattern to use (e.g., 1/3)')
    trace_parser.add_argument('--reverse', action='store_true', help='Trace backward (inform)')
    
    # Compare command
    compare_parser = subparsers.add_parser('compare', help='Compare patterns across N-Grams')
    compare_parser.add_argument('--type', choices=NGRAM_TYPES.keys(), default='2nd',
                               help='N-Gram type (default: 2nd)')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export tables to markdown')
    export_parser.add_argument('--output', '-o', help='Output file (default: auto-generated)')
    export_parser.add_argument('--type', choices=NGRAM_TYPES.keys(), default='2nd',
                              help='N-Gram type (default: 2nd)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Dispatch to appropriate command
    commands = {
        'types': cmd_types,
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
