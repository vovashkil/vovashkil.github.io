#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue"> Regular Expressions
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # Regular expressions introduction
# **Regular expressions** make use of **literal characters and special characters** to match patterns in strings. We will examnine a number of them here through examples.

# ## Regular expressions in Python
# **Python's built-in re module**, part of the Python Standard Library, provides a **comprehensive suite of functions** for working with **regular expressions**. You can view the **full documention** for the re module **here: https://docs.python.org/3/library/re.html**

# In[ ]:


import re


# ### Python re functions
# There are a number of functions supported in the re module. We will look more into them later, but for now, we'll introduce a few that will be used in our first few demos:
# - **re.search** - Returns the **first occurrence of a pattern** anywhere in the target string.
# - **re.findall** - Returns a **list containing all matches** in the target string.
# 
# For most of the examples I'll use the findall function, because it let's me show examples of multiple matches in the same target string. I'll also use search later on.

# ### Match Object
# Many of the **Python re functions**, including *search*, will **return** one or more **Match object** in their result. The Match object encpasulates the information about the search and the result.
# 
# The **Match object** has functions to return these **key properties**:
# - **span()** - returns a **tuple containing** the **start and end positions of** the **match**
# - **string** - returns the **string passed** into the function
# - **group()** - returns the **part(s) of** the **string where** the **match was found**
# 
# We will discuss groups later in the notebook.

# ## Refresher - Python Raw Strings
# We will see later that there are **many cases** where we **need to use** the **backslash character ("\\")** to **express** different **things in regular expressions**. The problem is, **"\\"** is **also used for many things in Python strings**, such as indicating new lines ("\\n"), tabs ("\\t") or escapaing other special characters. In fact a plain "\\" won't even print in a Python string (you would need to use "\\\\\\").
# 
# **In order** to have the **"\\" to be left as is**, so it can be used in RegEx expressions, we **use** a the Python feature of a **"raw string"**. This is not something specific to regular expressions, but it's useful here. In a raw string, all characters are interpreted literally. **Raw strings** are **denoted with an "r" preceeding the string**, so ***r"Hello"*** is a raw string.
# 
# Let's look at some examples.

# In[ ]:


# string with new line
regular_string = "Hello\nMy name is Fernando"
raw_string = r"Hello\nMy name is Fernando"

# print regular and raw strings
print(regular_string)
print("----------------------")
print(raw_string)


# In[ ]:


# String with \b, which has a special meaning for regular expressions. 
regular_string = "In regular expressions, \b represents the beginning of a word"
raw_string = r"In regular expressions, \b represents the beginning of a word"

# print regular and raw strings
print(regular_string)
print("----------------------")
print(raw_string)


# In most cases, I'm using regular strings in my examples. But from time to time, as needed, I also use raw strings. Generally I use it when I need to use backslash in my pattern.

# # Regular Expression Constructs
# We will look at the various constructs used for regular expressions using examples. In most cases, we'll look at them individually. Later, we'll look at various examples of combining them to make complex patterns.

# ## Literal Characters
# Literal characters, also known as ordinary characters, match exactly what they represent and have a literal meaning in RegEx.

# #### Examples

# ##### Success case

# In[ ]:


# Target text
target_text = "Outbreak"

# RegEx search pattern
pattern = "break"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ##### Fail case

# In[ ]:


# Target text
target_text = "Coma"

# RegEx search pattern
pattern = "Comma"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Case sensitivity
# **By default, searches will be case sensitive**. When we look at re flags later, we'll see how we can change that. But for now, we can assume our examples are case sensitive.

# In[ ]:


# Target text
target_text = "Replay"

# RegEx search pattern
pattern = "replay"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ## Character Sets
# To define a character set, place a group of characters inside square brackets. They will match any one of these characters in the text. 

# ### Simple sets

# #### Examples

# ##### Success case

# In[ ]:


# Target text
target_text = "The Dragon Reborn"

# RegEx search pattern
pattern = "[Tgbx]"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ##### Fail case

# In[ ]:


# Target text
target_text = "The Dragon Reborn"

# RegEx search pattern
pattern = "[ABC]"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Mixing cases and digits

# #### Examples

# In[ ]:


# Target text
target_text = "4.50 from Paddington"

# RegEx search pattern
pattern = "[4fqd]"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# In[ ]:


# Target text
target_text = "Ysabel"

# RegEx search pattern
pattern = "[Y1BLe]"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Combining sets and literals in longer patterns
# In the previous examples, we were matching a single character based on a set. But we can look for a longer string pattern based on a combination of sets and literals.

# #### Examples

# In[ ]:


# Target text
target_text = "Ready player one"

# RegEx search pattern
pattern = "pl[abc][wyz]er"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# In[ ]:


# Target text
target_text = "Elantris"

# RegEx search pattern
pattern = "[E123]lan[rst987]"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ## Character Ranges
# A character range is similar to a character set, but it simplifies the notation for common range of characters. 

# ### Simple ranges

# #### Examples

# In[ ]:


# Target text
target_text = "Dune"

# RegEx search pattern
pattern = "[A-Z]"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# In[ ]:


# Target text
target_text = "2010: Odyssey Two"

# RegEx search pattern
pattern = "[0-9]"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Combining ranges, sets, and literals

# #### Examples

# In[ ]:


# Target text
target_text = "The Martian"

