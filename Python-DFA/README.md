# Python-DFA
When supplied with a text document of the correct format, this python tool constructs a DFA. After constructing the DFA, user input is read in and tested against the DFA's logic.
The machine description file will consist of the following parts (separated by newlines):

1. The input alphabet: single characters separated by spaces.
2. The number of states in the machine. States shall be labeled Q0 ... Qn where n is one less than this value.
3. A list of accept states, separated by spaces. If no accept states are present in the machine, this line shall contain two hyphens.
4. Three hyphens (just as a separator).
5. A list of rules, each on its own line. Each rule consists of the starting state, what character from the input alphabet to transition on, and the state to transition to — separated by spaces.
6. Any blank lines shall be ignored.

Correct usage:
python DFA.py [testfile.txt]

Press Ctrl+C to exit the input loop.