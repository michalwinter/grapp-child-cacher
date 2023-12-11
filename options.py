import getopt

def get_options(arguments):
  arguments_tuples = getopt.getopt(arguments, "h:p:", ["rw="])[0]
  arguments = {}
  for argument in arguments_tuples:
    arguments[argument[0].removeprefix("-")] = argument[1]
  
  return arguments