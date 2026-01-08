# S-Grams Quick Reference

## What are S-Grams?

S-Grams (2nd Power N-Grams) are mathematical structures that model state transformations through cyclic patterns. Each S-Gram (indexed 0-11) has:

- **Formula**: `1 + (1+n)²` where n is the index
- **Fraction patterns**: Cyclic sequences of states
- **Resolving (→)**: Forward state transitions
- **Informing (←)**: Backward state transitions

## Quick Start

### Python API

```python
# Create an S-Gram
from sgrams.sgram import SGramFactory
sgram = SGramFactory.create_sgram(3)  # Creates S-Gram 3 (s4)

# State transformations
from sgrams.state_transformer import StateTransformer
transformer = StateTransformer(sgram)

# Move forward (resolve)
next_state = transformer.resolve(1, pattern='1/7')  # 1 → 4

# Move backward (inform)
prev_state = transformer.inform(4, pattern='1/7')  # 7 ← 4

# Trace a path
path = transformer.trace_path(1, 10, pattern='1/7')
# Result: [1, 4, 2, 8, 5, 7, 1, 4, 2, 8, 5]
```

### CLI Commands

```bash
# Summary of all S-Grams
python src/sgrams/sgrams_cli.py summary

# Detailed view of S-Gram 3
python src/sgrams/sgrams_cli.py show 3

# State transitions for state 5 in S-Gram 3
python src/sgrams/sgrams_cli.py transition 3 5

# Trace 10 forward steps from state 1
python src/sgrams/sgrams_cli.py trace 3 1 --steps 10 --pattern 1/7

# Trace 8 backward steps from state 13
python src/sgrams/sgrams_cli.py trace 4 13 --steps 8 --reverse

# Compare all S-Grams
python src/sgrams/sgrams_cli.py compare

# Export to markdown
python src/sgrams/sgrams_cli.py export --output my_tables.md
```

## S-Grams Summary Table

| Index | Symbol | Catalan | Fraction | Formula Result | Primary Pattern |
|-------|--------|---------|----------|----------------|-----------------|
| 0 | s1 | 1 | 0/0 | 2 | 0/1 (cycle: 1) |
| 1 | s2 | 2 | 1/1 | 5 | 1/1 (cycle: 1) |
| 2 | s3 | 5 | 1/2 | 10 | 1/3 (cycle: 2) |
| 3 | s4 | 14 | 1/3 | 17 | 1/7 (cycle: 6) |
| 4 | s5 | 42 | 1/4 | 26 | 1/13 (cycle: 6) |
| 5 | s6 | 132 | 1/5 | 37 | 1/21 (cycle: 6) |
| 6 | s7 | 429 | 1/6 | 50 | 1/31 (cycle: 6) |
| 7 | s8 | 1430 | 1/7 | 65 | 1/43 (cycle: 6) |
| 8 | s9 | 4862 | 1/8 | 82 | 1/57 (cycle: 6) |
| 9 | s10 | 16796 | 1/9 | 101 | 1/73 (cycle: 6) |
| 10 | s11 | 58786 | 1/10 | 122 | 1/91 (cycle: 6) |
| 11 | s12 | 208012 | 1/11 | 145 | 1/111 (cycle: 6) |

## Key Patterns

### State Cycle Lengths
From S-Gram 3 onwards, primary patterns have cycle length 6:
- S-Gram 3: `1 → 4 → 2 → 8 → 5 → 7 → 1` (pattern 1/7)
- S-Gram 4: `1 → 5 → 3 → 15 → 11 → 13 → 1` (pattern 1/13)
- S-Gram 5: `1 → 6 → 4 → 24 → 19 → 21 → 1` (pattern 1/21)

### Total Unique States
The number of unique states follows a perfect square pattern:
- S-Gram 0: 1 state (0²+1 or special case)
- S-Gram 1: 1 state (1²)
- S-Gram 2: 4 states (2²)
- S-Gram 3: 9 states (3²)
- S-Gram 4: 16 states (4²)
- S-Gram n: (n+1)² states

### Fractal Nesting
S-Gram 9 exhibits fractal nesting:
```
(81)(27 54)(9 36 18 72 45 63) = 9 × [(9)(3 6)(1 4 2 8 5 7)]
```

## Common Use Cases

### 1. Organizational Cycles
Model quarterly business rhythms:
```python
# Q1-Q4 cycle using S-Gram 2
sgram = SGramFactory.create_sgram(2)
quarters = transformer.trace_path(1, 4, pattern='1/2')
```

### 2. State Machine Design
Build deterministic state machines:
```python
# 6-state cycle
sgram = SGramFactory.create_sgram(3)
states = transformer.get_transition_table('1/7')
```

### 3. Pattern Analysis
Analyze cyclic dependencies:
```python
from sgrams.fraction_patterns import FractionPatternAnalyzer
analyzer = FractionPatternAnalyzer(sgram)
cycle_info = analyzer.analyze_cycle_relationships()
```

### 4. Multi-Pattern Systems
Work with systems operating on multiple rhythms:
```python
from sgrams.state_transformer import MultiPatternTransformer
multi = MultiPatternTransformer(sgram)
patterns = multi.get_pattern_for_state(6)
```

## API Quick Reference

### Core Classes

- `SGram`: Immutable S-Gram data structure
- `SGramFactory`: Creates S-Grams by index
- `StateTransformer`: Handles state transitions
- `FractionPatternAnalyzer`: Analyzes patterns
- `StateTransformationTableGenerator`: Generates formatted output

### Key Methods

#### SGram
- `sgram.symbol` - Get symbol (e.g., 's4')
- `sgram.formula` - Get formula string
- `sgram.get_all_patterns()` - All patterns
- `sgram.fraction_patterns` - Primary patterns
- `sgram.additional_factors` - Factor patterns

#### StateTransformer
- `resolve(state, pattern)` - Next state
- `inform(state, pattern)` - Previous state
- `trace_path(start, steps, pattern, reverse)` - Path trace
- `get_transition_table(pattern)` - Full transition table
- `get_cycle_length(pattern)` - Cycle length

#### FractionPatternAnalyzer
- `get_primary_pattern()` - Primary pattern
- `get_all_states()` - All unique states
- `analyze_cycle_relationships()` - Cycle analysis
- `get_state_distribution()` - State frequency

## Files and Documentation

- `src/sgrams/` - Implementation source
- `docs/SGRAMS_README.md` - Complete documentation
- `docs/SGRAMS_TABLES.md` - Full reference tables
- `docs/SGRAMS_MATHEMATICAL_EXTENSIONS.md` - Mathematical foundations, N-Gram orders, dimensional extensions
- `src/sgrams/examples.py` - Usage examples

## Mathematical Context

Current S-Grams implement **2nd Power N-Grams** mapping to **1D Catalan numbers** (OEIS A000108).

Future extensions could include:
- **1st Power N-Grams**: Linear patterns for simple workflows
- **3rd Power N-Grams**: Cubic patterns for hierarchical structures  
- **2D Catalan (OEIS A000081)**: Rooted trees for organizational hierarchies
- **3D Catalan (OEIS A000055)**: Symmetric networks with flip transform
- **Partitions (OEIS A000041)**: Resource allocation patterns

See [Mathematical Extensions](./SGRAMS_MATHEMATICAL_EXTENSIONS.md) for details.

## License

MIT License - Part of CoSys-Org framework
