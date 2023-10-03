# 0x09. Python - Everything is object

In this project, I learned how Python works with different types of object
- the difference between immutable object and mutable object
- What reference, assignment and alias mean
- How to display the variable identifier using `id()` (which is the memory address in the CPython implementation)


## Table of contents :book:
Files | Description
----- | -----------
[0-answer.txt](./0-answer.txt) | contains answer to -> What function would you use to get the type of an object?
[1-answer.txt](./1-answer.txt) | contains answer to -> How do you get the variable identifier (which is the memory address in the CPython implementation)?
[2-answer.txt](./2-answer.txt) | contains answer to -> In the following code, do `a` and `b` point to the same object?<br>`>>> a = 89` <br> `>>> b = 100`
[3-answer.txt](./3-answer.txt) | contains answer to -> In the following code, do `a` and `b` point to the same object?<br>`>>> a = 89` <br> `>>> b = 89`
[4-answer.txt](./4-answer.txt) | contains answer to -> In the following code, do `a` and `b` point to the same object?<br>`>>> a = 89` <br> `>>> b = a`
[5-answer.txt](./5-answer.txt) | contains answer to -> In the following code, do `a` and `b` point to the same object?<br>`>>> a = 89` <br> `>>> b = a + 1`
[6-answer.txt](./6-answer.txt) | contains answer to -> What do these 3 lines print?<br> `>>> s1 = "Best School"` <br> `>>> s2 = s1` <br> `>>> print(s1 == s2)`
[7-answer.txt](./7-answer.txt) | contains answer to -> What do these 3 lines print?<br> `>>> s1 = "Best"` <br> `>>> s2 = s1` <br> `>>> print(s1 is s2)`
[8-answer.txt](./8-answer.txt) | contains answer to -> What do these 3 lines print?<br> `>>> s1 = "Best School"` <br> `>>> s2 = "Best School"` <br> `>>> print(s1 == s2)`
[9-answer.txt](./9-answer.txt) | contains answer to -> What do these 3 lines print?<br> `>>> s1 = "Best School"` <br> `>>> s2 = "Best School"` <br> `>>> print(s1 is s2)`
[10-answer.txt](./10-answer.txt) | contains answer to -> What do these 3 lines print?<br> `>>> l1 = [1, 2, 3]` <br> `>>> l2 = [1, 2, 3]` <br> `>>> print(l1 == l2)`
[11-answer.txt](./11-answer.txt) | contains answer to -> What do these 3 lines print?<br> `>>> l1 = [1, 2, 3]` <br> `>>> l2 = [1, 2, 3]` <br> `>>> print(l1 is l2)`
[12-answer.txt](./12-answer.txt) | contains answer to -> What do these 3 lines print?<br> `>>> l1 = [1, 2, 3]` <br> `>>> l2 = l1` <br> `>>> print(l1 == l2)`
[13-answer.txt](./13-answer.txt) | contains answer to -> What do these 3 lines print?<br> `>>> l1 = [1, 2, 3]` <br> `>>> l2 = l1` <br> `>>> print(l1 is l2)`
[14-answer.txt](./14-answer.txt) | contains answer to -> What does this script print?<br> `l1 = [1, 2, 3]` <br> `l2 = l1`  <br> `l1.append(4)` <br> `print(l2)`
[15-answer.txt](./15-answer.txt) | contains answer to -> What does this script print?<br> `l1 = [1, 2, 3]` <br> `l2 = l1`  <br> `l1 = l1 + [4]` <br> `print(l2)`
[17-answer.txt](./17-answer.txt) | contains answer to -> What does this script print?<br> `def increment(n):` <br> `    n.append(4)` <br><br> `l = [1, 2, 3]` <br> `increment(l)` <br> `print(l)`
[18-answer.txt](./18-answer.txt) | contains answer to -> What does this script print?<br> `def assign_value(n, v):` <br> `    n = v`  <br><br> `l1 = [1, 2, 3]` <br> `l2 = [4, 5, 6]` <br>`assign_value(l1, l2)` <br> `print(l1)`
[19-answer.txt](./19-answer.txt) | function `def copy_list(l):` that returns a copy of a list
[20-answer.txt](./20-answer.txt) | contains answer to -> `a = ()` Is `a` a tuple?
[21-answer.txt](./21-answer.txt) | contains answer to -> `a = (1, 2)` Is `a` a tuple?
[22-answer.txt](./22-answer.txt) | contains answer to -> `a = (1)` Is `a` a tuple?
[23-answer.txt](./23-answer.txt) | contains answer to -> `a = (1, )` Is `a` a tuple?
