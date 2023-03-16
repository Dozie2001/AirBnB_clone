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
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ""


    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')
    
    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        print()
        exit()
    
    def default(self, arg):
        """Default behaviour for cmd module when input is invalid"""
        action_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
            }

        match = re.search(r"\.", arg)
        if match:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in action_map:
                    call = "{} {}".format(arg1[0], command[1])
                    return action_map[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

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
        arg_list = check_args(arg)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
        else:
            key = "{}.{}".format(**arg_list)
            if key not in storage.all():
                print("**no instance found**")
            else:
                del storage.all()[key]
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
    
    def do_update(self, argv):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        [USAGE]: update <classname> <id> <attribute name> "<attribute value>"
        """
        arg_list = check_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
