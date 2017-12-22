#! python
# work with strings

# Strings can be concatenated (glued together) with the + operator, and repeated with *: 


word = 'Help' + 'A'
print ('word')

print '<' + word*5 + '>'

# Two string literals next to each other are automatically concatenated; 
# the first line above could also have been written "word = 'Help' 'A'"; 
# this only works with two literals, not with arbitrary string expressions: 

st='str' 'ing'             #  <-  This is ok
print st
st='str'.strip() + 'ing'   #  <-  This is ok
print st

# Strings can be subscripted (indexed); like in C, the first character of a string 
# has subscript (index) 0. There is no separate character type; a character is 
# simply a string of size one. Like in Icon, substrings can be specified with 
# the slice notation: two indices separated by a colon. 

print word[4]

print word[0:2]

print word[2:4]

# Slice indices have useful defaults; an omitted first index defaults to zero, 
# an omitted second index defaults to the size of the string being sliced. 

print word[:2]    # The first two characters
print word[2:]    # All but the first two characters

# Python strings cannot be changed. Assigning to an indexed position in the string results in an error: 
# However, creating a new string with the combined content is easy and efficient: 

print 'x' + word[1:]

print 'Splat' + word[4]

# Here's a useful invariant of slice operations: s[:i] + s[i:] equals s. 

print word[:2] + word[2:]

print word[:3] + word[3:]


# Degenerate slice indices are handled gracefully: an index that is too large is replaced 
# by the string size, an upper bound smaller than the lower bound returns an empty string. 

print word[1:100]

print word[10:]

print word[2:1]


# Indices may be negative numbers, to start counting from the right. For example: 


print word[-1]     # The last character

print word[-2]     # The last-but-one character

print word[-2:]    # The last two characters

print word[:-2]    # All but the last two characters


# But note that -0 is really the same as 0, so it does not count from the right! 

print word[-0]     # (since -0 equals 0)

# Out-of-range negative slice indices are truncated, but don't try this for single-element (non-slice) indices: 

print word[-100:]

# print word[-10]    # error

#The best way to remember how slices work is to think of the indices as pointing between characters, 
#with the left edge of the first character numbered 0. Then the right edge of the last character 
#of a string of n characters has index n, for example: 

# +---+---+---+---+---+ 
# | H | e | l | p | A |
# +---+---+---+---+---+ 
# 0   1   2   3   4   5 
#-5  -4  -3  -2  -1


s = 'supercalifragilisticexpialidocious'
print s
print len(s)
