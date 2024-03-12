#!/usr/bin/python3
"""
Entry point for the command interpreter.
"""

import cmd
import json
import os


class BaseModel:
    def __init__(self):
        self.id = "1234-1234-1234"

    def save(self):
        """Save the instance to a JSON file."""
        data = {"id": self.id}
        with open("instances.json", "a") as file:
            file.write(json.dumps(data) + "\n")


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

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
        print("*** Unknown syntax: {}".format(line))

    def do_create(self, line):
        """Usage: create <class>
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        args = self.parse_args(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            instance = BaseModel() # Simplified for demonstration
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Usage: show <class> <id>
        Prints the string representation of an instance based on the class name and id."""
        args = self.parse_args(line)
        if len(args) < 2:
            print("** class name or instance id missing **")
        else:
            instance = self.load_instance(args[0], args[1])
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, line):
        """Usage: destroy <class> <id>
        Deletes an instance based on the class name and id."""
        args = self.parse_args(line)
        if len(args) < 2:
            print("** class name or instance id missing **")
        else:
            if self.delete_instance(args[0], args[1]):
                print("Instance deleted successfully.")
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Usage: all or all <class>
        Prints all string representation of all instances based or not on the class name."""
        args = self.parse_args(line)
        if len(args) > 1 and args[1] not in self.__classes:
            print("** class doesn't exist **")
        else:
            instances = self.load_all_instances(args[0] if len(args) > 0 else None)
            print(instances)

    def do_update(self, line):
        """Usage: update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name and id by adding or updating attribute."""
        args = self.parse_args(line)
        if len(args) < 4:
            print("** missing arguments **")
        else:
            if self.update_instance(args[0], args[1], args[2], args[3]):
                print("Instance updated successfully.")
            else:
                print("** no instance found **")

    def parse_args(self, line):
        """
        Parses arguments from the input line, handling quoted strings.
        """
        args = []
        current_arg = ""
        in_quotes = False
        for char in line:
            if char == '"':
                in_quotes = not in_quotes
                if not in_quotes:
                    args.append(current_arg)
                    current_arg = ""
                continue
            if char == " " and not in_quotes:
                if current_arg:
                    args.append(current_arg)
                    current_arg = ""
                continue
            current_arg += char
        if current_arg:
            args.append(current_arg)
        return args

    def load_instance(self, class_name, instance_id):
        # Placeholder for loading an instance from the JSON file
        pass

    def delete_instance(self, class_name, instance_id):
        # Placeholder for deleting an instance from the JSON file
        pass

    def load_all_instances(self, class_name=None):
        # Placeholder for loading all instances of a class from the JSON file
        pass

    def update_instance(self, class_name, instance_id, attribute_name, attribute_value):
        # Placeholder for updating an instance's attribute in the JSON file
        pass

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
        create - Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        show - Prints the string representation of an instance based on the class name and id.
        destroy - Deletes an instance based on the class name and id.
        all - Prints all string representation of all instances based or not on the class name.
        update - Updates an instance based on the class name and id by adding or updating attribute.
        """)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
