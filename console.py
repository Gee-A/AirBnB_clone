#!/usr/bin/python3
"""Module console
Serves as the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Handles End of File character\n"""
        print()
        return True

    def emptyline(self):
        """Ensures the last nonempty command is not repeated\n"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()