# RegEx search pattern
pattern = "[A-Z]h[12345abcde] [A-Za-z]artia[a-z0-9]"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ## Negative Sets and Ranges ([^...])
# **Sometimes** you may **need to express** that a **pattern does NOT include a character, or set of characters**. You **can do** that by **using the format [^ ]**. Note that the "^" only has that behavior when used right after the opening "[", because we'll see "^" being used for a different purpose later.

# ### Negating a set

# #### Examples

# ##### Success case

# In[ ]:


# Target text
target_text = "Divergent"

# RegEx search pattern
pattern = "[^IA]iver"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **This worked** because the first "D" in Divergent was neither "I" or "A"

# ##### Fail case

# In[ ]:


# Target text
target_text = "Insurgent"

# RegEx search pattern
pattern = "[^IA]nsurg"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **This failed** because the first "I" in Insuregen was excluded by the [^IA] in the pattern.

# ### Negating a range

# #### Examples

# ##### Success case

# In[ ]:


# Target text
target_text = "1984"

# RegEx search pattern
pattern = "[^A-Za-z]"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **This matched everything**, because it's a rare **title with no characters**.

# In[ ]:


# Target text
target_text = "Flight 714 to Sydney"

# RegEx search pattern
pattern = "[^0-9]"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# And this one **excluded all the digits**.

# ## Quantifiers
# Quantifiers **allow a pattern to apply to a different numbers of characters**.

# ### Dot (.)
# **Matches any single character**, except for a newline character (\n)

# #### Examples

# In[ ]:


# Target text
target_text = "Without Remorse"

# RegEx search pattern
pattern = "Wit.out"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# In[ ]:


# Target text
target_text = "The mirror of her dreams"

# RegEx search pattern
pattern = ".r"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Question mark (?)
# **Matches the preceding character, group, or character** class either **zero or one time**.

# #### Examples

# In[ ]:


# Target text
target_text = "And then there was none"

# RegEx search pattern
pattern = "the[n]?"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Asterisk (*)
# **Matches zero or more occurrences** of the preceding **character, group, or character class**

# #### Examples

# In[ ]:


# Target text
target_text = "The name of the Wind"

# RegEx search pattern
pattern = "[A-Z][a-z]* "

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# In[ ]:


# Target text
target_text = "Rebecca"

# RegEx search pattern
pattern = "[A-Z][12345]*[a-z]*"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **Notice** in we **didn't have character in** the **[12345]** set, **but that works for "*"**, because "*" is for **ZERO** or more occurrances.

# ### Plus sign (+)
# **Matches one or more occurrences** of the preceding **character, group, or character class**. So this is similar to "*", but there needs to be at least one match.

# #### Examples

# ##### Success case

# In[ ]:


# Target text
target_text = "The Word"

# RegEx search pattern
pattern = "[A-Z]+"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ##### Fail case

# In[ ]:


# Target text
target_text = "It"

# RegEx search pattern
pattern = "[0-9]+It"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Brace quantifier ({n})
# Matches a **specific number occurrences** of the preceding element. There are three variations:
# - **{n}** - Matches exactly n occurrences of the preceding element
# - **{n,}** - Matches at least n occurrences of the preceding element
# - **{m,n}** - Matches between m and n occurrences of the preceding element

# #### {n} - Exactly *n* occurances

# ##### Success case

# In[ ]:


# Target text
target_text = "Hotel"

# RegEx search pattern
pattern = "[A-Za-z]{5}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ##### Fail case

# In[ ]:


# Target text
target_text = "Hotel"

# RegEx search pattern
pattern = "[A-Za-z]{6}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# #### {m,n} - Between *m* and *n* occurances

# ##### Success case

# In[ ]:


# Target text
target_text = "The Path of Daggers"

# RegEx search pattern
pattern = "[A-Za-z]{4,7}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ## Special Character Sequences with backslash
# We've see sets and ranges as a way to specify valid combination of characters. **For some common combinations**, we can also **use special sequences using a backslash "\\"**.
# - **\w** searches for alphanumeric characters (including the underscore), serving as a shorthand for [a-zA-Z0-9_].
# - **\d** searches for digits in a target, serving as shorthand for the zero through nine character set [0-9].
# - **\A** matches the expression at the start of a string, whether single-line or multi-line.
# - **\b** matches the empty string at the word boundary, either at the beginning or the end of a word.
# - **\B** matches positions where \b does not, typically within words.
# - **\D** matches any non-digit character, equivalent to [^0-9].
# - **\s** matches any whitespace character, including tab (\t), newline (\n), return (\r), and space.
# - **\S** matches any non-whitespace character.
# - **\W** matches non-alphanumeric characters, equivalent to [^a-zA-Z0-9].
# - **\Z** matches the position at the end of a string.
# 
# We'll look at some examples here, and other ones in context later.

# ### Alphanumerics: \w
# Searches for alphanumeric characters (including the underscore), serving as a **shorthand for [a-zA-Z0-9_].**

# #### Examples

# In[ ]:


# Target text
target_text = "Ender's Game"

# RegEx search pattern
pattern = r"\w"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **Note** the apostrophe was not matched.

# ### Digits: \d
# \d searches for digits in a target, serving as shorthand for the zero through nine character set [0-9].

# #### Examples

# In[ ]:


# Target text
target_text = "11/22/63"

