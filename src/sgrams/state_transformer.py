"""
State Transformer for S-Grams

Implements state transformation logic for S-Grams, including:
- State transitions based on fraction patterns
- Resolving patterns (forward transitions)
- Informing patterns (backward transitions)
"""

from typing import List, Dict, Tuple, Optional
from .sgram import SGram


class StateTransformer:
    """
    Handles state transformations for S-Grams.
    
    The StateTransformer implements the "Resolving" and "Informing" patterns
    that govern how states transition within an S-Gram system.
    """
    
    def __init__(self, sgram: SGram):
        """
        Initialize the StateTransformer with an S-Gram.
        
        Args:
            sgram: The S-Gram to use for state transformations
        """
        self.sgram = sgram
        self._state_map = self._build_state_map()
    
    def _build_state_map(self) -> Dict[int, Dict[str, int]]:
        """
        Build a mapping of states to their next states for each pattern.
        
        Returns:
            Dictionary mapping state -> {pattern: next_state}
        """
        state_map = {}
        
        for pattern_name, sequence in self.sgram.get_all_patterns().items():
            for i, state in enumerate(sequence):
                if state not in state_map:
                    state_map[state] = {}
                # Next state in the sequence (circular)
                next_state = sequence[(i + 1) % len(sequence)]
                state_map[state][pattern_name] = next_state
        
        return state_map
    
    def resolve(self, state: int, pattern: Optional[str] = None) -> int:
        """
        Apply the "Resolving" pattern: move forward in the state sequence.
        
        Args:
            state: Current state value
            pattern: The pattern to follow (e.g., '1/3', '1/7'). 
                    If None, uses the primary pattern.
                    
        Returns:
            The next state in the sequence
            
        Raises:
            ValueError: If the state or pattern is invalid
        """
        if pattern is None:
            # Get the first (primary) pattern
            patterns = list(self.sgram.fraction_patterns.keys())
            if not patterns:
                raise ValueError(f"No patterns available for S-Gram {self.sgram.index}")
            pattern = patterns[0]
        
        if state not in self._state_map:
            raise ValueError(f"State {state} not found in S-Gram {self.sgram.index}")
        
        if pattern not in self._state_map[state]:
            raise ValueError(f"Pattern {pattern} not applicable to state {state}")
        
        return self._state_map[state][pattern]
    
    def inform(self, state: int, pattern: Optional[str] = None) -> int:
        """
        Apply the "Informing" pattern: move backward in the state sequence.
        
        Args:
            state: Current state value
            pattern: The pattern to follow (e.g., '1/3', '1/7').
                    If None, uses the primary pattern.
                    
        Returns:
            The previous state in the sequence
            
        Raises:
            ValueError: If the state or pattern is invalid
        """
        if pattern is None:
            patterns = list(self.sgram.fraction_patterns.keys())
            if not patterns:
                raise ValueError(f"No patterns available for S-Gram {self.sgram.index}")
            pattern = patterns[0]
        
        sequence = self.sgram.fraction_patterns.get(pattern) or \
                   self.sgram.additional_factors.get(pattern)
        
        if sequence is None:
            raise ValueError(f"Pattern {pattern} not found in S-Gram {self.sgram.index}")
        
        if state not in sequence:
            raise ValueError(f"State {state} not in pattern {pattern}")
        
        # Find previous state (circular)
        idx = sequence.index(state)
        prev_state = sequence[(idx - 1) % len(sequence)]
        return prev_state
    
    def get_cycle_length(self, pattern: Optional[str] = None) -> int:
        """
        Get the cycle length for a specific pattern.
        
        Args:
            pattern: The pattern name. If None, uses the primary pattern.
            
        Returns:
            The length of the state cycle
        """
        if pattern is None:
            patterns = list(self.sgram.fraction_patterns.keys())
            if not patterns:
                return 0
            pattern = patterns[0]
        
        sequence = self.sgram.fraction_patterns.get(pattern) or \
                   self.sgram.additional_factors.get(pattern)
        
        return len(sequence) if sequence else 0
    
    def get_state_distance(self, from_state: int, to_state: int, 
                          pattern: Optional[str] = None) -> int:
        """
        Calculate the distance between two states in the sequence.
        
        Args:
            from_state: Starting state
            to_state: Target state
            pattern: The pattern to use. If None, uses the primary pattern.
            
        Returns:
            Number of steps from from_state to to_state (always positive)
            
        Raises:
            ValueError: If states or pattern are invalid
        """
        if pattern is None:
            patterns = list(self.sgram.fraction_patterns.keys())
            if not patterns:
                raise ValueError(f"No patterns available for S-Gram {self.sgram.index}")
            pattern = patterns[0]
        
        sequence = self.sgram.fraction_patterns.get(pattern) or \
                   self.sgram.additional_factors.get(pattern)
        
        if sequence is None:
            raise ValueError(f"Pattern {pattern} not found")
        
        if from_state not in sequence or to_state not in sequence:
            raise ValueError(f"States must be in the pattern sequence")
        
        from_idx = sequence.index(from_state)
        to_idx = sequence.index(to_state)
        
        # Calculate forward distance (circular)
        if to_idx >= from_idx:
            return to_idx - from_idx
        else:
            return len(sequence) - from_idx + to_idx
    
    def trace_path(self, start_state: int, steps: int, 
                   pattern: Optional[str] = None, 
                   reverse: bool = False) -> List[int]:
        """
        Trace a path through the state space for a given number of steps.
        
        Args:
            start_state: Starting state
            steps: Number of steps to trace
            pattern: The pattern to follow. If None, uses the primary pattern.
            reverse: If True, trace backward (inform), otherwise forward (resolve)
            
        Returns:
            List of states in the path, including the start state
        """
        path = [start_state]
        current_state = start_state
        
        for _ in range(steps):
            if reverse:
                current_state = self.inform(current_state, pattern)
            else:
                current_state = self.resolve(current_state, pattern)
            path.append(current_state)
        
        return path
    
    def get_transition_table(self, pattern: Optional[str] = None) -> Dict[int, Tuple[int, int]]:
        """
        Get a complete transition table showing (previous, next) for each state.
        
        Args:
            pattern: The pattern to use. If None, uses the primary pattern.
            
        Returns:
            Dictionary mapping state -> (previous_state, next_state)
        """
        if pattern is None:
            patterns = list(self.sgram.fraction_patterns.keys())
            if not patterns:
                return {}
            pattern = patterns[0]
        
        sequence = self.sgram.fraction_patterns.get(pattern) or \
                   self.sgram.additional_factors.get(pattern)
        
        if sequence is None:
            return {}
        
        table = {}
        for i, state in enumerate(sequence):
            prev_state = sequence[(i - 1) % len(sequence)]
            next_state = sequence[(i + 1) % len(sequence)]
            table[state] = (prev_state, next_state)
        
        return table
    
    def __repr__(self) -> str:
        """String representation of the StateTransformer"""
        return f"StateTransformer(sgram={self.sgram.symbol})"


