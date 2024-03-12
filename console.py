#!/usr/bin/python3
# My command line interpreter
"""
Entry point for the command interpreter.
"""

import cmd
import re


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB.
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quits the command interpreter.
        """
        print("Quitting the HBNB command interpreter.")
        return True

    def do_EOF(self, line):
        """
        Handles EOF (Ctrl-D) to exit the program.
        """
        print("Exiting the HBNB command interpreter.")
        return True

    def emptyline(self):
        """
        Overrides the default behavior for an empty line.
        """
        pass

    def default(self, line):
        """Default behavior for cmd module when input is invalid"""
        # Regex pattern to match commands and their arguments
        pattern = r"(\w+)\s*(?:\((.*?)\))?"
        match = re.match(pattern, line)
        if match:
            command = match.group(1)
            args = match.group(2)
            if command in ['all', 'show', 'destroy', 'count', 'update']:
                # Call the appropriate method based on the command
                getattr(self, 'do_' + command)(args)
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))

    def help_help(self):
        """
        Overrides the default help command to provide custom help text.
        """
        print("""
        HBNB Command Interpreter
        ------------------------
        Available commands:
        quit - Quits the command interpreter.
        help - Displays this help message.
        """)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