# RegEx search pattern
pattern = r"\d"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### White Space: \s
# **\s** matches any whitespace character, including tab (\t), newline (\n), return (\r), and space.

# #### Examples
# In this example, we are looking for **words sourrounded by spaces**. We use the "+" quantifier we saw earlier.

# In[ ]:


# Target text
target_text = "The Other Side of Midnight"

# RegEx search pattern
pattern = r"\s\w+\s"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **Note** that the words "Side" was not found, even though it is sorrounded by spaces. Why is that? That's because when the regular expression used the space after the word "Other" for its match. That space cannot be reused for another match. Later on, we'll see a better way to capture words.

# ## Non-alphanumeric characters
# Most of the examples I'm showing are for regular alpha-numeric strings. However **ponctuations, and other special characters can** definitely **be specified in regular expressions**. Some special characters are used as part of regular expressions, so they will have to be escaped (we'll see that). The ability of **matching special characters** is **important** in **many practical examples** we'll show later.
# 
# For now, I'll just show some basic examples of matches non alpha-numeric chracters.

# ### Examples
# #### Examples with literal match

# In[ ]:


# Target text
target_text = "Emails need a @ in them"

# RegEx search pattern
pattern = r"@"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# In[ ]:


# Target text
target_text = "What about - , ; = & and other ones?"

# RegEx search pattern
pattern = r"[-,;=&]"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# #### Examples using \W
# \W matches non-alphanumeric characters, equivalent to [^a-zA-Z0-9].

# In[ ]:


# Target text
target_text = "A bunch of them: %, @, :, &, ), ; , etc"

# RegEx search pattern
pattern = r"\W"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ## Anchors
# Anchor metacharacters specify **where to look for a pattern string within a target string**.

# ### Caret (^)
# **Indicates** that the following **pattern must appear at the beginning** of the string or line

# #### Example

# In[ ]:


# Target text
target_text = "The Eye of the World"

# RegEx search pattern
pattern = "^[Tt]he"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# Note that it **matched only** the **first "The" at the beginning of the string**, with the capital T, but not the second.

# ### Dollar sign ($)
# **Indicates** that the following **pattern must appear at the end** of the string or line

# #### Examples

# ##### Success case

# In[ ]:


# Target text
target_text = "Master of the Game"

# RegEx search pattern
pattern = "Game$"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ##### Fail case

# In[ ]:


# Target text
target_text = "A Game of Thrones"

# RegEx search pattern
pattern = "Game$"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ## Word Boundaries
# Word boundaries denote the **start and end of a word**. Similar to the anchors, they don't match a specific character, but simply help mark the position of matched characters.

# ### Word begin/end (\b)
# \b Indicates a match where characters are at the beginning or end of a word.

# #### Examples

# In[ ]:


# Target text
target_text = "red rackham's treasure"

# RegEx search pattern
pattern = r"\br.."

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **Note** that we matched the "r" in "**r**ed**" and the "r" "**r**ackham", because they were the start of a word, but neither "r" in "Treasure", because they were in the middle.

# In[ ]:


# Target text
target_text = "the secret of the unicorn"

# RegEx search pattern
pattern = r"...t\b"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **Note** that we matched the "t" in "secret" because it was at the end of a word, but not the "t" in "the".

# #### Comparing with \s for finding words
# As you might recall, in a previous example we used the pattern "\s\w+\s" similarly to find words. That worked ok, but some words were not found, because a space used in one pattern couldn't be reused in the next. That's not the case with \b. It only marks the beging/end of the word, but does not need to capture a space around it.

# In[ ]:


# Target text
target_text = "The Other Side of Midnight"

# RegEx search pattern
pattern = r"\b\w+\b"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# Using **\b, all the words are found**.

# ### Word does not begin/end (\B)
# **\B is the opposite of \b**. It indicates a match where characters are NOT at the beginning or end of a word. We'll use the same example, so you can see we'll get the opposite matches.

# #### Examples

# In[ ]:


# Target text
target_text = "red rackham's treasure"

# RegEx search pattern
pattern = r"\Br.."

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# In[ ]:


# Target text
target_text = "the secret of the unicorn"

# RegEx search pattern
pattern = r"...t\B"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ## Using Backslash (\\) as Escape Character
# With **seen a number of special characters** used for various purposes in regular expressions (*, +, ^, ?, etc). But **what if** the **pattern you are looking for includes** one of those **special characters**?
# 
# The **backlash "\\" character**, referred in this context as a **escape character**, specifies that the **character should be taken literaly**.

# ### Example: searching for a question
# Assume you are **trying to match** a **question in a string**.

# #### Without "\\"
# First we try a pattern **"^[A-Za-z0-9\ ']\*?"**, which attempts to look for **any combination of alphanumerical characters, spaces or apostrophe following by a question.**

# In[ ]:


# Target text
target_text = "The Firm"

# RegEx search pattern
pattern = r"^[A-Za-z0-9' ]*?"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# In[ ]:


# Target text
target_text = "The Firm"

# RegEx search pattern
pattern = r"^[A-Za-z0-9' ]*?"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# That **incorrectly returned a match**, even though this wasn't a question. That's because the "?" was interpreted as the special RegEx character that matches zero or one occurrance.

# #### With "\\"
# Now we try the **same pattern**, but we **add the "\" to escape the "?" character**. This will for the RegEx to look for the literal character "?"