class MultiPatternTransformer:
    """
    Handles transformations across multiple patterns within an S-Gram.
    
    This allows for more complex state transitions that may jump between
    different fraction patterns based on specific rules.
    """
    
    def __init__(self, sgram: SGram):
        """
        Initialize with an S-Gram.
        
        Args:
            sgram: The S-Gram to use
        """
        self.sgram = sgram
        self.transformers = {
            pattern: StateTransformer(sgram)
            for pattern in sgram.get_all_patterns().keys()
        }
    
    def cross_pattern_transition(self, state: int, 
                                from_pattern: str, 
                                to_pattern: str) -> Optional[int]:
        """
        Attempt to transition from one pattern to another at a given state.
        
        Args:
            state: Current state
            from_pattern: Current pattern
            to_pattern: Target pattern
            
        Returns:
            The state in the target pattern, or None if not possible
        """
        # Check if state exists in both patterns
        from_seq = self.sgram.get_all_patterns().get(from_pattern, [])
        to_seq = self.sgram.get_all_patterns().get(to_pattern, [])
        
        if state not in from_seq:
            return None
        
        # If the state exists in the target pattern, return it
        if state in to_seq:
            return state
        
        # Otherwise, no direct cross-pattern transition
        return None
    
    def get_pattern_for_state(self, state: int) -> List[str]:
        """
        Get all patterns that contain a given state.
        
        Args:
            state: The state to search for
            
        Returns:
            List of pattern names containing the state
        """
        patterns = []
        for pattern_name, sequence in self.sgram.get_all_patterns().items():
            if state in sequence:
                patterns.append(pattern_name)
        return patterns
