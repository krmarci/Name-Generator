# Name-Generator

This code can be used to generate new names from a list of existing names.

**Make sure to name your input file as input.txt and put it in the folder next to the code. This repository also includes an example input with 219 Hungarian male names.**

The software does not use neural networks, instead it relies on a probabilistic approach. First, the software calculates probabilities for all substrings that can be found in the dataset. After that, when generating a word, it looks up all substrings which include an ending substring of the already generated word and end with an additional character after that. Using this, we can generate a probability table for the next character, and generate the next character randomly. This process is repeated until the word ending character is generated.

As an example, let's look at a list of five names: ["James", "Robert", "John", "Michael", "William"]. To make word processing easier, the program converts all names to lower-case, and adds a semicolon at the beginning and end to be able to generate the first character and the word ending character: [";james;", ";robert;", ";john;", ";michael;", ";william;"]. We initialise our generated name as ";". TBC
