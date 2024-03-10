#!/usr/bin/python3
# My command interpreter.
import cmd


class HBNBCommand(cmd.Cmd):
    """Interactive command interpreter for HBNB project"""
    prompt = "(hbnb) "

    # Defining basic commands
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    # Aliasing
    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
