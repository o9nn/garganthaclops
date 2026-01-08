# S-Grams State Transformation Tables

Complete reference for S-Grams (2nd Power N-Grams) from 0 to 11.

---

## S-Gram s1 (Index 0)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 1 |
| Fraction | 0/0 |
| Formula | 1+(1+0)^2 = 1+1+1+1+1 = 2+1 = 5 |
| Symbolic Notation | [0)(0] = [0] ~> [-] = () |
| Transformation | [(][)] = (][)(][) = (-) = () = O |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 0/1 | 0 |

---

## S-Gram s2 (Index 1)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 2 |
| Fraction | 1/1 |
| Formula | 1+(1+1)^2 = 1+2+1+2+4 = 3+4 = 10 |
| Symbolic Notation | [1)(1] = [1] ~> [(0)] = [] |
| Transformation | [)(] = )[()]( = )|( = ][ = I |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 1/1 | 1 |

### Additional Factors

| Divisor | Sequence |
|---------|----------|
| 1/1 | 1 |

---

## S-Gram s3 (Index 2)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 5 |
| Fraction | 1/2 |
| Formula | 1+(1+2)^2 = 1+3+1+3+9 = 4+9 = 17 |
| Symbolic Notation | [2)(1] = [2] ~> [([1])] = [([])] |
| Transformation | [()] = [(][)] = [(I)] = IO |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 1/3 | 1, 3 |
| 1/2 | 2 |

### Additional Factors

| Divisor | Sequence |
|---------|----------|
| 1/1 | 4 |

---

## S-Gram s4 (Index 3)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 14 |
| Fraction | 1/3 |
| Formula | 1+(1+3)^2 = 1+4+1+4+16 = 5+16 = 26 |
| Symbolic Notation | [3)(1] = [3] ~> [([2])] = [([()])] |
| Transformation | [(())] |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 1/7 | 1, 4, 2, 8, 5, 7 |
| 1/3 | 3, 6 |

### Additional Factors

| Divisor | Sequence |
|---------|----------|
| 1/1 | 9 |

---

## S-Gram s5 (Index 4)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 42 |
| Fraction | 1/4 |
| Formula | 1+(1+4)^2 = 1+5+1+5+25 = 6+25 = 37 |
| Symbolic Notation | [4] = [2][2] = [(1)][(1)] |
| Transformation | [()][()] = [()()] |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 1/13 | 1, 5, 3, 15, 11, 13 |
| 2/13 | 2, 10, 7, 14, 6, 9 |
| 1/4 | 4, 8, 12 |

### Additional Factors

| Divisor | Sequence |
|---------|----------|
| 1/4 | 4, 12 |
| 1/2 | 8 |
| 1/1 | 16 |

---

## S-Gram s6 (Index 5)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 132 |
| Fraction | 1/5 |
| Formula | 1+(1+5)^2 = 1+6+1+6+36 = 7+36 = 50 |
| Symbolic Notation | [5] ~> [([3])] = [([(())])] |
| Transformation | [((()))] |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 1/21 | 1, 6, 4, 24, 19, 21 |
| 2/21 | 2, 12, 9, 23, 13, 16 |
| 3/21 | 3, 18, 14, 22, 7, 11 |
| 7/21 | 8, 17 |
| 1/5 | 5, 10, 15, 20 |

### Additional Factors

| Divisor | Sequence |
|---------|----------|
| 1/1 | 25 |

---

## S-Gram s7 (Index 6)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 429 |
| Fraction | 1/6 |
| Formula | 1+(1+6)^2 = 1+7+1+7+49 = 8+49 = 65 |
| Symbolic Notation | [6] = [2][3] = [()][(())] |
| Transformation | [()(())] |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 1/31 | 1, 7, 5, 35, 29, 31 |
| 2/31 | 2, 14, 11, 34, 22, 25 |
| 3/31 | 3, 21, 17, 33, 15, 19 |
| 4/31 | 4, 28, 23, 32, 8, 13 |
| 8/31 | 9, 20, 10, 27, 16, 26 |
| 1/6 | 6, 12, 18, 24, 30 |

### Additional Factors

| Divisor | Sequence |
|---------|----------|
| 1/6 | 6, 30 |
| 1/3 | 12, 24 |
| 1/2 | 18 |
| 1/1 | 36 |

---

## S-Gram s8 (Index 7)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 1430 |
| Fraction | 1/7 |
| Formula | 1+(1+7)^2 = 1+8+1+8+64 = 9+64 = 82 |
| Symbolic Notation | [7] = [([4])] = [([()()])] |
| Transformation | [(()())] |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 1/43 | 1, 8, 6, 48, 41, 43 |
| 2/43 | 2, 16, 13, 47, 33, 36 |
| 3/43 | 3, 24, 20, 46, 25, 29 |
| 4/43 | 4, 32, 27, 45, 17, 22 |
| 5/43 | 5, 40, 34, 44, 9, 15 |
| 9/43 | 10, 23, 12, 39, 26, 37 |
| 10/43 | 11, 31, 19, 38, 18, 30 |
| 1/7 | 7, 14, 21, 28, 35, 42 |

### Additional Factors

| Divisor | Sequence |
|---------|----------|
| 1/1 | 49 |

---

## S-Gram s9 (Index 8)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 4862 |
| Fraction | 1/8 |
| Formula | 1+(1+8)^2 = 1+9+1+9+81 = 10+81 = 101 |
| Symbolic Notation | [8] = [2][2][2] = [3[2]] = [()][()][()]  |
| Transformation | [()()()] |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 1/57 | 1, 9, 7, 63, 55, 57 |
| 2/57 | 2, 18, 15, 62, 46, 49 |
| 3/57 | 3, 27, 23, 61, 37, 41 |
| 4/57 | 4, 36, 31, 60, 28, 33 |
| 5/57 | 5, 45, 39, 59, 19, 25 |
| 6/57 | 6, 54, 47, 58, 10, 17 |
| 10/57 | 11, 26, 14, 53, 38, 50 |
| 11/57 | 12, 35, 22, 52, 29, 42 |
| 12/57 | 13, 44, 30, 51, 20, 34 |
| 19/57 | 21, 43 |
| 1/8 | 8, 16, 24, 32, 40, 48, 56 |

### Additional Factors

| Divisor | Sequence |
|---------|----------|
| 1/8 | 8, 24, 40, 56 |
| 1/4 | 16, 48 |
| 1/2 | 32 |
| 1/1 | 64 |

---

## S-Gram s10 (Index 9)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 16796 |
| Fraction | 1/9 |
| Formula | 1+(1+9)^2 = 1+10+1+10+100 = 11+100 = 122 |
| Symbolic Notation | [9] = [3][3] = [2[3]] = [(())][(())] |
| Transformation | [(())(())] |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 1/73 | 1, 10, 8, 80, 71, 73 |
| 2/73 | 2, 20, 17, 79, 61, 64 |
| 3/73 | 3, 30, 26, 78, 51, 55 |
| 4/73 | 4, 40, 35, 77, 41, 46 |
| 5/73 | 5, 50, 44, 76, 31, 37 |
| 6/73 | 6, 60, 53, 75, 21, 28 |
| 7/73 | 7, 70, 62, 74, 11, 19 |
| 11/73 | 12, 29, 16, 69, 52, 65 |
| 12/73 | 13, 39, 25, 68, 42, 56 |
| 13/73 | 14, 49, 34, 67, 32, 47 |
| 14/73 | 15, 59, 43, 66, 22, 38 |
| 21/73 | 23, 48, 24, 58, 33, 57 |
| 1/9 | 9, 18, 27, 36, 45, 54, 63, 72 |

### Additional Factors

| Divisor | Sequence |
|---------|----------|
| 1/9 | 9, 18, 36, 45, 63, 72 |
| 1/3 | 27, 54 |
| 1/1 | 81 |

---

## S-Gram s11 (Index 10)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 58786 |
| Fraction | 1/10 |
| Formula | 1+(1+10)^2 = 1+11+1+11+121 = 12+121 = 145 |
| Symbolic Notation | [10] = [2][5] = [()][((()))] |
| Transformation | [()((()))] |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 1/91 | 1, 11, 9, 99, 89, 91 |
| 2/91 | 2, 22, 19, 98, 78, 81 |
| 3/91 | 3, 33, 29, 97, 67, 71 |
| 4/91 | 4, 44, 39, 96, 56, 61 |
| 5/91 | 5, 55, 49, 95, 45, 51 |
| 6/91 | 6, 66, 59, 94, 34, 41 |
| 7/91 | 7, 77, 69, 93, 23, 31 |
| 8/91 | 8, 88, 79, 92, 12, 21 |
| 12/91 | 13, 32, 18, 87, 68, 82 |
| 13/91 | 14, 43, 28, 86, 57, 72 |
| 14/91 | 15, 54, 38, 85, 46, 62 |
| 15/91 | 16, 65, 48, 84, 35, 52 |
| 16/91 | 17, 76, 58, 83, 24, 42 |
| 23/91 | 25, 53, 27, 75, 47, 73 |
| 24/91 | 26, 64, 37, 74, 36, 63 |
| 1/10 | 10, 20, 30, 40, 50, 60, 70, 80, 90 |

### Additional Factors

| Divisor | Sequence |
|---------|----------|
| 1/10 | 10, 30, 70, 90 |
| 1/5 | 20, 40, 60, 80 |
| 1/2 | 50 |
| 1/1 | 100 |

---

## S-Gram s12 (Index 11)

### Basic Information

| Property | Value |
|----------|-------|
| Catalan Number | 208012 |
| Fraction | 1/11 |
| Formula | 1+(1+11)^2 = 1+12+1+12+144 = 13+144 = 170 |
| Symbolic Notation | [11] = [[5]] = [[((()))]] |
| Transformation | [(((())))] |

### Fraction Patterns

| Divisor | Sequence |
|---------|----------|
| 1/111 | 1, 12, 10, 120, 109, 111 |
| 2/111 | 2, 24, 21, 119, 97, 100 |
| 3/111 | 3, 36, 32, 118, 85, 89 |
| 4/111 | 4, 48, 43, 117, 73, 78 |
| 5/111 | 5, 60, 54, 116, 61, 67 |
| 6/111 | 6, 72, 65, 115, 49, 56 |
| 7/111 | 7, 84, 76, 114, 37, 45 |
| 8/111 | 8, 96, 87, 113, 25, 34 |
| 9/111 | 9, 108, 98, 112, 13, 23 |
| 13/111 | 14, 35, 20, 107, 86, 101 |
| 14/111 | 15, 47, 31, 106, 74, 90 |
| 15/111 | 16, 59, 42, 105, 62, 79 |
| 16/111 | 17, 71, 53, 104, 50, 68 |
| 17/111 | 18, 83, 64, 103, 38, 57 |
| 18/111 | 19, 95, 75, 102, 26, 46 |
| 25/111 | 27, 58, 30, 94, 63, 91 |
| 26/111 | 28, 70, 41, 93, 51, 80 |
| 27/111 | 29, 82, 52, 92, 39, 69 |
| 37/111 | 40, 81 |
| 1/11 | 11, 22, 33, 44, 55, 66, 77, 88, 99, 110 |

### Additional Factors

| Divisor | Sequence |
|---------|----------|
| 1/1 | 121 |

---
