def math_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()

max_round = 5
start = 1

for item in range(0, max_round):
  rounds = math_statement("* Round {} of {} *".format(start, max_round), "*")
  start += 1
