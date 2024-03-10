#!/usr/bin/python3
# My command interpreter.
import cmd
import json

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    models = {}

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
        An empty line + ENTER shouldn’t execute anything
        """
        pass

    def parse_args(self, arg):
        """
        Parses arguments, handling quoted strings with spaces.
        """
        args = []
        current_arg = ""
        in_quotes = False
        for char in arg:
            if char == '"':
                in_quotes = not in_quotes
                if not in_quotes and current_arg:
                    args.append(current_arg)
                    current_arg = ""
            elif char == ' ' and not in_quotes:
                if current_arg:
                    args.append(current_arg)
                    current_arg = ""
            else:
                current_arg += char
        if current_arg:
            args.append(current_arg)
        return args

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it and prints
        the id.
        """
        args = self.parse_args(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.models:
            print("** class doesn't exist **")
            return
        # Assuming BaseModel has a method to create a new instance
        instance = self.models[class_name].create()
        print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = self.parse_args(arg)
        if len(args) < 2:
            print("** class name or instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in self.models:
            print("** class doesn't exist **")
            return
        if instance_id not in self.models[class_name]:
            print("** no instance found **")
            return
        instance = self.models[class_name][instance_id]
        print(str(instance))

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = self.parse_args(arg)
        if len(args) < 2:
            print("** class name or instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in self.models:
            print("** class doesn't exist **")
            return
        if instance_id not in self.models[class_name]:
            print("** no instance found **")
            return
        del self.models[class_name][instance_id]
        print("Instance deleted")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        args = self.parse_args(arg)
        if len(args) > 1:
            class_name = args[0]
            if class_name not in self.models:
                print("** class doesn't exist **")
                return
            instances = self.models[class_name].values()
        else:
            instances = [instance for instances in self.models.values() for instance in instances.values()]
        print([str(instance) for instance in instances])

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute.
        """
        args = self.parse_args(arg)
        if len(args) < 4:
            print("** class name, instance id, attribute name, or value missing **")
            return
        class_name, instance_id, attr_name, attr_value = args[0], args[1], args[2], args[3]
        if class_name not in self.models:
            print("** class doesn't exist **")
            return
        if instance_id not in self.models[class_name]:
            print("** no instance found **")
            return
        instance = self.models[class_name][instance_id]
        setattr(instance, attr_name, attr_value)
        print("Instance updated")

    def process_commands(self, commands):
        """Processes a list of commands in non-interactive mode."""
        for command in commands:
            if command.startswith('do_'):
                command = command[3:]
            self.onecmd(command)

if __name__ == '__main__':
    # Example usage in non-interactive mode
    commands = [
        'create BaseModel',
        'show BaseModel 1234-1234-1234',
        'destroy BaseModel 1234-1234-1234',
        'all BaseModel',
        'update BaseModel 1234-1234-1234 email "aibnb@mail.com"'
    ]
    HBNBCommand().process_commands(commands)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
