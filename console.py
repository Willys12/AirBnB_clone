#!/usr/bin/python3
"""
Entry point for the command interpreter.
"""

import cmd
import json
import os
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', datetime.now())

    def save(self):
        """Save the instance to a JSON file."""
        data = self.__dict__
        with open("instances.json", "a") as file:
            file.write(json.dumps(data) + "\n")

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        # Add other classes here
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
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Usage: show <class> <id>
        Prints the string representation of an instance based on the class name and id."""
        args = line.split()
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
        args = line.split()
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
        args = line.split()
        if len(args) > 1 and args[1] not in self.__classes:
            print("** class doesn't exist **")
        else:
            instances = self.load_all_instances(args[0] if len(args) > 0 else None)
            print(instances)

    def do_update(self, line):
        """Usage: update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name and id by adding or updating attribute."""
        args = line.split()
        if len(args) < 4:
            print("** missing arguments **")
        else:
            if self.update_instance(args[0], args[1], args[2], args[3]):
                print("Instance updated successfully.")
            else:
                print("** no instance found **")

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
