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
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        else:
            new_model = HBNBCommand.class_dict[args]()
            print(new_model.id)
            new_model.save()

    def do_show(self, args):
        """Prints the string representation of an instance\n"""
        if not args:
            print("** class name missing **")
            return

        l_args = args.split(' ')
        if l_args[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(l_args) == 1:
            print("** instance id missing **")
        else:
            object_dict = storage.all()
            for key, obj in object_dict.items():
                obj_name = obj.__class__.__name__
                obj_id = obj.id
                if obj_name == l_args[0] and obj_id == l_args[1].strip('"'):
                    print(obj)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id\n"""
        list_ = args.split()
        if len(list_) == 0:
            print("** class name missing **")
        elif list_[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(list_) == 1:
            print("** instance id missing **")
        else:
            list_key = list_[0] + "." + list_[1]
            dict_ = storage.all()
            if list_key in dict_.keys():
                del dict_[list_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances\n"""
        list_ = args.split()
        if len(list_) == 0:
            print([str(i) for i in storage.all().values()])
        elif list_[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        else:
            print([
                str(i) for i in storage.all().values()
                if list_[0] == i.__class__.__name__
            ])

    def do_update(self, args):
        """Updates an instance by adding or updating its attribute \n"""
        list_ = args.split()
        list_key = list_[0] + "." + list_[1]
        dict_ = storage.all()
        if len(list_) == 0:
            print("** class name missing **")
        elif list_[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(list_) == 1:
            print("** instance id missing **")
        elif list_key not in dict_.keys():
            print("** no instance found **")
        elif len(list_) == 2:
            print("** attribute name missing **")
        elif len(list_) == 3:
            print("** value missing **")
        else:
            if list_key in dict_.keys():
                setattr(dict_[list_key], list_[2], list_[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
