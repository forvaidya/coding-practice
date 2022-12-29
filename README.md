- [coding-practice](#coding-practice)
  - [General Rules](#general-rules)
  - [Yaml Rules](#yaml-rules)
  - [Python Rules](#python-rules)
    - [Idiomatic Python.](#idiomatic-python)
      - [Use list comprehension instead of for loops.](#use-list-comprehension-instead-of-for-loops)
      - [Use slices for array operation.](#use-slices-for-array-operation)
      - [Use dictionaries and sets instead of rewriting this type of code again.](#use-dictionaries-and-sets-instead-of-rewriting-this-type-of-code-again)
  - [Bash Rules](#bash-rules)
  - [Git Rules](#git-rules)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# coding-practice

## General Rules

Code must have character limit of *80 +/- 5* columns.

By adhearing to this it is very easy to review the code and understand git diffs.

There should be a trailing newline at the end of file.

If a code block is to be removed, delete that block rather than commenting it, it is git review friendly practice

There should be sufficient blank lines as a logical delimiter.



## Yaml Rules
Yaml should start with a line ```---``` to indicate that this yaml for editors.

Long strings must split to adheare to 80 columns rule.
example
```
filepath: >-
    a-long-string-
    lorem-ipsum-foo
    -bar-car
```
This results in a string

```
a-long-string- lorem-ipsum-foo -bar-car
```
This adds a white space in between the tokens. If you dont want the space you should handel in the program.


Line breaks can be preserved by using "|" 

example
```
filepath: |-
    a-long-string-
    lorem-ipsum-foo
    -bar-car
```
This results in a string

```
a-long-string-
lorem-ipsum-foo
-bar-car
```
A *hyphen* after ```|``` or ```>``` removes leadings tabs.
 
There should be sufficient blank lines as a logical delimiter



## Python Rules

### Idiomatic Python.

#### Use list comprehension instead of for loops.

Example - this list returns squares of a list in one line.

```
In [1]: input =  list(range(1,8))

In [2]: input
Out[2]: [1, 2, 3, 4, 5, 6, 7]

In [3]: output_sq = [ item * item for item in input ]

In [4]: output_sq
Out[4]: [1, 4, 9, 16, 25, 36, 49]

In [5]:

```
#### Use slices for array operation.
Use slices to traverse, split and manipulate an array.

Example - to detect palindrome in pythonic way.
```
In [4]: input = "atita"

In [5]: input == input[::-1]
Out[5]: True

In [6]: input = "NewYork"

In [7]: input == input[::-1]
Out[7]: False

```
#### Use dictionaries and sets instead of rewriting this type of code again.
Dictionaries are versatile and generally fast.

## Bash Rules

+ Adheare to 80 columns rule.

+ NO trailing space at the end of line.

+ NO blank line above ```do```

+ Use HEREDOC to represent multiline strings, long commands to SSH

+ Use ```exec >``` instead of traditional redirection.

+ Use ``` -e ``` flag to exit on error, Fail Fast !!

+ Use ``` : ``` to bail out of error condition.


Example
```
#!/bin/bash -e
exec 1>${$}-run.log
cat<<HEREDOC
Hello: UTC Date is $(date -u)
This is a long message.
HEREDOC
```

## Git Rules

+ While merging a PR always do a "Squash Merge"
+ Never do a merge commit unless merge of a final branch to another final branch
+ Use ```git rebase -i``` to squash multiple commits in a single commit.
+ Never commit a binary file (jar/tar/zip) in git.
+ Always leave a trailing blank line in all type of code.
+ Always write a README.md
+ 

