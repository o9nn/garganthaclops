# S-Grams: State Transformation Tables

## Overview

This document describes the S-Grams (2nd Power N-Grams) implementation for the CoSys-Org framework. S-Grams represent a mathematical pattern system for modeling state transformations using "Resolving" and "Informing" patterns.

**Note**: For mathematical context on N-Gram orders (1st, 2nd, 3rd power) and dimensional Catalan extensions (1D→2D→3D), see [Mathematical Extensions](SGRAMS_MATHEMATICAL_EXTENSIONS.md).

## What are S-Grams?

S-Grams are mathematical structures defined by:

- **Index**: 0 through 11
- **Catalan Number**: Associated combinatorial value
- **Fraction**: Reduced form of numerator/denominator
- **Formula**: `1 + (1 + n)²` where n is the index
- **Symbolic Notation**: Bracket-based representation
- **Fraction Patterns**: State sequences for different divisors

### Mathematical Foundation

For each S-Gram at index `n`:
- Formula: `1 + (1 + n)² = 1 + (1+n) + 1 + (1+n) + (1+n)²`
- This expands to: `(n+2) + (n+1)²`
- Example for n=3: `1 + (1+3)² = 1+4+1+4+16 = 5+16 = 26`

The **square term** `(1+n)²` creates quadratic growth in state space and maps to **1D Catalan numbers** (OEIS A000108), representing the "surface" of a 1-dimensional interval where **order matters**.

**Catalan Numbers** (OEIS A000108): 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, ...

## State Transformations

### Resolving Pattern (→)

The "Resolving" pattern moves forward through state sequences. Given a current state and a pattern, resolving returns the next state in the cycle.

```python
from sgrams.sgram import SGramFactory
from sgrams.state_transformer import StateTransformer

sgram = SGramFactory.create_sgram(3)
transformer = StateTransformer(sgram)

# Resolve: move forward
next_state = transformer.resolve(1, pattern='1/7')  # 1 → 4
```

### Informing Pattern (←)

The "Informing" pattern moves backward through state sequences. Given a current state and a pattern, informing returns the previous state in the cycle.

```python
# Inform: move backward
prev_state = transformer.inform(4, pattern='1/7')  # 7 ← 4
```

## Fraction Patterns

Each S-Gram contains multiple fraction patterns that define different state sequences:

### Primary Patterns
The main state sequences for the S-Gram, typically starting with `1/n` where n is related to the formula expansion.

### Additional Factors
Factor patterns that represent divisors of the denominator, providing alternative state sequences.

Example for S-Gram 3 (s4):
- Primary: `1/7 | 1 4 2 8 5 7` (cycle length: 6)
- Primary: `1/3 | 3 6` (cycle length: 2)
- Factor: `1/1 | 9` (cycle length: 1)

## Module Structure

### Core Classes

#### `SGram`
Represents a single S-Gram with all its properties:
- `index`: S-Gram index (0-11)
- `catalan_number`: Associated Catalan number
- `fraction_patterns`: Dictionary of fraction patterns
- `additional_factors`: Dictionary of factor patterns

#### `StateTransformer`
Handles state transformations:
- `resolve(state, pattern)`: Apply resolving pattern
- `inform(state, pattern)`: Apply informing pattern
- `trace_path(start, steps, pattern, reverse)`: Trace a path through state space
- `get_transition_table(pattern)`: Get complete transition table

#### `FractionPatternAnalyzer`
Analyzes fraction patterns:
- `get_primary_pattern()`: Get the primary pattern
- `get_patterns_containing_state(state)`: Find patterns with a state
- `analyze_cycle_relationships()`: Analyze cycle lengths
- `get_state_distribution()`: Distribution of states across patterns

#### `StateTransformationTableGenerator`
Generates formatted tables:
- `generate_basic_info_table()`: Basic S-Gram information
- `generate_fraction_patterns_table()`: All fraction patterns
- `generate_state_transition_table(pattern)`: State transitions
- `generate_complete_table()`: Complete formatted output

## Usage Examples

### Basic Usage

```python
from sgrams.sgram import SGramFactory

# Create a specific S-Gram
sgram = SGramFactory.create_sgram(5)
print(f"S-Gram: {sgram.symbol}")
print(f"Formula: {sgram.formula}")

# Access fraction patterns
for divisor, sequence in sgram.fraction_patterns.items():
    print(f"{divisor}: {sequence}")
```

### State Transformations

```python
from sgrams.state_transformer import StateTransformer

transformer = StateTransformer(sgram)

# Move forward through states
state = 1
for i in range(5):
    state = transformer.resolve(state, '1/21')
    print(f"Step {i+1}: {state}")

# Move backward
state = transformer.inform(21, '1/21')
print(f"Previous state: {state}")
```

### Path Tracing

```python
# Trace a forward path
path = transformer.trace_path(1, 10, pattern='1/21', reverse=False)
print(" → ".join(map(str, path)))

# Trace a backward path
path = transformer.trace_path(21, 8, pattern='1/21', reverse=True)
print(" ← ".join(map(str, path)))
```

