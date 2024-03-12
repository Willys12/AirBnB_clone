#!/usr/bin/python3
# My command line interpreter
"""
Entry point for the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB.
    """

    prompt = '(hbnb) '

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
        """
        Overrides the default behavior for unrecognized commands.
        """
        print(f"Unknown command: {line}")

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
