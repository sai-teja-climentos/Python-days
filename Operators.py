# ========================================================
# 1. Arithmetic Operators
# ========================================================

# + (Addition)
# a = 10
# b = 20

# c = a + b

# print(c)


# - (Subtraction)
# a = 10
# b = 20

# c = b - a

# print(c)

# * (Multiplication)
# a = 10
# b = 20

# c = a * b

# print(c)

# / (Division)
# a = 10
# b = 20

# c = b / a

# print(c)

# % (Modulus)
# a = 10
# b = 20

# c = b % a

# print(c)

# ** (Exponent)
# a = 10
# b = 14

# c = a ** b

# print(c)


# // (Floor Division)

# a = 20
# b = 30

# c = a // b

# print(c)


# ========================================================
# 2. Comparison (Relational) Operators
# ========================================================
# == (Equal to)

# a = 10
# b = 20

# c = a == b
# print(c)

# != (Not equal to)
# a = 10
# b = 20

# c = a != b
# print(c)

# > (Greater than) < (Less than)
# a = 10
# b = 20
# c = a < b
# d = a > b

# print(c)
# print(d)

# >= (Greater than or equal to) <= (Less than or equal to)

# a = 10
# b = 10

# c = a >= b
# d = a <= b

# print(c)
# print(d)

# ========================================================
# 3. Logical Operators
# ========================================================
# and → True if both conditions are true
# a = 10
# b = 12

# c = (b==0) != a  and (a==10000) != a

# print(c)
# or → True if at least one condition is true
# a = 10
# b = 12

# c =  a==11 or a<=10

# print(c)


# not → Reverses the result

# a = 12
# b = 12

# c = not (a <= b)

# print(c)

# =======================================
# 4. Assignment Operators
# =======================================

# a = 10
# b = a
# b //= a

# print(b)

# =======================================
# 5. Identity Operators
# =======================================
# # is → True if both variables refer to the same object
# a = [10, 10]
# b = a

# print(a is b)  

# # Used to test if a value exists in a sequence.
# a = [10, 10]
# b = [10, 10]

# print(a is not b)  

# =======================================
# 6. Membership Operators
# =======================================
# Used to test if a value exists in a sequence.

# in → True if value is present
# a = [10, 20, 30, 40]

# print(31 in a)

# b = ["A", "B", "C"]

# print("C" in b)

# not in → True if value is not present
# a = [10, 20, 30, 40]

# print(31 not in a)

# b = ["A", "B", "C"]

# print("C" not in b)

# =======================================
# 7. Bitwise Operators
# =======================================

# Work on binary (bits) of numbers.
# & (AND)
# Returns 1 only if both bits are 1.
# a = 14 # 1110
# b = 15 # 1111

#        # 1110         

# print(a & b)

# | (OR)
# Bitwise OR (|)
# Returns 1 if at least one bit is 1.

# a = 7  # 0111
# b = 10 # 1010

#        # 1111         

# print(a | b)

# ^ (XOR)
# Bitwise XOR (^)

# Returns 1 if bits are different.

# a = 5  # 0101
# b = 3  # 0011

#        # 0110     

# print(a ^ b)

# Reverses all bits.
# ~ (NOT)
# Bitwise NOT (~)
# a = -1  # -

# print(~a)  #~n = -(n+1)
 

# << (Left shift)
# Left Shift (<<)

# Shifts bits to the left.


#number << positions
# number → the value to shift
# positions → how many places to shift left

# Main Concept

# Every left shift by 1 position means:

# Multiply the number by 2

# Every left shift by 2 positions means:

# Multiply the number by 4

# Because:

# 2^n

# Where n = shift positions.

# Quick Examples Table
# Expression BinaryResult	Decimal
# 5 << 1	00001010	10
# 5 << 2	00010100	20
# 5 << 3	00101000	40
# 3 << 2	00001100	12

# a = 5  # 0101

# print(a << 8 )

# >> (Right shift)

# Step 1: Convert 5 to Binary
# 5 = 00000101
# Step 2: Shift Left by 1
# 00000101  →  00001010

# Result:

# 00001010 = 10

# So:

# 5 << 1 = 10

# a = 10  # --

# print(a >> 1 )






