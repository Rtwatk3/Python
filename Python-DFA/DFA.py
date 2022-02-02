import sys #To get command line file
alphabet = []
states = 0
thisDFA = dict()
acceptState = []

def main():
	#recieve the file through the command line file filename
  	#send file to parse fxn, recieve data structure
	if(len(sys.argv)!=2):
		print("Please Add text file to command line prompt.")
		return 0
	if(parse(sys.argv[1])):
		print("file loaded successfully")
	else:
		print("Input file not supported. Please Submit a new file.")
		return 0
	#recieve string to evaluate from user, infinte loop only stopped by ctrl+c
	while(1):
		input_string = str(input("Please enter an input string:"))
		#evaluate list of rules in order to determine if acceptable DFA, send data structure & input to eval fxn, recieve path
		if input_string.count('1') + input_string.count('0') == len(input_string):
			accepted = eval(input_string)
			print(accepted)
		else:
			print("Please only enter 1s and 0s")
	return 0

#parsing function: file filename
def parse(filename):
	flag=True
	f = open(filename, "r")
	alphabet=f.readline().rstrip("\n")
	alphabet=alphabet.split()
	states=int(f.readline().rstrip("\n"))
	acceptState.append(str(f.readline().rstrip("\n")))
	separator = f.readline().rstrip("\n")
	#error checking
	if(separator!="---"):
		print("Input File does not contain ---")
		return False
	if(acceptState=="--"):
		print("No accept states")
		return False
	allRules=[]
	#Read all lines break them into rule sets
	#Format is State, input, State
	for lines in f:
		lines=lines.rstrip("\n")
		currRule=lines.split(" ")
		allRules.append(currRule)
	f.close()
	for rules in allRules:
		if(rules[0] not in thisDFA.keys()):
			thisDFA[rules[0]]={rules[1]:rules[2]}
		else:
			if(rules[1] not in thisDFA[rules[0]].keys()):
				thisDFA[rules[0]].update({rules[1]:rules[2]})
			else:
				print("Not a DFA, state",rules[0],"splits into two seperate paths with the same input",rules[1])
				return False
	#Error checks
	if(len(thisDFA.keys())!=states):
		return False
	#Test that the accept state is in the DFA
	for testStates in acceptState[0].split():
		if testStates not in thisDFA.keys():
			print(testStates,"not in DFA")
			return False
	return True
  
  #input-> file
  #output-> print: parsed correctly/incorrectly, return: data structure of DFA
  #read the file in & store parts of the file in appropriate data structure
  #first line: language of DFA
  #second line: number of states in DFA
  #third line: list of accept states in DFA
  #fourth line: dashes
  #rest: list of rules, each on its own line. start state->input character->state to transition to. seperated by spaces

def eval(input_string):

	#input-> data structure of DFA, input string
	#output-> print: T/F (string is/is not in the DFA) return: path 
	#note: can only be a dfa if there is a unique path in the graph to obtain a given string
	state = 'Q0'
	path = []
	path.append(state)
	acceptStates=acceptState[0].split()
	for x in input_string:
		state = thisDFA[state].get(x)
		path.append(state)
	if state in acceptStates:
		print("Input is Accepted. Path:")
	else:
		print("Input is Rejected. Path:")
	return path

main()