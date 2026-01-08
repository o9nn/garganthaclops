"""
SGram class representing a single S-Gram (2nd Power N-Gram).

Each S-Gram has:
- An index (0-11)
- A symbolic notation (s1-s12)
- A Catalan number
- Transformation patterns
- Fraction patterns showing state transitions
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class SGram:
    """
    Represents a single S-Gram with its properties and state transformations.
    
    Attributes:
        index: The S-Gram index (0-11)
        catalan_number: The corresponding Catalan number
        numerator: Numerator in the fraction form
        denominator: Denominator in the fraction form
        symbolic_notation: Symbolic bracket notation
        transformation: Visual transformation pattern
        formula_parts: Parts of the formula calculation
        fraction_patterns: Dictionary mapping divisors to sequence patterns
        additional_factors: Optional additional factor patterns
    """
    index: int
    catalan_number: int
    numerator: int
    denominator: int
    symbolic_notation: str
    transformation: str
    formula_parts: Dict[str, int]
    fraction_patterns: Dict[str, List[int]] = field(default_factory=dict)
    additional_factors: Dict[str, List[int]] = field(default_factory=dict)
    
    @property
    def symbol(self) -> str:
        """Returns the s-notation (s1, s2, etc.)"""
        return f"s{self.index + 1}"
    
    @property
    def fraction(self) -> str:
        """Returns the fraction representation"""
        if self.denominator == 0:
            return f"{self.numerator}/0"
        gcd_val = self._gcd(self.numerator, self.denominator)
        return f"{self.numerator//gcd_val}/{self.denominator//gcd_val}"
    
    @property
    def formula(self) -> str:
        """Returns the full formula string"""
        n = self.index
        expansion = 1 + (1 + n) ** 2
        parts = [1, (1 + n), 1, (1 + n), (1 + n) ** 2]
        total = sum(parts)
        split_sum = f"{1 + (1 + n)}+{(1 + n) ** 2}"
        return f"1+(1+{n})^2 = {'+'.join(map(str, parts))} = {split_sum} = {total}"
    
    def _gcd(self, a: int, b: int) -> int:
        """Calculate greatest common divisor"""
        while b:
            a, b = b, a % b
        return a
    
    def get_state_sequence(self, divisor: Optional[str] = None) -> List[int]:
        """
        Get the state sequence for a specific divisor.
        
        Args:
            divisor: The divisor key (e.g., '1/3', '1/7'). If None, returns primary pattern.
            
        Returns:
            List of integers representing the state sequence
        """
        if divisor is None:
            # Return the primary fraction pattern
            if self.fraction_patterns:
                return list(self.fraction_patterns.values())[0]
            return []
        return self.fraction_patterns.get(divisor, [])
    
    def get_all_patterns(self) -> Dict[str, List[int]]:
        """Returns all fraction patterns including additional factors"""
        all_patterns = dict(self.fraction_patterns)
        all_patterns.update(self.additional_factors)
        return all_patterns
    
    def __str__(self) -> str:
        """String representation of the S-Gram"""
        lines = []
        lines.append("-" * 60)
        lines.append(f"{self.index} {self.symbol} [{self.catalan_number}] {self.fraction} -> {self.symbolic_notation}")
        lines.append(f"Transformation: {self.transformation}")
        lines.append(f"Formula: {self.formula}")
        lines.append("-" * 60)
        
        # Add fraction patterns
        if self.fraction_patterns:
            lines.append("\nFraction Patterns:")
            for divisor, pattern in self.fraction_patterns.items():
                lines.append(f"  {divisor} | {' '.join(map(str, pattern))}")
        
        # Add additional factors
        if self.additional_factors:
            lines.append("\nAdditional Factors:")
            for divisor, pattern in self.additional_factors.items():
                lines.append(f"  {divisor} | {' '.join(map(str, pattern))}")
        
        return "\n".join(lines)


class SGramFactory:
    """Factory class for creating S-Gram instances"""
    
    # Catalan numbers for indices 0-11
    CATALAN_NUMBERS = [1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012]
    
    @staticmethod
    def create_sgram_0() -> SGram:
        """S-Gram 0: s1 [1] 0/0"""
        return SGram(
            index=0,
            catalan_number=1,
            numerator=0,
            denominator=0,
            symbolic_notation="[0)(0] = [0] ~> [-] = ()",
            transformation="[(][)] = (][)(][) = (-) = () = O",
            formula_parts={'base': 1, 'expansion': 0},
            fraction_patterns={
                '0/1': [0]
            },
            additional_factors={}
        )
    
    @staticmethod
    def create_sgram_1() -> SGram:
        """S-Gram 1: s2 [2] 1/1"""
        return SGram(
            index=1,
            catalan_number=2,
            numerator=1,
            denominator=1,
            symbolic_notation="[1)(1] = [1] ~> [(0)] = []",
            transformation="[)(] = )[()]( = )|( = ][ = I",
            formula_parts={'base': 1, 'expansion': 1},
            fraction_patterns={
                '1/1': [1]
            },
            additional_factors={
                '1/1': [1]
            }
        )
    
    @staticmethod
    def create_sgram_2() -> SGram:
        """S-Gram 2: s3 [4] 2/4 = 1/2"""
        return SGram(
            index=2,
            catalan_number=5,
            numerator=2,
            denominator=4,
            symbolic_notation="[2)(1] = [2] ~> [([1])] = [([])]",
            transformation="[()] = [(][)] = [(I)] = IO",
            formula_parts={'base': 2, 'expansion': 3},
            fraction_patterns={
                '1/3': [1, 3],
                '1/2': [2]
            },
            additional_factors={
                '1/1': [4]
            }
        )
    
    @staticmethod
    def create_sgram_3() -> SGram:
        """S-Gram 3: s4 [9] 3/9 = 1/3"""
        return SGram(
            index=3,
            catalan_number=14,
            numerator=3,
            denominator=9,
            symbolic_notation="[3)(1] = [3] ~> [([2])] = [([()])]",
            transformation="[(())]",
            formula_parts={'base': 3, 'expansion': 7},
            fraction_patterns={
                '1/7': [1, 4, 2, 8, 5, 7],
                '1/3': [3, 6]
            },
            additional_factors={
                '1/1': [9]
            }
        )
    
    @staticmethod
    def create_sgram_4() -> SGram:
        """S-Gram 4: s5 [20] 4/16 = 1/4"""
        return SGram(
            index=4,
            catalan_number=42,
            numerator=4,
            denominator=16,
            symbolic_notation="[4] = [2][2] = [(1)][(1)]",
            transformation="[()][()] = [()()]",
            formula_parts={'base': 4, 'expansion': 13},
            fraction_patterns={
                '1/13': [1, 5, 3, 15, 11, 13],
                '2/13': [2, 10, 7, 14, 6, 9],
                '1/4': [4, 8, 12]
            },
            additional_factors={
                '1/4': [4, 12],
                '1/2': [8],
                '1/1': [16]
            }
        )
    
    @staticmethod
    def create_sgram_5() -> SGram:
        """S-Gram 5: s6 [48] 5/25 = 1/5"""
        return SGram(
            index=5,
            catalan_number=132,
            numerator=5,
            denominator=25,
            symbolic_notation="[5] ~> [([3])] = [([(())])]",
            transformation="[((()))]",
            formula_parts={'base': 5, 'expansion': 21},
            fraction_patterns={
                '1/21': [1, 6, 4, 24, 19, 21],
                '2/21': [2, 12, 9, 23, 13, 16],
                '3/21': [3, 18, 14, 22, 7, 11],
                '7/21': [8, 17],
                '1/5': [5, 10, 15, 20]
            },
            additional_factors={
                '1/1': [25]
            }
        )
    
    @staticmethod
    def create_sgram_6() -> SGram:
        """S-Gram 6: s7 [115] 6/36 = 1/6"""
        return SGram(
            index=6,
            catalan_number=429,
            numerator=6,
            denominator=36,
            symbolic_notation="[6] = [2][3] = [()][(())]",
            transformation="[()(())]",
            formula_parts={'base': 6, 'expansion': 31},
            fraction_patterns={
                '1/31': [1, 7, 5, 35, 29, 31],
                '2/31': [2, 14, 11, 34, 22, 25],
                '3/31': [3, 21, 17, 33, 15, 19],
                '4/31': [4, 28, 23, 32, 8, 13],
                '8/31': [9, 20, 10, 27, 16, 26],
                '1/6': [6, 12, 18, 24, 30]
            },
            additional_factors={
                '1/6': [6, 30],
                '1/3': [12, 24],
                '1/2': [18],
                '1/1': [36]
            }
        )
    
    @staticmethod
    def create_sgram_7() -> SGram:
        """S-Gram 7: s8 [286] 7/49 = 1/7"""
        return SGram(
            index=7,
            catalan_number=1430,
            numerator=7,
            denominator=49,
            symbolic_notation="[7] = [([4])] = [([()()])]",
            transformation="[(()())]",
            formula_parts={'base': 7, 'expansion': 43},
            fraction_patterns={
                '1/43': [1, 8, 6, 48, 41, 43],
                '2/43': [2, 16, 13, 47, 33, 36],
                '3/43': [3, 24, 20, 46, 25, 29],
                '4/43': [4, 32, 27, 45, 17, 22],
                '5/43': [5, 40, 34, 44, 9, 15],
                '9/43': [10, 23, 12, 39, 26, 37],
                '10/43': [11, 31, 19, 38, 18, 30],
                '1/7': [7, 14, 21, 28, 35, 42]
            },
            additional_factors={
                '1/1': [49]
            }
        )
    
    @staticmethod
    def create_sgram_8() -> SGram:
        """S-Gram 8: s9 [719] 8/64 = 1/8"""
        return SGram(
            index=8,
            catalan_number=4862,
            numerator=8,
            denominator=64,
            symbolic_notation="[8] = [2][2][2] = [3[2]] = [()][()][()] ",
            transformation="[()()()]",
            formula_parts={'base': 8, 'expansion': 57},
            fraction_patterns={
                '1/57': [1, 9, 7, 63, 55, 57],
                '2/57': [2, 18, 15, 62, 46, 49],
                '3/57': [3, 27, 23, 61, 37, 41],
                '4/57': [4, 36, 31, 60, 28, 33],
                '5/57': [5, 45, 39, 59, 19, 25],
                '6/57': [6, 54, 47, 58, 10, 17],
                '10/57': [11, 26, 14, 53, 38, 50],
                '11/57': [12, 35, 22, 52, 29, 42],
                '12/57': [13, 44, 30, 51, 20, 34],
                '19/57': [21, 43],
                '1/8': [8, 16, 24, 32, 40, 48, 56]
            },
            additional_factors={
                '1/8': [8, 24, 40, 56],
                '1/4': [16, 48],
                '1/2': [32],
                '1/1': [64]
            }
        )
    
    @staticmethod
    def create_sgram_9() -> SGram:
        """S-Gram 9: s10 [1842] 9/81 = 1/9"""
        return SGram(
            index=9,
            catalan_number=16796,
            numerator=9,
            denominator=81,
            symbolic_notation="[9] = [3][3] = [2[3]] = [(())][(())]",
            transformation="[(())(())]",
            formula_parts={'base': 9, 'expansion': 73},
            fraction_patterns={
                '1/73': [1, 10, 8, 80, 71, 73],
                '2/73': [2, 20, 17, 79, 61, 64],
                '3/73': [3, 30, 26, 78, 51, 55],
                '4/73': [4, 40, 35, 77, 41, 46],
                '5/73': [5, 50, 44, 76, 31, 37],
                '6/73': [6, 60, 53, 75, 21, 28],
                '7/73': [7, 70, 62, 74, 11, 19],
                '11/73': [12, 29, 16, 69, 52, 65],
                '12/73': [13, 39, 25, 68, 42, 56],
                '13/73': [14, 49, 34, 67, 32, 47],
                '14/73': [15, 59, 43, 66, 22, 38],
                '21/73': [23, 48, 24, 58, 33, 57],
                '1/9': [9, 18, 27, 36, 45, 54, 63, 72]
            },
            additional_factors={
                '1/9': [9, 18, 36, 45, 63, 72],
                '1/3': [27, 54],
                '1/1': [81]
            }
        )
    
    @staticmethod
    def create_sgram_10() -> SGram:
        """S-Gram 10: s11 [4766] 10/100 = 1/10"""
        return SGram(
            index=10,
            catalan_number=58786,
            numerator=10,
            denominator=100,
            symbolic_notation="[10] = [2][5] = [()][((()))]",
            transformation="[()((()))]",
            formula_parts={'base': 10, 'expansion': 91},
            fraction_patterns={
                '1/91': [1, 11, 9, 99, 89, 91],
                '2/91': [2, 22, 19, 98, 78, 81],
                '3/91': [3, 33, 29, 97, 67, 71],
                '4/91': [4, 44, 39, 96, 56, 61],
                '5/91': [5, 55, 49, 95, 45, 51],
                '6/91': [6, 66, 59, 94, 34, 41],
                '7/91': [7, 77, 69, 93, 23, 31],
                '8/91': [8, 88, 79, 92, 12, 21],
                '12/91': [13, 32, 18, 87, 68, 82],
                '13/91': [14, 43, 28, 86, 57, 72],
                '14/91': [15, 54, 38, 85, 46, 62],
                '15/91': [16, 65, 48, 84, 35, 52],
                '16/91': [17, 76, 58, 83, 24, 42],
                '23/91': [25, 53, 27, 75, 47, 73],
                '24/91': [26, 64, 37, 74, 36, 63],
                '1/10': [10, 20, 30, 40, 50, 60, 70, 80, 90]
            },
            additional_factors={
                '1/10': [10, 30, 70, 90],
                '1/5': [20, 40, 60, 80],
                '1/2': [50],
                '1/1': [100]
            }
        )
    
    @staticmethod
    def create_sgram_11() -> SGram:
        """S-Gram 11: s12 [128??] 11/121 = 1/11"""
        return SGram(
            index=11,
            catalan_number=208012,
            numerator=11,
            denominator=121,
            symbolic_notation="[11] = [[5]] = [[((()))]]",
            transformation="[(((())))]",
            formula_parts={'base': 11, 'expansion': 111},
            fraction_patterns={
                '1/111': [1, 12, 10, 120, 109, 111],
                '2/111': [2, 24, 21, 119, 97, 100],
                '3/111': [3, 36, 32, 118, 85, 89],
                '4/111': [4, 48, 43, 117, 73, 78],
                '5/111': [5, 60, 54, 116, 61, 67],
                '6/111': [6, 72, 65, 115, 49, 56],
                '7/111': [7, 84, 76, 114, 37, 45],
                '8/111': [8, 96, 87, 113, 25, 34],
                '9/111': [9, 108, 98, 112, 13, 23],
                '13/111': [14, 35, 20, 107, 86, 101],
                '14/111': [15, 47, 31, 106, 74, 90],
                '15/111': [16, 59, 42, 105, 62, 79],
                '16/111': [17, 71, 53, 104, 50, 68],
                '17/111': [18, 83, 64, 103, 38, 57],
                '18/111': [19, 95, 75, 102, 26, 46],
                '25/111': [27, 58, 30, 94, 63, 91],
                '26/111': [28, 70, 41, 93, 51, 80],
                '27/111': [29, 82, 52, 92, 39, 69],
                '37/111': [40, 81],
                '1/11': [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
            },
            additional_factors={
                '1/1': [121]
            }
        )
    
    @classmethod
    def create_all_sgrams(cls) -> List[SGram]:
        """Create all S-Grams from 0 to 11"""
        return [
            cls.create_sgram_0(),
            cls.create_sgram_1(),
            cls.create_sgram_2(),
            cls.create_sgram_3(),
            cls.create_sgram_4(),
            cls.create_sgram_5(),
            cls.create_sgram_6(),
            cls.create_sgram_7(),
            cls.create_sgram_8(),
            cls.create_sgram_9(),
            cls.create_sgram_10(),
            cls.create_sgram_11(),
        ]
    
    @classmethod
    def create_sgram(cls, index: int) -> SGram:
        """Create a specific S-Gram by index (0-11)"""
        if index < 0 or index > 11:
            raise ValueError(f"S-Gram index must be between 0 and 11, got {index}")
        
        creators = [
            cls.create_sgram_0, cls.create_sgram_1, cls.create_sgram_2,
            cls.create_sgram_3, cls.create_sgram_4, cls.create_sgram_5,
            cls.create_sgram_6, cls.create_sgram_7, cls.create_sgram_8,
            cls.create_sgram_9, cls.create_sgram_10, cls.create_sgram_11,
        ]
        
        return creators[index]()
