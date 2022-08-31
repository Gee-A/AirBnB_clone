#!/usr/bin/python3
"""Module console
Serves as the entry point of the command interpreter"""

from models.base_model import BaseModel
from models import storage
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

    def do_create(self, line):
        """Creates a new instance and saves it to JSON file
        on success: returns id
        else: returns an error msg\n"""

        if line is None or line == "":
            print("** class name missing **")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        else:
            o = BaseModel()
            o.save()
            print(o.id)

    def do_show(self, line):
        """Prints the string representation of an instance based\
 on class name and id\n"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id\n"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del(storage.all()[key])
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances\
 given a class name or not\n"""
        if line != "":
            words = line.split(' ')
            if words[0] != 'BaseModel':
                print("** class doesn't exist **")
            else:
                o_list = [str(obj) for key, obj in storage.all().items()
                          if type(obj).__name__ == words[0]]
                print(o_list)
        else:
            o_list = [str(obj) for key, obj in storage.all().items()]
            print(o_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id\n"""
        if line == "":
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] != 'BaseModel':
                print("** class doesn't exit **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    if len(words) < 3:
                        print("** attribute name missing **")
                    elif len(words) < 4:
                        print("** value missing **")
                    else:
                        setattr(storage.all()[key], words[2], words[3])
                        storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
