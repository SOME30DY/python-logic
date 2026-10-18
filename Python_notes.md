if / elif / else

if checks a condition. If it’s True, that block runs.
elif means “else if.” It’s only checked when everything above it was False.
else is the fallback that runs when nothing above it was True.
Every if, elif and else line ends with a colon :.
The code under each one has to be indented 4 spaces.

Relational operators (each one gives True or False)

Operator	Meaning
==	equal to
!=	not equal to
< / >	less than / greater than
<= / >=	less than or equal / greater than or equal

Remember: = stores a value (car = 5), and == compares two values (car == 5).

Logical operators

and: both sides have to be True. For example, the PC is in use AND it’s been offline more than 30 days.
or: only one side has to be True. For example, high priority OR 10+ users affected.
not: flips True to False and False to True.

Precedence

Python runs not first, then and, then or.
Use parentheses to control the order, just like in math: gpa >= 3.5 and (hours >= 50 or leader == "yes").

Data types

input() always gives back text (a string), even if the user types a number.
Wrap it in int() for whole numbers or float() for decimals before you compare it to a number.
.lower() turns “YES” into “yes” so your comparisons still match.

Common mistakes

Forgetting the colon at the end of an if line.
Writing print: instead of print(. You get no error and nothing prints.
Using = when you meant ==.
Indentation that doesn’t line up.
