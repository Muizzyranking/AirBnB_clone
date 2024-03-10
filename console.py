#!/usr/bin/env python3
import cmd

"""Module for HBNBCommand class"""


class HBNBCommand(cmd.Cmd):
    """
    Defines the HBNBCommand class
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