# #### Fail case

# In[ ]:


# Target text
target_text = "The Firm"

# RegEx search pattern
pattern = r"^[A-Za-z0-9' ]*\?"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# This time we **did not match, which is correct** since this wasn't a question.

# #### Success case
# Let's make sure that we can match a sentence with a question.

# In[ ]:


# Target text
target_text = "Why didn't they ask Evans?"

# RegEx search pattern
pattern = r"^[A-Za-z0-9' ]*\?"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# Yep that works.

# ## Alternation using pipe (|)
# **Matches either** of the **expressions** appearing before or after the pipe

# #### Examples

# In[ ]:


# Target text
target_text = "The Chronicles of Thomas Covenant"

# RegEx search pattern
pattern = "Tom|Thomas"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ## Groups
# Groups allow you to break up your pattern into multiple parts. Each part can be evaluated separately, and you can view the results separately for each when needed. There are two variations of groups:
# - **Capturing groups** - In a capturing group, the regular expression will maintain the individual matches per group in the mattern
# - **Non-capturing groups** - A non-capturing group will still have different groups in the patterm, wit mostly the same syntax, but it will not maintain seperate results.
# 
# It's one of the more complex topics in regular expressions, so let's look at a few examples. 

# ### Group results with findall and search
# We have been using the findall function for most of our examples, but we will also look at some examples with search later.  ***findall()*** and ***search()*** will show group results differently:
# - **findall** returns a list of tuples for each result matching the groups
# - **search** always returns a ***Match*** object. Withing that object, you can call the *groups()* method to get a tuple with all the group results, or the group() call passing a group number to retrieve a specific group result.

# ### Example: Capturing characters and numbers separately
# In this example, let's assume we have a list of people's names and ages. We don't know how they were separated (using ",", "-", ":" or anything else. So we want to match strings and numbers only, being able to track them separately.

# #### *findall()* example

# In[ ]:


# Target text
target_text = "Jane Doe: 25, Juan Li - 30, Kwesi Manu/23, Saanvi Sarkar: 19"

