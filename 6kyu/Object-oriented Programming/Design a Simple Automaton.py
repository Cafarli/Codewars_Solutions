"""
Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states: q1, q2, and q3. Here is the description of the states:

q1 is our start state, we begin reading commands from here
q2 is our accept state, we return true if this is our last state
And the transitions:

q1 moves to q2 when given a 1, and stays at q1 when given a 0
q2 moves to q3 when given a 0, and stays at q2 when given a 1
q3 moves to q2 when given a 0 or 1
The automaton should return whether we end in our accepted state (q2), or not (true/false).

Your task
You will have to design your state objects, and how your Automaton handles transitions. Also make sure you set up the three states, q1, q2,
and q3 for the myAutomaton instance. The test fixtures will be calling against myAutomaton.

As an aside, the automaton accepts an array of strings, rather than just numbers, or a number represented as a string, 
because the language an automaton can accept isn't confined to just numbers. An automaton should be able to accept any 'symbol.'
"""

class Automaton:
    def __init__(self):
        self.states = {'q1', 'q2', 'q3'}
        self.current_state = 'q1'

    def read_commands(self, commands):
        for command in commands:
            if self.current_state == 'q1':
                if command == '1':
                    self.current_state = 'q2'
                elif command == '0':
                    self.current_state = 'q1'
            elif self.current_state == 'q2':
                if command == '0':
                    self.current_state = 'q3'
                elif command == '1':
                    self.current_state = 'q2'
            elif self.current_state == 'q3':
                if command == '0' or command == '1':
                    self.current_state = 'q2'
        return self.current_state == 'q2'


my_automaton = Automaton()
