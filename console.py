#!/usr/bin/python3
"""
AirBnB Command-Line Interface (CLI) for interacting with the AirBnB data model.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for AirBnB. Handles user inputs and executes commands.
    """

    prompt = "(hbnb) "
    __all_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """
        Overrides default behavior for empty input lines.
        """
        pass

    def do_quit(self, arg):
        """
        Exits the command interpreter when called.
        """
        return True

    def do_EOF(self, arg):
        """
        Handles End-Of-File signal to exit the interpreter.
        """
        print("")
        return True

    def help_quit(self):
        """
        Displays help information for the quit command.
        """
        print("Exits the command interpreter.")

    def help_EOF(self):
        """
        Displays help information for the EOF signal.
        """
        print("Exits the command interpreter on EOF signal.")

    def do_create(self, args):
        """
        Creates a new instance of a specified class, saves it, and prints its ID.
        Usage: create <class_name>
        """
        if len(args) < 1:
            print("** class name missing **")
            return
        
        args = args.split()
        class_name = args[0]

        if class_name not in self.__all_classes:
            print("** class doesn't exist **")
            return

        new_object = eval(class_name + "()")
        new_object.save()
        print(new_object.id)
        storage.save()

    def do_show(self, args):
        """
        Displays the string representation of a class instance by ID.
        Usage: show <class> <id>
        """
        arg_list = args.split()
        objdict = storage.all()
        
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        elif arg_list[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        elif len(arg_list) == 1:
            print("** instance id missing **")
            return

        object_key = "{}.{}".format(arg_list[0], arg_list[1])

        if object_key not in objdict:
            print("** no instance found **")
            return
        else:
            print(objdict[object_key])

    def do_destroy(self, args):
        """
        Deletes an instance of a specified class by ID.
        Usage: destroy <class> <id>
        """
        arg_list = args.split()
        all_objects = storage.all()
        
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        class_name = arg_list[0]

        if class_name not in self.__all_classes:
            print("** class doesn't exist **")
            return
        
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        
        instance_id = arg_list[1]
        object_key = "{}.{}".format(class_name, instance_id)

        if object_key not in all_objects.keys():
            print("** no instance found **")
        else:
            del all_objects[object_key]
            storage.save()

    def do_all(self, args):
        """
        Displays all instances of a class or all objects if no class is specified.
        Usage: all or all <class>
        """
        arg_list = args.split()
        all_objects = storage.all()
        object_list = []
        
        if len(arg_list) == 0:
            for obj in all_objects.values():
                object_list.append(obj.__str__())
            print(list(object_list))
            return

        if len(arg_list) > 0 and arg_list[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        
        class_name = arg_list[0]
        object_list = []

        for obj in all_objects:
            if class_name == all_objects[obj].__class__.__name__:
                object_list.append(str(all_objects[obj]))
        print(object_list)

    def do_update(self, args):
        """
        Updates an instance of a class with a specified attribute.
        Usage: update <class> <id> <attribute_name> <attribute_value>
        """
        arg_list = args.split()
        all_objects = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        
        class_name = arg_list[0]

        if class_name not in self.__all_classes:
            print("** class doesn't exist **")
            return False

        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        
        instance_id = arg_list[1]
        object_key = "{}.{}".format(class_name, instance_id)

        if object_key not in all_objects:
            print("** no instance found **")
            return False

        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        
        attribute_name = arg_list[2]

        if len(arg_list) == 3:
            print("** value missing **")
            return False
        
        attribute_value = arg_list[3]

        if attribute_value.isdigit():
            if '.' in attribute_value:
                attribute_value = float(attribute_value)
            else:
                attribute_value = int(attribute_value)

        obj = all_objects[object_key]

        if attribute_name in obj.to_dict():
            attribute_original_type = type(obj[attribute_name])
            attribute_value = attribute_original_type(attribute_value)
            obj[attribute_name] = attribute_value
        else:
            obj.__dict__.update({attribute_name: attribute_value})

        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
