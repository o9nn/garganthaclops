# S-Grams: Mathematical Extensions and N-Gram Orders

## Overview

This document extends the S-Grams framework to explore higher-dimensional Catalan extensions and different orders of N-Grams, based on mathematical relationships between OEIS sequences and geometric interpretations.

## Current Implementation: 2nd Power N-Grams (S-Grams)

The current S-Grams implementation represents **2nd Power N-Grams** with the formula:

```
S(n) = 1 + (1 + n)²
```

These map to **1D Catalan numbers** (OEIS A000108) which represent the "surface" of a 1-dimensional interval where **order matters**.

### OEIS A000108: Catalan Numbers (1D)
```
Sequence: 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, ...
Formula: C(n) = (2n)! / ((n+1)! × n!)
```

**Interpretation**: 
- Count of binary trees with n internal nodes
- Dyck paths of length 2n
- Ways to triangulate a convex polygon
- **Maps to 1D interval surfaces** where sequence order is preserved

## Dimensional Extensions of Catalan Numbers

### 1D → 2D → 3D Catalan Progression

```
Dimension | OEIS      | Geometric Interpretation        | N-Gram Order
----------|-----------|----------------------------------|---------------
1D        | A000108   | Interval surface, order matters | 2nd Power
2D        | A000081   | Planar surface, rooted trees    | 3rd Power?
3D        | A000055   | Spherical surface, flip transform| 4th Power?
```

### OEIS A000081: Rooted Trees (2D Planar Catalan)

```
Sequence: 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766, ...
```

**Properties**:
- Number of rooted trees with n nodes
- Maps 2nd Power cycle patterns to **planar surfaces**
- Represents hierarchical organizational structures
- Extension of 1D Catalan to 2D plane

**Organizational Interpretation**:
- Hierarchical department structures
- Reporting relationships
- Decision tree pathways
- Strategic planning trees

### OEIS A000055: Trees (3D Spherical Catalan)

```
Sequence: 1, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, ...
```

**Properties**:
- Number of unlabeled trees with n nodes
- Clusters patterns under **flip transform**
- Maps to **spherical surfaces** (3D extension)
- Symmetry considerations reduce count

**Organizational Interpretation**:
- Network structures with symmetry
- Peer-to-peer coordination
- Matrix organizations
- Cross-functional teams

### OEIS A000041: Integer Partitions (Comparison)

```
Sequence: 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, ...
```

**Properties**:
- Number of partitions of n
- Different growth rate than Catalan sequences
- Represents resource allocation patterns
- Complementary to tree structures

**Organizational Interpretation**:
- Budget allocations
- Resource partitioning
- Team size distributions
- Work package divisions

## N-Gram Orders: 1st, 2nd, 3rd Power

### 1st Power N-Grams (Linear)

**Formula**: `N₁(n) = 1 + (1 + n)`

```
Index | Formula       | Value | Interpretation
------|---------------|-------|------------------
0     | 1 + (1 + 0)   | 2     | Linear progression
1     | 1 + (1 + 1)   | 3     | Simple sequence
2     | 1 + (1 + 2)   | 4     | Arithmetic growth
3     | 1 + (1 + 3)   | 5     | Constant increment
```

**Organizational Application**:
- Simple linear workflows
- Sequential processes
- Single-threaded execution
- Basic state machines

**Characteristics**:
- No branching
- No cycles (except trivial)
- Direct cause-effect
- Minimal complexity

### 2nd Power N-Grams (Quadratic - Current S-Grams)

**Formula**: `N₂(n) = 1 + (1 + n)²`

```
Index | Formula         | Value | Catalan | Organizational Rhythm
------|-----------------|-------|---------|----------------------
0     | 1 + (1 + 0)²   | 2     | 1       | Null state
1     | 1 + (1 + 1)²   | 5     | 2       | Binary decision
2     | 1 + (1 + 2)²   | 10    | 5       | Weekly cycle
3     | 1 + (1 + 3)²   | 17    | 14      | Bi-weekly cycle
4     | 1 + (1 + 4)²   | 26    | 42      | Monthly cycle
5     | 1 + (1 + 5)²   | 37    | 132     | Quarterly segment
```

**Organizational Application**:
- Cyclic processes with branching
- Feedback loops
- Multiple concurrent patterns
- Resolving/Informing dynamics

