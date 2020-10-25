Parser
======

The parse function, from the parser submodule, is the main functionality of the
chris-parser package. It is a simple function, which parses a .chris file.

parse
^^^^^

The parse function takes a single argument, which is either the relative or
absolute path of the .chris file to be parsed. It then returns a Chris object
containing all of the data from within the file. An InvalidFile exception will
be raised if the parser fails to recognize the contents of the given files as a
valid .chris file.
