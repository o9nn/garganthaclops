"""
Examples for All N-Gram Types

Demonstrates usage of:
- 1st Power N-Grams (Linear)
- 2nd Power N-Grams (S-Grams/Quadratic)
- 3rd Power N-Grams (Cubic)
- 2D Catalan N-Grams (Rooted Trees)
- 3D Catalan N-Grams (Unlabeled Trees)
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from sgrams import (
    NGram1stPower, NGram1stPowerFactory,
    NGram3rdPower, NGram3rdPowerFactory,
    NGram2DCatalan, NGram2DCatalanFactory,
    NGram3DCatalan, NGram3DCatalanFactory,
    FlipTransform
)


def example_1st_power_ngrams():
    """Example: 1st Power N-Grams (Linear)"""
    print("=" * 80)
    print("EXAMPLE 1: 1st Power N-Grams (Linear)")
    print("=" * 80)
    print("\n1st Power N-Grams follow the formula: N₁(n) = 1 + (1 + n)")
    print("These represent simple linear progressions.\n")
    
    # Create a single 1st power N-Gram
    ngram = NGram1stPowerFactory.create_ngram_1st(5)
    print(f"Single N-Gram at index 5:")
    print(ngram)
    
    # Create a range
    print("\n\nSequence of 1st Power N-Grams (0-10):")
    print("-" * 80)
    ngrams = NGram1stPowerFactory.create_range(0, 11)
    
    print(f"{'Index':<8} {'Symbol':<12} {'Value':<8} {'Formula'}")
    print("-" * 80)
    for ng in ngrams:
        print(f"{ng.index:<8} {ng.symbol:<12} {ng.sequence_value:<8} {ng.formula}")


def example_3rd_power_ngrams():
    """Example: 3rd Power N-Grams (Cubic)"""
    print("\n\n" + "=" * 80)
    print("EXAMPLE 2: 3rd Power N-Grams (Cubic)")
    print("=" * 80)
    print("\n3rd Power N-Grams follow the formula: N₃(n) = 1 + (1 + n)³")
    print("These represent complex hierarchical patterns with cubic growth.\n")
    
    # Create a single 3rd power N-Gram
    ngram = NGram3rdPowerFactory.create_ngram_3rd(4)
    print(f"Single N-Gram at index 4:")
    print(ngram)
    
    # Create a range and show growth
    print("\n\nSequence of 3rd Power N-Grams (0-8):")
    print("-" * 80)
    ngrams = NGram3rdPowerFactory.create_range(0, 9)
    
    print(f"{'Index':<8} {'Symbol':<12} {'Value':<10} {'Growth':<10} {'Cube Base'}")
    print("-" * 80)
    prev_value = 0
    for ng in ngrams:
        growth = ng.sequence_value - prev_value if prev_value > 0 else 0
        cube_base = ng.formula_parts['cube_base']
        print(f"{ng.index:<8} {ng.symbol:<12} {ng.sequence_value:<10} {growth:<10} {cube_base}")
        prev_value = ng.sequence_value


def example_2d_catalan_ngrams():
    """Example: 2D Catalan N-Grams (Rooted Trees)"""
    print("\n\n" + "=" * 80)
    print("EXAMPLE 3: 2D Catalan N-Grams (Rooted Trees - OEIS A000081)")
    print("=" * 80)
    print("\nRooted Trees represent organizational hierarchies on planar surfaces.")
    print("Sequence: 0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, ...\n")
    
    # Create a single 2D Catalan N-Gram
    ngram = NGram2DCatalanFactory.create_ngram_2d_catalan(7)
    print(f"Single N-Gram at index 7:")
    print(ngram)
    
    # Create a range
    print("\n\nSequence of 2D Catalan N-Grams (1-11):")
    print("-" * 80)
    ngrams = NGram2DCatalanFactory.create_range(1, 12)
    
    print(f"{'Index':<8} {'Symbol':<12} {'Trees':<10} {'Growth Rate':<12} {'Patterns'}")
    print("-" * 80)
    prev_value = 0
    for ng in ngrams:
        growth = ng.sequence_value - prev_value if prev_value > 0 else 0
        pattern_count = len(ng.fraction_patterns)
        print(f"{ng.index:<8} {ng.symbol:<12} {ng.sequence_value:<10} {growth:<12} {pattern_count}")
        prev_value = ng.sequence_value
    
    # Show hierarchy patterns for a specific index
    print("\n\nHierarchy Patterns for index 6 (20 rooted trees):")
    print("-" * 80)
    ngram6 = NGram2DCatalanFactory.create_ngram_2d_catalan(6)
    for divisor, pattern in ngram6.fraction_patterns.items():
        print(f"  {divisor}: {pattern}")


def example_3d_catalan_ngrams():
    """Example: 3D Catalan N-Grams (Unlabeled Trees)"""
    print("\n\n" + "=" * 80)
    print("EXAMPLE 4: 3D Catalan N-Grams (Unlabeled Trees - OEIS A000055)")
    print("=" * 80)
    print("\nUnlabeled Trees represent symmetric networks on spherical surfaces.")
    print("These account for symmetry via the flip transform.")
    print("Sequence: 1, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, ...\n")
    
    # Create a single 3D Catalan N-Gram
    ngram = NGram3DCatalanFactory.create_ngram_3d_catalan(8)
    print(f"Single N-Gram at index 8:")
    print(ngram)
    
    # Create a range
    print("\n\nSequence of 3D Catalan N-Grams (0-11):")
    print("-" * 80)
    ngrams = NGram3DCatalanFactory.create_range(0, 12)
    
    print(f"{'Index':<8} {'Symbol':<12} {'Trees':<10} {'Symmetry Factor':<16} {'Patterns'}")
    print("-" * 80)
    for ng in ngrams:
        pattern_count = len(ng.fraction_patterns)
        sym = "flip_transform" if ng.sequence_value > 1 else "trivial"
        print(f"{ng.index:<8} {ng.symbol:<12} {ng.sequence_value:<10} {sym:<16} {pattern_count}")


def example_flip_transform():
    """Example: Flip Transform for Symmetry Clustering"""
    print("\n\n" + "=" * 80)
    print("EXAMPLE 5: Flip Transform for Symmetry Clustering")
    print("=" * 80)
    print("\nThe flip transform identifies equivalent structures under graph isomorphism.\n")
    
    # Example patterns
    patterns = [
        [1, 2, 3, 4],
        [4, 3, 2, 1],  # Same as above under flip
        [1, 3, 2, 4],
        [2, 4, 1, 3],
        [3, 1, 4, 2],
    ]
    
    print("Original patterns:")
    for i, pattern in enumerate(patterns):
        print(f"  Pattern {i+1}: {pattern}")
    
    print("\nApplying flip transform:")
    for i, pattern in enumerate(patterns):
        flipped = FlipTransform.apply_flip(pattern)
        print(f"  Pattern {i+1}: {pattern} → Canonical: {flipped}")
    
    print("\nClustering by symmetry:")
    clusters = FlipTransform.cluster_by_symmetry(patterns)
    for canonical, cluster in clusters.items():
        print(f"  Canonical {canonical}:")
        for pattern in cluster:
            print(f"    {pattern}")


def example_comparative_analysis():
    """Example: Comparative Analysis of All N-Gram Types"""
    print("\n\n" + "=" * 80)
    print("EXAMPLE 6: Comparative Analysis of All N-Gram Types")
    print("=" * 80)
    print("\nComparing growth rates across all N-Gram types:\n")
    
    print(f"{'Index':<8} {'1st Power':<12} {'2nd Power':<12} {'3rd Power':<12} {'2D Catalan':<12} {'3D Catalan':<12}")
    print("-" * 80)
    
    from sgrams.ngram_1st_power import compute_1st_power_sequence
    from sgrams.ngram_3rd_power import compute_3rd_power_sequence
    from sgrams.ngram_2d_catalan import get_rooted_trees_sequence
    from sgrams.ngram_3d_catalan import get_unlabeled_trees_sequence
    from sgrams.sgram import SGramFactory
    
    # Get sequences
    seq_1st = compute_1st_power_sequence(12)
    seq_3rd = compute_3rd_power_sequence(12)
    seq_2d = get_rooted_trees_sequence(11)
    seq_3d = get_unlabeled_trees_sequence(11)
    
    # 2nd power (S-Grams)
    sgrams = SGramFactory.create_all_sgrams()
    seq_2nd = [1 + (1 + sg.index) ** 2 for sg in sgrams]
    
    for i in range(12):
        val_1st = seq_1st[i] if i < len(seq_1st) else '-'
        val_2nd = seq_2nd[i] if i < len(seq_2nd) else '-'
        val_3rd = seq_3rd[i] if i < len(seq_3rd) else '-'
        val_2d = seq_2d[i] if i < len(seq_2d) else '-'
        val_3d = seq_3d[i] if i < len(seq_3d) else '-'
        
        print(f"{i:<8} {str(val_1st):<12} {str(val_2nd):<12} {str(val_3rd):<12} {str(val_2d):<12} {str(val_3d):<12}")


def example_organizational_applications():
    """Example: Organizational Applications"""
    print("\n\n" + "=" * 80)
    print("EXAMPLE 7: Organizational Applications")
    print("=" * 80)
    
    print("\n1st Power N-Grams (Linear) - Simple Workflows:")
    print("-" * 80)
    print("  • Sequential task execution")
    print("  • Linear approval chains")
    print("  • Single-threaded processes")
    print("  Example: Document approval → Review → Sign → Archive")
    
    print("\n2nd Power N-Grams (S-Grams) - Cyclic Processes:")
    print("-" * 80)
    print("  • Weekly/monthly cycles")
    print("  • Feedback loops")
    print("  • Resolving/Informing dynamics")
    print("  Example: Sprint planning → Development → Review → Retrospective (cycle)")
    
    print("\n3rd Power N-Grams (Cubic) - Hierarchical Matrices:")
    print("-" * 80)
    print("  • Three-dimensional org structures")
    print("  • Multi-axis decision spaces")
    print("  • Tensor organizations")
    print("  Example: Product × Geography × Function matrix")
    
    print("\n2D Catalan (Rooted Trees) - Organizational Hierarchies:")
    print("-" * 80)
    print("  • Department structures")
    print("  • Reporting relationships")
    print("  • Decision tree pathways")
    print("  Example: CEO → VPs → Directors → Managers → Teams")
    
    print("\n3D Catalan (Unlabeled Trees) - Symmetric Networks:")
    print("-" * 80)
    print("  • Peer-to-peer coordination")
    print("  • Matrix organizations")
    print("  • Cross-functional teams")
    print("  Example: Agile squads with interchangeable roles")


def main():
    """Run all examples"""
    print("\n" + "#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + "  N-GRAMS COMPREHENSIVE EXAMPLES".center(78) + "#")
    print("#" + "  (1st, 2nd, 3rd Power and Catalan Extensions)".center(78) + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)
    
    examples = [
        example_1st_power_ngrams,
        example_3rd_power_ngrams,
        example_2d_catalan_ngrams,
        example_3d_catalan_ngrams,
        example_flip_transform,
        example_comparative_analysis,
        example_organizational_applications,
    ]
    
    for example_func in examples:
        try:
            example_func()
        except Exception as e:
            print(f"\nError in {example_func.__name__}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "#" * 80)
    print("# All examples completed")
    print("#" * 80)
    print()


if __name__ == '__main__':
    main()