**Characteristics**:
- Quadratic growth in states
- Rich cycle structure
- Multiple fraction patterns
- Maps to 1D Catalan (surface of interval)

### 3rd Power N-Grams (Cubic - Future Extension)

**Formula**: `N₃(n) = 1 + (1 + n)³`

```
Index | Formula         | Value | Potential Mapping
------|-----------------|-------|------------------
0     | 1 + (1 + 0)³   | 2     | Root node
1     | 1 + (1 + 1)³   | 9     | Binary cube
2     | 1 + (1 + 2)³   | 28    | Complex branching
3     | 1 + (1 + 3)³   | 65    | Deep hierarchies
4     | 1 + (1 + 4)³   | 126   | Multi-level structures
```

**Potential Organizational Application**:
- Three-dimensional organizational matrices
- Tensor organizational structures
- Multi-axis decision spaces
- Volume-based resource allocation

**Characteristics**:
- Cubic growth in complexity
- Three independent dimensions
- Potential mapping to 2D Catalan (rooted trees)
- Hierarchical depth encoding

### Comparison: Growth Rates

```python
def compare_ngram_orders(n):
    """Compare different N-Gram order growth rates."""
    linear = 1 + (1 + n)
    quadratic = 1 + (1 + n) ** 2
    cubic = 1 + (1 + n) ** 3
    
    catalan = catalan_number(n)  # A000108
    rooted_trees = rooted_trees_count(n)  # A000081
    trees = trees_count(n)  # A000055
    partitions = partition_count(n)  # A000041
    
    return {
        '1st_power': linear,
        '2nd_power': quadratic,
        '3rd_power': cubic,
        'catalan_1d': catalan,
        'catalan_2d': rooted_trees,
        'catalan_3d': trees,
        'partitions': partitions
    }

# Example for n=5
# 1st_power: 7
# 2nd_power: 37
# 3rd_power: 217
# catalan_1d: 132
# catalan_2d: 20
# catalan_3d: 3
# partitions: 7
```

## Relationship Between N-Gram Powers and Catalan Dimensions

### Hypothesis: Power-Dimension Correspondence

```
N-Gram Order    | Catalan Dimension | OEIS     | Geometric Space
----------------|-------------------|----------|------------------
1st Power (n)   | 0D (points)       | ?        | Discrete points
2nd Power (n²)  | 1D (interval)     | A000108  | Line/interval surface
3rd Power (n³)  | 2D (planar)       | A000081  | Planar surface/trees
4th Power (n⁴)  | 3D (spherical)    | A000055  | Spherical surface/symmetry
```

### The Square Term in S-Grams

The square term `(1 + n)²` in S-Grams creates:

1. **Quadratic State Growth**: States scale with n²
2. **Cycle Patterns**: Multiple fraction patterns emerge
3. **Surface Mapping**: Maps to 1D Catalan (interval surfaces)
4. **Order Preservation**: Sequence order matters in transformations

### Flip Transform and 3D Extensions

**Flip Transform** (mentioned for OEIS A000055):
- Creates equivalence classes under graph isomorphism
- Reduces count due to symmetry
- Relevant for 3D Catalan (trees on sphere)
- Organizational analog: symmetric team structures

```python
class FlipTransform:
    """
    Flip transform for clustering patterns under symmetry.
    Relevant for 3D Catalan extensions (OEIS A000055).
    """
    
    def apply_flip(self, pattern):
        """Apply flip transform to create equivalence class."""
        # For organizational structures, this might represent:
        # - Role symmetry (interchangeable positions)
        # - Geographic symmetry (identical regional structures)
        # - Temporal symmetry (repeating patterns)
        pass
    
    def cluster_by_symmetry(self, patterns):
        """Cluster patterns that are equivalent under flip."""
        # Reduces state space by identifying symmetric patterns
        pass
```

## Future Extensions for CoSys-Org

### 1. Rooted Tree Patterns (2D Catalan - A000081)

Implement organizational hierarchy patterns using rooted trees:

```python
class RootedTreeSGram:
    """
    Extension of S-Grams to 2D planar patterns.
    Maps to OEIS A000081 (rooted trees).
    """
    
    def __init__(self, depth):
        self.depth = depth
        self.rooted_tree_count = self.compute_a000081(depth)
    
    def generate_hierarchy_patterns(self):
        """Generate organizational hierarchy patterns."""
        # Map rooted trees to org chart structures
        pass
```

