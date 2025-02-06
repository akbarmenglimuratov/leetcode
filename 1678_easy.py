# SOLVED
def interpret(command):
	return command.replace('()', 'o').replace('(al)','al')

command = "(al)G(al)()()G"
print(interpret(command))