### Pattern Analysis

```python
from sgrams.fraction_patterns import FractionPatternAnalyzer

analyzer = FractionPatternAnalyzer(sgram)

# Get primary pattern
primary = analyzer.get_primary_pattern()
print(f"Primary: {primary.divisor}, Cycle Length: {primary.cycle_length}")

# Analyze cycles
cycle_info = analyzer.analyze_cycle_relationships()
print(f"Common divisor: {cycle_info['common_divisor']}")
print(f"Max cycle: {cycle_info['max_cycle_length']}")
```

### Cross-S-Gram Analysis

```python
from sgrams.fraction_patterns import CrossSGramAnalyzer

# Analyze multiple S-Grams
sgrams = [SGramFactory.create_sgram(i) for i in range(6)]
cross_analyzer = CrossSGramAnalyzer(sgrams)

# Find common patterns
common = cross_analyzer.find_common_patterns()
for divisor, sgram_indices in common:
    print(f"{divisor} appears in S-Grams: {sgram_indices}")

# Analyze growth
growth = cross_analyzer.analyze_growth_pattern()
print(f"Catalan numbers: {growth['catalan_numbers']}")
```

### Table Generation

```python
from sgrams.table_generator import StateTransformationTableGenerator

generator = StateTransformationTableGenerator(sgram)

# Generate formatted tables
print(generator.generate_basic_info_table())
print(generator.generate_fraction_patterns_table())
print(generator.generate_state_transition_table('1/21'))
print(generator.generate_cycle_info_table())
```

## Command-Line Interface

The S-Grams module includes a CLI tool for easy exploration:

### Summary of All S-Grams
```bash
python src/sgrams/sgrams_cli.py summary
```

### Show Details for Specific S-Gram
```bash
python src/sgrams/sgrams_cli.py show 3
```

### Show State Transitions
```bash
python src/sgrams/sgrams_cli.py transition 3 5
```

### Trace Path Through State Space
```bash
python src/sgrams/sgrams_cli.py trace 3 1 --steps 10 --pattern 1/7
python src/sgrams/sgrams_cli.py trace 4 13 --steps 8 --reverse
```

### Compare All S-Grams
```bash
python src/sgrams/sgrams_cli.py compare
```

### Export to Markdown
```bash
python src/sgrams/sgrams_cli.py export --output my_tables.md
```

## Relationship to CoSys-Org

S-Grams provide a mathematical foundation for state transformations in the CoSys-Org organizational model:

1. **State Cycles**: The fraction patterns represent organizational cycles (quarterly, annual, etc.)
2. **Resolving/Informing**: Forward planning vs. backward analysis
3. **Multiple Patterns**: Different organizational rhythms operating simultaneously
4. **Nested Structures**: The bracket notation maps to nested organizational triads

### Integration Points

- **Cerebral Triad**: Strategic planning uses long-cycle patterns
- **Somatic Triad**: Operational execution follows medium-cycle patterns
- **Autonomic Triad**: Support functions operate on short-cycle patterns

The multi-pattern nature of S-Grams allows different organizational functions to operate on different time scales while maintaining coherence through common states.

## Mathematical Properties

### Catalan Numbers
Each S-Gram is associated with a Catalan number, which grows as:
- C₀ = 1, C₁ = 2, C₂ = 5, C₃ = 14, C₄ = 42, ...
- Formula: Cₙ = (1/(n+1)) × (2n choose n)

### Cycle Lengths
Fraction patterns have cycle lengths related to:
- The denominator of the reduced fraction
- The formula expansion value
- Common divisors reveal hierarchical structure

### Nested Patterns
The fractal nesting observed in S-Gram 9 (s10):
```
(81)(27 54)(9 36 18 72 45 63) = 9 × [(9)(3 6)(1 4 2 8 5 7)]
```
Shows self-similar structure across scales.

## Implementation Notes

### Design Decisions

1. **Immutable Data Structures**: S-Grams are created once and don't change
2. **Separate Concerns**: State transformations separate from pattern analysis
3. **Multiple Representations**: Support both computational and human-readable formats
4. **Extensibility**: Easy to add new analysis methods

### Performance Considerations

- State lookups are O(1) using dictionaries
- Cycle detection uses modular arithmetic
- Pattern matching is pre-computed during initialization

### Future Extensions

Potential areas for expansion:
- Interactive visualization tools
- Integration with organizational simulation
- Real-time state tracking
- Pattern prediction and forecasting
- Connection to other CoSys models

## References

- Agent Instructions: See `.github/agents/cosys-org.agent.md`
- Main Repository: CoSys-Org organizational framework
- Related Concepts: Catalan numbers, state machines, cycle theory

## Complete S-Grams Reference

See [SGRAMS_TABLES.md](./SGRAMS_TABLES.md) for complete tables of all S-Grams from 0 to 11.

## License

MIT License - Part of the CoSys-Org framework
