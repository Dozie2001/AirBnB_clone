#!/usr/bin/python3
"""Console"""

import cmd



class HBNBCommand(cmd.Cmd):
    """functionality for HBNB console"""

    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        return True

    
    def do_quit(self, arg):
        """Quits commant to exit the Program"""
        exit()
    
    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()