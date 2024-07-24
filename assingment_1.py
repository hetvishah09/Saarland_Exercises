####### TASK: 1
# Task 1: Write a function process_list (2 points)
# Write a function process_list that modifies each element in a list and returns the
# maximum value of the modified list.
# Specification
# Name: process_list
# Parameter: list of integers
# Return value: largest number in the list after modification
# Modification:
# 1 If an elements is
# odd, multiply the element by 2;
# even, divide the element by 2.
# 2 If the position in the list is a multiple of 7, add the position to the value.


def process_list(numbers):
    for index in range(len(numbers)):
        print("\n\n\n index===>",index)
        if numbers[index] % 2 == 0:
            numbers[index] = numbers[index] / 2
        else:
            numbers[index] = numbers[index] * 2
        
        if index % 7 == 0:
            numbers[index] += index
    
    return max(numbers)

numbers = [10, 15, 8, 7, 22, 14, 3, 6, 19, 24, 5, 10, 17, 13, 18]
print(process_list(numbers))



################# TASK-2
# Task 2: DNA Reverse Complement (2 points)
# Write a function DNA_complement that takes a string as input and computes its reverse
# DNA complement (A ↔ T, C ↔ G).
# For example, ACGATCGATCGATTC ↔ GAATCGATCGATCGT.
# You can assume that the input string only contains the upper case letters A,C,G,T.

def DNA_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_dna = dna[::-1]
    print("\n\n\n reversed_dna===>",reversed_dna)
    reverse_complement = ''
    
    for letters in reversed_dna:
        print("\n\n\n letters===>",letters)
        reverse_complement += complement.get(letters)
        print("\n\n reversed_complement===>",reverse_complement)
    
    return reverse_complement

dna = "ACGATCGATCGATTC"
print(DNA_complement(dna))
    

################### TASK- 3
# Task 3: Extracting k-mers (substrings of length k) from a DNA sequence (3
# points)
# 1 Write a function list_kmers that, given a DNA sequence s and an integer k,
# returns a list of all k-mers (strings of length k, from left to right, overlapping).
# Handle edge cases correctly (k > |s| ?!).
# 2 Write a function number_of_unique_kmers that, given s and k,
# returns the number of unique k-mers in s (k-mers that appear only once).

def list_kmers(s, k):
    if k > len(s):
        return []
    
    kmers = []
    for i in range(len(s) - k + 1):
        print("\n\n\n i==>", i)
        print("\n\n\n ange==>",range(len(s) - k + 1) )
        kmers.append(s[i:i+k])
    
    return kmers

s = "ACGATCGATC"
k = 3
print(list_kmers(s, k))

def number_of_unique_kmers(s, k):
    kmers = list_kmers(s, k)
    
    kmer_counts = {}
    for kmer in kmers:
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1
    
    unique_count = sum(1 for count in kmer_counts.values() if count == 1)
    
    return unique_count

s = "ACGATCGATC"
k = 3
print(number_of_unique_kmers(s, k))  


############# TASK-4
# Task 4: Integer encoding of k-mers (3 points)
# For a given k, there are 4k different possible k-mers. Let’s encode every k-mer
# bijectively as an integer 0 ≤ c < 4
# k
# Use this encoding: Convert A 7→ 0, C 7→ 1, G 7→ 2, T 7→ 3.
# Interpret the sequence of digits as an integer with base 4.
# Example: ACGT 7→ (0, 1, 2, 3)4 = 0 · 4
# 3 + 1 · 4
# 2 + 2 · 4
# 1 + 3 · 4
# 0 = 16 + 8 + 3 = 27.
# Write a function kmer_code(kmer) that returns the integer encoding of the string
# kmer using bit operations.
# Write a function kmer_decode(code, k) that returns the correct string for a
# given integer encoding and k-mer length k using bit operations.
# Hints:
# Your are not allowed to use any packages, like numpy, in this exercise.


def kmer_code(kmer):
    base4_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    code = 0
    for nucleotide in kmer:
        code = code * 4 + base4_map[nucleotide]
    
    return code

kmer = "ACGT"
print(kmer_code(kmer))


def kmer_decode(code, k):
    base4_rev_map = ['A', 'C', 'G', 'T']
    kmer = ''
    for _ in range(k):
        kmer = base4_rev_map[code % 4] + kmer
        code //= 4
    return kmer


code = 27
k = 4
print(kmer_decode(code, k)) 