# RegEx search pattern
# \w+\s*\w* matches names
# \W+ matches at least on non-alphanumeric separator
# \d matches digits
pattern = r"(\w+\s*\w*)\W+(\d+)"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')

    # print individual group results
    print('\nIndividual group results: ')
    for i in range(len(result[0])):
        group_result = [item[i] for item in result]
        print(f'- Result group {i+1}: {group_result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# #### *search()* example
# Remember that *search* only returns the first match, as a Match object.

# In[ ]:


# Target text
target_text = "Jane Doe: 25, Juan Li - 30, Kwesi Manu/23, Saanvi Sarkar: 19"

# RegEx search pattern
# (\w+\s*\w*) matches names
# \W+ matches at least on non-alphanumeric separator
# (\d) matches digits
pattern = r"(\w+\s*\w*)\W+(\d+)"

# Find all occurrances of pattern and check result
result = re.search(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"') 
    print(f'- Matched string: {result.groups()}')
    
    # print individual group results
    print('\nIndividual group results: ')
    for i in range(len(result.groups())):
        print(f'- Result group {i+1}: {result.group(i+1)}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Example: Capturing appointments with month, day, year, hour and minute
# In this example, let's assume we have a **list of appointments in the following CSV format**: 
# - ***\<appointment title>, \<date as mm/dd/yyyy>, \<time as hh24:mi>***
# 
# I want to be able to match the format, and also extract each component separately.
# 

# #### *findall()* example

# In[ ]:


# Target text
target_text = "\n\
Tucker's vet,10/03/2024,14:30\n\
Tucker and Finn,09/15/2023,16:20\n\
Bathe Moose,9/4/2024,09:00\n\
Finn pills,9/7/2024,13:45"

# RegEx search pattern
# (([a-zA-Z]+[\w ']*) matches something that starts with a letter, and continues with alphanumeric, apostrophe or spaces
# , (used multuple times) will match the literal "," used as a separator
# (\d{1,2}/\d{1,2}/\d{4}) matches a date, where the days and months can be 1 or 2 digits, and the year is expected as 4 digits
# (\d{1,2}:\d{2}) matches a time in 24 hour format, where the hour can be 
pattern = r"([a-zA-Z]+[\w ']*),(\d{1,2}/\d{1,2}/\d{4}),(\d{1,2}:\d{2})"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')

    # print individual group results
    print('\nIndividual group results: ')
    for i in range(len(result[0])):
        group_result = [item[i] for item in result]
        print(f'- Result group {i+1}: {group_result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Backreferences
# Backreferences allow you to **reference and reuse** the **text captured by a group** within the same regex pattern. This is useful if a text includes repeated patterns you want to identify.

# #### Example: Finding duplicate words
# Most of us have encountered the scenario where a grammar check warns us that we have a **repeated word in a sentence**. How can you implement that check using regular expressions?

# In[ ]:


# Target text
target_text = "There are so many different different RegEx constructs. This notebook is getting huge."

# RegEx search pattern
# (\w+) will match a word
# \s+ ensures we match one or more spaces
# \1 will look for that same word imediatelly following
pattern = r"(\w+)\s+\1"

# Find all occurrances of pattern and check result
result = re.search(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"') 
    
    # print individual group results
    print('\nGroup results: ')
    for i in range(len(result.groups())):
        print(f'- Result group {i+1}: {result.group(i+1)}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Non-capturing groups
# **Non-apturing groups** will **work largely the same way**, **but** they **won't record** the **individual results of groups**. But you can still use them to group parts of the pattern, and apply other constructs on them.
# 
# The example below is intentionally the same one I used early, but not that I simply a **"?:" at the beginning of each group**. That is the **notation** you use **to indicate** this is a **non-capturing group**. I removed the additional print statements for the individual group results, because they wouldn't work here, since the information is not kept for the groups.

# In[ ]:


# Target text
target_text = "Jane Doe: 25, Juan Li - 30, Kwesi Manu/23, Saanvi Sarkar: 19"

# RegEx search pattern
# \w+\s*\w* matches names
# \W+ matches at least on non-alphanumeric separator
# \d matches digits
pattern = r"(?:\w+\s*\w*)\W+(?:\d+)"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ## Greety vs lazy quantifiers
# **Quantifiers** in regular expressions are **categorized as greedy or lazy** based on how they search and match patterns within a string. **Greedy quantifiers attempt to match as much** of the input **as possible**, whereas **lazy (or non-greedy) quantifiers match as little as possible**.
# 
# The **quantifiers** we **saw earlier, "?", "\*", "+", and "{n,m}"** are **considered greedy**, because they will try to **match as many characters as possible** that satisfy their condition. The **lazy alternative** to them is **achieved by adding "?" after** each. So **"??", "\*?", "+?", and "{n,m}?" are the non-greedy** versions.
# 
# The best way to understand is to see the comparison between them, so we'll **look at a couple examples** for some.

# ### Greedy "\*" vs Lazy "\*?"

# #### Greedy example

# In[ ]:


# Target text
target_text = "Jonathan Livingston Seagull"

# RegEx search pattern
pattern = r"[A-Z]\w*n"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **Notice** in this gready case, how the **"\w\*"** expression **caught as many alphanumeric characters as possible**, before it finds and "n". For both "Jonathan", and "Linvingston", even after it finds an "n", it still tries to match more alphanumerics before a 2nd "n":

# #### Lazy example

# In[ ]:


# Target text
target_text = "Jonathan Livingston Seagull"

# RegEx search pattern
pattern = r"[A-Z]\w*?n"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **Notice** in the non-greedy case, how the **"\w\*?"** expression **caught as little as possible**, before it finds an "n". So the moment it finds the first occurring "n" in that completes the pattern, it stops.

# ### Greedy "{n,m}" vs Lazy "{n,m}?"

# #### Greedy example

# In[ ]:


# Target text
target_text = "2001: A Space Odyssey"

# RegEx search pattern
pattern = r"\d{2,4}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **Notice** in this greedy case, how the **"{2,4}"** expression **tries to match as many digits as possible up to the limit of 4**, so it will match the entire year.

# #### Lazy example

# In[ ]:


# Target text
target_text = "2001: A Space Odyssey"

# RegEx search pattern
pattern = r"\d{2,4}?"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **Notice** in the non-greedy case, how the **"{2,4}"** expression **matches as little as possible that satisfies the minimum of 2**, so it will match two different portions of the year.

# # A Few Practical Examples
# We've already seen some practical examples as we went through the constructs, but let's look at a few others.

# ### Example: basic email
# **I'm not being exaustive in the possible combinations or precise valid email characters** in the following example (didn't have the patience to check all the official rules). The point is to give a general idea.

# ##### Success cases

# In[ ]:


# an email example
target_text = "tucker@cs.finncollege.edu"

# RegEx search pattern
# \w+ matches a word
# @ matches the literal @ symbol
# (?:\w+\.)+ matches one or more word characters followed by a period, at least one time
# (?:com|edu|net|org) matches one of the specified top-level domains
# Note that I used non-capturing groups (?:) because I don't need separate matches for each group
pattern = r"\w+@(?:\w+\.)+(?:com|edu|net|org)"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# In[ ]:


# an email example
target_text = "lexi@lexicorp.org"

# RegEx search pattern
# \w+ matches a word
# @ matches the literal @ symbol
# (?:\w+\.)+ matches one or more word characters followed by a period, at least one time
# (?:com|edu|net|org) matches one of the specified top-level domains
# Note that I used non-capturing groups (?:) because I don't need separate matches for each group
pattern = r"\w+@(?:\w+\.)+(?:com|edu|net|org)"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ##### Fail case

# In[ ]:


# an email example
target_text = "lexilexicorp.org"

# RegEx search pattern
# \w+ matches a word
# @ matches the literal @ symbol
# (?:\w+\.)+ matches one or more word characters followed by a period, at least one time
# (?:com|edu|net|org) matches one of the specified top-level domains
# Note that I used non-capturing groups (?:) because I don't need separate matches for each group
pattern = r"\w+@(?:\w+\.)+(?:com|edu|net|org)"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Example: Telephone numbers
# Again, this is just a general check based on US number formats

# ##### Success cases

# In[ ]:


# a telephone example
target_text = "732-555-1212"

# RegEx search pattern
# (?:1-)? matches 0 or 1 occurances of the "1-" prefix
# \d{3}-\d{3}-\d{4} matches the expected the number of digits separated with dashes
pattern = r"(?:1-)?\d{3}-\d{3}-\d{4}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# In[ ]:


# a telephone example
target_text = "1-732-555-1212"

# RegEx search pattern
# (?:1-)? matches 0 or 1 occurances of the "1-" prefix
# \d{3}-\d{3}-\d{4} matches the expected the number of digits separated with dashes
pattern = r"(?:1-)?\d{3}-\d{3}-\d{4}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ##### Fail case
# This is common cell phone number ib Brazil. They have added an extra digit to support more numbers. But our format only supports US numbers.

# In[ ]:


# a possible brazilian cell phone example
target_text = "021-9992-1212"

# RegEx search pattern
# (?:1-)? matches 0 or 1 occurances of the "1-" prefix
# \d{3}-\d{3}-\d{4} matches the expected the number of digits separated with dashes
pattern = r"(?:1-)?\d{3}-\d{3}-\d{4}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Example: IP addresses

# #### Simple but not accurate IP address check
# This regular expression simply checks for 1 to 3 digit blocks, but does not account for the fact that not every 3 digit number is a vali IP address (max value is 255)

# ##### Success cases

# In[ ]:


# valid IP address
target_text = "192.168.1.21"

# RegEx search pattern
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# In[ ]:


# invalid IP address, but good enough to pass the simple test
target_text = "192.922.1.21"

# RegEx search pattern
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **This was a success**, **but** in the real world it **shouldn't be. "922"** is **not valid in an IP address.**

# ##### Fail case

# In[ ]:


# invalid IP address,missing one component
target_text = "192.1.21"

# RegEx search pattern 
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# #### Accurate but very long IP address check
# This regular expression should validate properly, but it's a lot harder to visualize.

# ##### Success cases

# In[ ]:


# valid IP address
target_text = "192.168.1.21"

# RegEx search pattern
pattern = r"(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ##### Fail case

# In[ ]:


# invalid IP address, which the better RegEx will catch
target_text = "192.922.1.21"

# RegEx search pattern
pattern = r"(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### Example: DS1 Private Line CLCI format
# **Say what?!!!**
# 
# I **don't expect anyone** who did not work in telecommunication many years ago **to know** about the **format of a DS1 Private Line circuit id** (aka, it's CLCI). The **point is**, there are a **lot of specialized notations across industries** that **require very specific formats** that may need to be validated. You can use regular expressions to check them.
# 
# Chances are this is not 100% correct (it's been many many years), but it was something like this ...

# ##### Success case

# In[ ]:


# a DS1 CLSI example
target_text = "DHEC/123/100/ATI/003"

# RegEx search pattern for a CLCI
pattern = r"[A-Z]{2,4}/\d{1,6}/\d{3}/ATI/\d{0,3}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ##### Fail case

# In[ ]:


# a DS1 CLSI example
target_text = "DHEC/1234/10/ATI/003"

# RegEx search pattern for a CLCI
pattern = r"[A-Z]{2,4}/\d{1,6}/\d{3}/ATI/\d{0,3}"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# # Python re Module
# We've **already been using Python's built-in re module** in all the sections above, but we've limitted ourselves to just the findall and search functions, since we wanted to focus on regular expressions themselves. Let's not look a bit moere at the **comprehensive suite of functions** for working with **regular expressions**.

# ## Functions
# We've seen these functions already:
# - **search()** - Returns the **first occurrence of a pattern** anywhere in the target string.
# - **findall()** - Returns a **list containing all matches** in the target string.
# 
# Here are a few other functions available (and there are more):
# - **match()** - **Finds** a **pattern** match at the **beginning of a string**.
# - **fullmatch()** - Checks whether the **entire string matches the pattern**.
# - **compile()** -  **Compiles** a **regular expression pattern into** a **regular expression** object that can be repeatedly used more efficiently.
# - **split()** - **Splits string by** the occurrences of **pattern.**
# - **finditer()** - **Return** an **iterator yielding Match objects** as **string is scanned left-to-right**. This is a way to repeatedly invoke the equivalent of the search() function across an entire string (recall that search only returns the first match).
# - **sub()** - **Return** the **string obtained** by **substituting** the **first match** of a pattern **with** a **provided replacement**.
# 
# For the **official documentation** on **all available functions**, click here: **https://docs.python.org/3/library/re.html#functions**

# ## Flags
# The behavior of some the functions above can be modified by passing various flags. We will look at these using examples:
# - **re.M or re.MULTILINE** - Makes the caret (^) and dollar sign ($) able to match the start and end of each line, not only the start and end of the string
# - **re.I or re.IGNORECASE** - Makes case-insensitive matching possible, so characters can match regardless of case
# - **re.S or re.DOTALL** - Makes the dot (.) match every character, including newline characters, which it does not normally match
# 
# For the **official documentation** on **all available flags**, click here: **https://docs.python.org/3/library/re.html#flags**

# ### re.M or re.MULTILINE
# **Makes** the **caret (^) and dollar sign ($)** able to **match the start and end of each line**, not only the start and end of the string. This is very useful when looking for patterns across a whole document.

# #### Example WITHOUT the flag
# We'll use the **first stanza of a famous William Shakespeare poem**. Why? Because I had to memorize that in 12th grade, and never forgot, so I might as well make some use of it. Let's **look for all the places** where a **sentence starts with "O "**, which is not used anymore.

# In[ ]:


# Target text
target_text = "\
O Mistress mine where are you roaming?\n\
O stay and hear, your true love's coming,\n\
That can sing both high and low.\n\
Trip no further pretty sweeting.\n\
Journeys end in lovers' meeting,\n\
Every wise man's son doth know."

# RegEx search pattern
pattern = "^O[\w\s]*"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **Note** that **only the very first line was found**.

# #### Example WITH the flag

# In[ ]:


# Target text
target_text = "\
O Mistress mine where are you roaming?\n\
O stay and hear, your true love's coming,\n\
That can sing both high and low.\n\
Trip no further pretty sweeting.\n\
Journeys end in lovers' meeting,\n\
Every wise man's son doth know."

# RegEx search pattern
pattern = "^O[\w\s]*"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text, flags=re.MULTILINE)
if (result):
    print(f'Found "{pattern}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **Note** that now **both occurrances were found**.

# ### re.I or re.IGNORECASE
# Makes case-insensitive matching possible, so characters can match regardless of case.

# #### Example WITHOUT the flag

# In[ ]:


# Target text
target_text = "The Caves of Steel"

# RegEx search pattern
pattern = "caves"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# #### Example WITH the flag

# In[ ]:


# Target text
target_text = "The Caves of Steel"

# RegEx search pattern
pattern = "caves"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text, flags=re.I)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### <span style="color:blue"> OPTIONAL: </span>re.S or re.DOTALL
# Makes the **dot (.) match every character, including newline (/n)** characters, Without it, "." would not match a /n.

# #### Example WITHOUT the flag

# In[ ]:


# Target text
target_text = "\
The Hunger Games\n\
Catching Fire"

# RegEx search pattern
pattern = "The Hunger Games....."

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# Notice how we **couldn't match** the **characters in** the **second line**, because the **pattern stopped when** it **reached the \n**.

# #### Example WITH the flag

# In[ ]:


# Target text
target_text = "\
The Hunger Games\n\
Catching Fire"

# RegEx search pattern
pattern = "The Hunger Games....."

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text, flags=re.DOTALL)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# **With the flag**, the **\n between the books was matched by the "."**, so we found a match.

# ## The search, match and fullmatch functions
# As we mentioned earlier:
# - **match()** - **Finds** a **pattern** match at the **beginning of a string**.
# - **fullmatch()** - Checks whether the **entire string matches the pattern**.
# - **search()** - Returns the **first occurrence of a pattern** anywhere in the target string.
# 
# All three of these return a *Match* object. Let's look at a simple example accross all three, to see that it's simply a matter of hoe flexible each is.

# ### The match() function

# In[ ]:


# Target text
target_text = "All the Light We Cannot See"

# RegEx search pattern
pattern = "All"

# Invoke function and check result
result = re.match(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substring: {result.group()}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')

print("\nHowever ... \n")

# RegEx search pattern
pattern = "Light"

# Invoke function and check result
result = re.match(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substring: {result.group()}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### The fullmatch() function

# In[ ]:


# Target text
target_text = "All the Light We Cannot See"

# RegEx search pattern
# (?:\b\w+\b\s*){6} matches exactly 6 words
pattern = r"(?:\b\w+\b\s*){6}"

# Invoke function and check result
result = re.fullmatch(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substring: {result.group()}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')

print("\nHowever ... \n")

# RegEx search pattern
# (?:\b\w+\b\s*){5} matches exactly 5 words
pattern = r"(?:\b\w+\b\s*){5}"

# Invoke function and check result
result = re.fullmatch(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substring: {result.group()}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### The search() function

# In[ ]:


# Target text
target_text = "All the Light We Cannot See"

# RegEx search pattern
# (?:\b\w+\b\s*){5} matches exactly 5 words
pattern = r"(?:\b\w+\b\s*){5}"

# Invoke function and check result
result = re.search(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substring: {result.group()}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')

print("\nand ... \n")

# RegEx search pattern
pattern = "All"

# Invoke function and check result
result = re.search(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substring: {result.group()}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')

print("\nand also ... \n")

# RegEx search pattern
pattern = "Light"

# Invoke function and check result
result = re.search(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substring: {result.group()}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ## <span style="color:blue"> OPTIONAL: </span>The findall and finditer functions
# As we mentioned earlier:
# - **findall()** - Returns a **list containing all matches** in the target string.
# - **finditer()** - **Return** an **iterator yielding Match objects** as **string is scanned left-to-right**. This is a way to repeatedly invoke the equivalent of the search() function across an entire string (recall that search only returns the first match).
# 
# Both of these functions allow you to find multiple matches in the same string. **findall** does it **all in one call, returning a list**. We've already seen countless examples of it. **finditter works with an iterator**, that is essentially repeatedly calling a  search, and returning a *Match* object. Let's look at it now.

# ### The findall function
# We've already seen a number of examples, but we'll just repeate one more for contrast. **With findall**, **note** the **results coming back in a list** which I can print directly.

# In[ ]:


# Target text
target_text = "Journey to the Center of the Earth"

# RegEx search pattern
pattern = r"the\s\w+"

# Find all occurrances of pattern and check result
result = re.findall(pattern, target_text)
if (result):
    print(f'Found "{pattern}" in "{target_text}"')
    print(f'- Matched substrings: {result}')
else:
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ### The finditer function
# We'll do the same search using finditer. **With finditer**, **note** the **use of an iterator** to get the **matches one at a time**. One issue with that, is that you **cannot easily check if no matches were found**. This is not an issue with finditer, but a **general behavior of Python iterators**. There is no simple "is_empty" or "len" type of call for iterators. So we have to change the code to **keep a variable** for **tracking if matches were found**.

# In[ ]:


# Target text
target_text = "Journey to the Center of the Earth"

# RegEx search pattern
pattern = r"the\s\w+"

# get an iterator to search for successive occurances
result_iter = re.finditer(pattern, target_text)

# iterate through match results
match_count = 0
for match in result_iter:
    match_count += 1
    print(f'Match #{match_count}: {match.group()}')

# print message if not matches were found
if (match_count == 0):
    print(f'Did NOT find "{pattern}" in "{target_text}"')


# ## The split() function
# As we mentioned earlier:
# - **split()** - Splits string by the occurrences of pattern.
# 
# This one is simple enough to see in an example.

# ### Example

# In[ ]:


# Target text
target_text = "Whip Hand, Bolt, In the Frame, Field of Thirteen"

# RegEx search pattern
pattern = r"\s*,\s*"

# Invoke function and check result
str_list = re.split(pattern, target_text)
print(f"String list: {str_list}")


# ## The sub() function
# As we mentioned earlier:
# - **sub()** - **Return** the **string obtained** by **replacing the first match of a pattern by a provided in replacement.
# 
# To me, **sub()** is one of the more interestaing functions, because it's the only one that does **more than simply find a pattern**. It gives us the **opportunity to change it**.

# ### Simple replacement example

# In[ ]:


# Target text
target_text = "Foundation"

# RegEx search pattern
pattern = r"Foundation"

# Replacement text
replacement = "Foundation and Empire"

# Invoke function and check result
new_text = re.sub(pattern, replacement, target_text) 
print(f"Original text: {target_text}")
print(f"New text: {new_text}")
print()

# Replacement text
replacement = "Second Foundation"

# Invoke function and check result
new_text = re.sub(pattern, replacement, target_text) 
print(f"Original text: {target_text}")
print(f"New text: {new_text}")
print()

# Replacement text
replacement = "Foundation's Edge"

# Invoke function and check result
new_text = re.sub(pattern, replacement, target_text) 
print(f"Original text: {target_text}")
print(f"New text: {new_text}")
print()


# ### Replacement using back references
# In this example, let's update the data format used in most of the world, to conform with the one used in the United States. **Most of of the world represents dates as Day/Month/Year**. So "10/09/2024" would be September 10th, 2024. The **United States** "dares to be different", and **uses** the well known **Month/Day/Year** format. If you have relatives in other parts of the world, that can lead to some confusion. So let's solve that with an automatic translator :-)
# 
# We will need to **use not just substitution**, but **also groups and backreferences**.

# In[ ]:


# This is a date invitation for September 10th, 2024, using the United States format
target_text = "Hi Marcia. I'm looking forward to our date on 09/10/2024, at the top of the Sugarloaf mountain"

# Pattern search for a US based date
pattern = r"(\d{1,2})/(\d{1,2})/(\d{4})"

# Replacement text swapping the day and the month
replacement = r"\2/\1/\3"

# Invoke function and check result
new_text = re.sub(pattern, replacement, target_text) 
print(f"Original text: {target_text}")
print(f"New text: {new_text}")


# Did you **notice how the month and day were swapped in the replacement**? Thanks to the sub function, nobody was left standing and dejected at the top of the mountain.

# # <span style="color:blue"> OPTIONAL</span>

# ## Find words that have "a" in them
# This was a question I got from a learner during the session, and I didn't have time to answer in real time. But since I love questions, I added as a bonus example here.

# ### Pattern used
# The pattern that did the trick was "\b\w*[Aa]\w*\b"
# - The "\b" in the beginning and end mark the word boundaries
# - In the middle, "\w*[Aa]\w*" will give me any combination of alphanumerics on each side, with an "a" or "A" in the middle.

# #### A bunch of successfull cases
# I'm using a list here to save time a test a bunch of success cases in one block

# In[ ]:


# Target text
target_texts = ["The A.B.C. Murders", "Pillars of the Earth", "Tigana", "Planet of the Apes", "Steelheart", "Belgarath the Sorcerer"]

# RegEx search pattern
pattern = r"\b\w*[Aa]\w*\b"

# Find all occurrances of pattern and check result
for target_text in target_texts:
    result = re.findall(pattern, target_text)
    if (result):
        print(f'Found "{pattern}" in "{target_text}"')
        print(f'- Matched substrings: {result}')
    else:
        print(f'Did NOT find "{pattern}" in "{target_text}"')
    print()


# #### A bunch of fail cases

# In[ ]:


# Target text
target_texts = ["Presumed Innocent", "Time to Kill", "Fever"]

# RegEx search pattern
pattern = r"\b\w*[Aa]\w*\b"

# Find all occurrances of pattern and check result
for target_text in target_texts:
    result = re.findall(pattern, target_text)
    if (result):
        print(f'Found "{pattern}" in "{target_text}"')
        print(f'- Matched substrings: {result}')
    else:
        print(f'Did NOT find "{pattern}" in "{target_text}"')
    print()


# In[ ]:




