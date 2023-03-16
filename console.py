#!/usr/bin/python3
"""Console"""

import cmd
import re
import sys
import shlex
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



def parse_cmd(argv: str) -> list:
    """
    Parse or split a string (argv) based on some pattern
    example, spaces, brackects
    :param argv: string
    :return:  a list of words representing the parsed string
    """
    braces = re.search(r"\{(.*?)}", argv)
    brackets = re.search(r"\[(.*?)]", argv)
    if not braces:
        if not brackets:
            return [i.strip(",") for i in shlex.split(argv)]
        else:
            var = shlex.split(argv[:brackets.span()[0]])
            retval = [i.strip(",") for i in var]
            retval.append(brackets.group())
            return retval
    else:
        var = shlex.split(argv[:braces.span()[0]])
        retval = [i.strip(",") for i in var]
        retval.append(braces.group())
        return retval


def check_args(args):
    """
    checks if args is valid
    Args:
        args (str): the string containing the arguments passed to a command
    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = parse_cmd(args)
    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in HBNBCommand.classes:
        print("** class doesn't exist **")
    else:
        return arg_list


class HBNBCommand(cmd.Cmd):
    """functionality for HBNB console"""

    classes = {'BaseModel': BaseModel}
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

    def do_create(self, arg):
        """
        Create an Instance of a class
        [USAGE]: create <classname>
        [Return]: id of the created class
        """
        args = check_args(arg)
        if args:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        args = check_args(arg)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        arg_list = check_arg(arg)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
        else:
            key = "{}.{}".format(*arg_list)
            if key not in storage.all():
                print("**no instance found**")
            else:
                del sstorage.all()[key]
                storage.save()

    def do_all(self, argv):
        """
        Prints all string representation of all instances
        [USAGE]: all <classname>
        """
        arg_list = shlex.split(argv)
        objects = storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects if arg_list[0] in str(obj)])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
