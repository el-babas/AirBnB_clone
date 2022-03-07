#!/usr/bin/python3
"""
Class
    6) HBNBCommand
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class:
        HBNBCommand that defines all common attributes/methods
        for other classes.
    """
    prompt = "(hbnb) "
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_EOF(self, args):
        """EOF command to exit the program\n"""
        print("")
        return True

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Does not perform any action"""
        pass

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def do_create(self, args):
        """Creates a new instance of BaseModel\n"""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        else:
            new_model = HBNBCommand.class_dict[tokens[0]]()
            new_model.save()
            print(new_model.id)

    def do_show(self, args):
        """Prints the string representation of an instance\n"""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif (tokens[0] + "." + tokens[1]) not in list(storage.all().keys()):
            print("** no instance found **")
        else:
            print(storage.all()[tokens[0] + "." + tokens[1]])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id\n"""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif (tokens[0] + "." + tokens[1]) not in list(storage.all().keys()):
            print("** no instance found **")
        else:
            all_objects = storage.all()
            del all_objects[tokens[0] + "." + tokens[1]]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances\n"""
        tokens = args.split()

        if tokens[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            list_instances = []
            for key, obj in all_objects.items():
                obj_name = obj.__class__.__name__
                if obj_name == tokens[0]:
                    list_instances += [obj.__str__()]
            print(list_instances)

    def do_update(self, args):
        """Updates an instance by adding or updating its attribute \n"""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif (tokens[0] + "." + tokens[1]) not in list(storage.all().keys()):
            print("** no instance found **")
        elif len(tokens) == 2:
            print("** attribute name missing **")
        elif len(tokens) == 3:
            print("** value missing **")
        else:
            all_objects = storage.all()
            current_object = all_objects[tokens[0] + "." + tokens[1]]
            att = tokens[2]
            val = tokens[3].strip("\"")
            setattr(
                current_object,
                att,
                val
            )
            current_object.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
