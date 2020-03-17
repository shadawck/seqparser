# Article from : [towardsdatascience.com](https://towardsdatascience.com/regex-performance-in-python-873bd948a0ea)

# Sequence parser with Regex expression for big set of data

## Recursive backtracking
In most programming languages, the regular expression engine is implemented using the recursive backtracking algorithm. This algorithm specializes in building a solution one piece at a time incrementally while removing solutions that fail to satisfy the constraints. It searches every possible combination to solve a computational problem. 

For instance, you can think of the process of backtracking as a tree. Depending on how close what you search identifies with what’s in your text, then the tree can be big or small.

Here’s an example, you are searching for the word “I” in a personal essay written in the first person. At each point when the backtracking algorithm finds an “I”, the algorithm can proceed forward. When the backtracking algorithm does not find an “I”, it will backtrack. Due to the frequency of the “I” in the text, your algorithm will likely move forward a lot. If you imagine all the steps the algorithm took as a tree, then this tree is probably pretty small.

What if you are searching for the word “I” in a scholarly article that is written in a third-person voice. The likelihood of finding the word “I” is almost 0. At each step, with each word, the algorithm will backtrack a lot. If you imagine all the steps the algorithm took as a tree, then this tree will grow to be pretty large.

When texts are large and your match is less than 1% of the text, then your recursive backtracking algorithm will end up backtracking for every word. This will slow the performance exponentially.

## NFA or Non-deterministic Finite Automata algorithm

A Finite Automaton is the simplest model of computation. It uses a very limited memory. It is an idealized machine to recognize and match strings to a character set. The machine either accepts or rejects the strings. This results in the state transitions of 1 or 0.

For instance, in the below example, going from state A to state B results in state transition 1. Going from state B to state A, the state transition is 1 as well. However, going from state A to state C, the state transition is 0.

In Deterministic Finite Automata, there is only one next state.

In Non-deterministic Finite Automata, there can be multiple next states. The states can also be chosen at random, and in parallel.

In a 1968 CACM paper, Thompson proposed the NFA algorithm to use NFA for regular expressions. The NFA of each regular expression is built up from subexpressions. This will create exactly one state per character or metacharacter in the regular expression. To transition from one state to the next, rather than trying each state individually and backtracking when it fails, the NFA contains all the states and tries them simultaneously.

For instance, if you have an example such as the one [provided by this blog post when the expression is (abab|abbb)](https://swtch.com/~rsc/regexp/regexp1.html), then at each step, there are two states: abab and abbb. The machine will try both paths simultaneously at each step reading the input string only once.

Using NFA, you don’t have the tree structure of paths taken that grows exponentially like in recursive backtracking. Instead, you have two states (in this case) or n-states which is evaluated simultaneously. The size of the data will allow processing time to grow linearly.
Below is the performance from the recursive backtracking algorithm compared to the performance of the NFA algorithm. You notice the exponential growth of matching time when data grows using the recursive backtracking algorithm. With NFA, the growth is more linear.

# Python Regular Expression

In the real world, because there’s a learning curve to use regular expressions properly, many programmers will shy away from using regular expressions. Programmers often make excuses such as, “Complex regular expressions seem like atomic statements.” to avoid using regular expression. Using regular expressions can mean that the code can be hard-to-debug, hard-to-read, and hard-to-maintain.
However, if you use Python regular expressions with thought about the performance and usage, it can create programs that have fewer lines of code and cleaner to read.

**The point is to use it as it was intended: to write simpler and cleaner code.**

To do that, by understanding both how recursive backtracking and NFA works, you can use regular expressions where it’s most effective.

**One rule to go by: be explicit. Guide the regex engine to where you want it to go. Spell it all out even if it’s a longer regular expression. It helps to break up the statements into simpler statements.**

A good practice is to test small chunks of regular expressions on small amounts of data. Benchmark the performance as you enlarge the dataset. Then, work your way up to a larger expression from there. (You can use a regex debugger for this. A list can be found below)

Another good practice is to draw out what is exactly happening with one piece of data that you are searching for. Think like the regex engine and see what steps it will take.

# Know when to use the quantifiers

There are several quantifiers in regular expressions. It’s critical to learn what they do. Then, when you write the statements, try to imagine how the Regex engine will go through the data. This way you can see if there’s a better solution by sidestepping “backtracking”.

Greedy quantifiers are the quantifiers that match as much as possible.
By default the Regex engine is greedy. This means that if you are not specific, then the engine will match as much as possible. This will lead to possibly a lot of “backtracking”.

Lazy quantifiers are the quantifiers that match as few as possible.
Lazy quantifiers can be expensive. They work on expanding their match one step at a time as much as needed. This may cause the engine to backtrack at each step.

Possessive quantifiers are the quantifiers that give up characters if needed to allow the rest of the pattern to match.
Possessive quantifiers can come in handy when you know that a match may fail when there’s no match. It can help it fail faster by not backtrack.

[Here’s a great blogpost](https://www.rexegg.com/regex-quantifiers.html) detailing examples of quantifiers and much more.

# Use Atomic Grouping

Atomic Grouping is a group that when the regex engine exits from it, throws away all the backtracking positions. Even though Python does not have this feature, you can emulate atomic grouping by using zero-width lookahead assert: ((?=regex)) where regex=(?P=name).

# Avoid Catastrophic Backtracking by Using Possessive Quantifiers

Catastrophic backtracking happens when a regular expression backtracks when a greedy quantifier fails repeatedly. This is especially true on nested greedy quantifiers. When one of quantifier fails, the backtracking grows exponentially because it’s nested. It doesn’t give up and ends up getting stuck in a loop.

To alleviate backtracking, you can use either possessive quantifiers or atomic groups. With possessive quantifiers, it will fail when a quantifier in a nested quantifier fails to match. The backtracking will be linear.

In cases where a good possessive quantifier can not be found, it’s good to use atomic groups to alleviate these catastrophic backtracking situations.

[Read more about this here.](https://www.regular-expressions.info/catastrophic.html)

# Debug Regular Expressions

[Regex Buddy](https://www.regexbuddy.com/debug.html) has a helpful tool to debug regular expressions by showing you what’s happening in the engine.
[Pythex](https://pythex.org/) is also another regex debugging tool that’s helpful for beginners.

# Alternatives to using the prepackaged Regex Engine for Text Processing

[RE2](https://github.com/google/re2) — It is a library that uses the Finite automata approach to speed up performance in your regular expression processing. It is designed to be run on the Linux Operating system.

[FlashText](https://github.com/vi3k6i5/flashtext) — It is a library that is used to replace words in a large text. It uses a Tri Data Structure to store data for fast retrieval. It will “search” and “replace” in a single pass. The key in FlashText’s speed comes from the fact that it checks to see if words exist in keys in a dictionary. This is much faster than checking for words in a list of words.

Learn More About Python Regular Expressions : 

[Tutorial: Python Regex (Regular Expressions) for Data Scientists](https://www.dataquest.io/blog/regular-expressions-data-scientists/)
[Python Regex Cheat Sheet](http://web.mit.edu/hackl/www/lab/turkshop/slides/regex-cheatsheet.pdf)
[Mastering Python Regular Expressions](https://www.oreilly.com/library/view/mastering-python-regular/9781783283156/)
[Regex tutorial — A quick cheatsheet by examples](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)

[int,int,int,int] [int,int,int,int] [int,int,int,int] [int,int,int,int] -> Credit Card Sequence