### 2. Spherical Patterns (3D Catalan - A000055)

Implement symmetric network structures:

```python
class SphericalSGram:
    """
    Extension to 3D spherical patterns with flip transform.
    Maps to OEIS A000055 (unlabeled trees).
    """
    
    def __init__(self, nodes):
        self.nodes = nodes
        self.tree_count = self.compute_a000055(nodes)
    
    def apply_flip_transform(self, network):
        """Apply flip transform for symmetry clustering."""
        # Identify symmetric organizational structures
        pass
```

### 3. Partition-Based Resource Allocation (A000041)

Implement resource partitioning using integer partitions:

```python
class PartitionSGram:
    """
    Resource allocation patterns using partitions.
    Maps to OEIS A000041.
    """
    
    def __init__(self, total_resources):
        self.total = total_resources
        self.partition_count = self.compute_a000041(total_resources)
    
    def generate_allocations(self):
        """Generate all possible resource allocations."""
        # Enumerate partition patterns for budgets, teams, etc.
        pass
```

## Comparative Analysis Table

```
Property              | A000108  | A000081  | A000055  | A000041
                      | 1D Cat   | 2D Cat   | 3D Cat   | Partition
----------------------|----------|----------|----------|----------
Growth Rate           | ~4^n/n^(3/2) | ~2.96^n | ~2.95^n | exp(π√(2n/3))
Order Matters         | Yes      | Yes      | No       | No
Organizational Use    | Cycles   | Hierarchy| Networks | Resources
Current S-Gram Map    | Direct   | Indirect | None     | None
Complexity Level      | Medium   | High     | Very High| Medium
```

## Implementation Roadmap

### Phase 1: Enhanced Documentation (Current)
- [x] Document 2nd Power S-Grams (OEIS A000108)
- [x] Document relationships to higher dimensions
- [ ] Add references to OEIS sequences
- [ ] Create comparison visualizations

### Phase 2: 1st Power N-Grams
- [ ] Implement linear N-Gram patterns
- [ ] Simple state machines
- [ ] Basic workflow modeling

### Phase 3: 3rd Power N-Grams
- [ ] Implement cubic N-Gram patterns
- [ ] Hierarchical depth encoding
- [ ] Three-dimensional state spaces

### Phase 4: 2D Catalan Extensions (A000081)
- [ ] Implement rooted tree patterns
- [ ] Organizational hierarchy mapping
- [ ] Planar surface transformations

### Phase 5: 3D Catalan Extensions (A000055)
- [ ] Implement flip transform
- [ ] Symmetric network patterns
- [ ] Spherical surface mappings

### Phase 6: Partition Functions (A000041)
- [ ] Resource allocation patterns
- [ ] Budget distribution modeling
- [ ] Team size optimization

## Mathematical References

1. **OEIS A000108** (Catalan numbers): https://oeis.org/A000108
   - "Surface" of 1D interval, order matters
   - Current S-Gram implementation

2. **OEIS A000081** (Rooted trees): https://oeis.org/A000081
   - 2D Catalan extension
   - Planar surface patterns
   - Hierarchical structures

3. **OEIS A000055** (Trees): https://oeis.org/A000055
   - 3D Catalan extension
   - Spherical surface patterns
   - Flip transform clustering

4. **OEIS A000041** (Partitions): https://oeis.org/A000041
   - Complementary perspective
   - Resource allocation
   - Different growth characteristics

## Conclusion

The current S-Grams implementation (2nd Power N-Grams) provides a solid foundation for exploring:

1. **Linear patterns** (1st power) for simple workflows
2. **Quadratic patterns** (2nd power) for cyclic processes ✓ (current)
3. **Cubic patterns** (3rd power) for hierarchical structures
4. **Dimensional extensions** from 1D → 2D → 3D Catalan sequences
5. **Resource partitioning** using partition functions

This framework naturally extends to model increasingly complex organizational structures while maintaining mathematical rigor and practical utility.

---

**Note**: This document outlines the mathematical foundation for future extensions. The current implementation focuses on 2nd Power N-Grams (S-Grams) which map to 1D Catalan numbers (OEIS A000108).
