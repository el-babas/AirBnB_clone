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
    cmd_list = ['create', 'show', 'update', 'all', 'destroy', 'count']

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

    def precmd(self, args):
        """parses command input"""
        if '.' in args and '(' in args and ')' in args:
            cm_class = args.split('.')
            cm_action = cm_class[1].split('(')
            cm_args = cm_action[1].split(')')
            if (cm_class[0] in HBNBCommand.class_dict.keys() and
                    cm_action[0] in HBNBCommand.cmd_list):
                args = cm_action[0] + ' ' + cm_class[0] + ' ' + cm_args[0]
        return args

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
        if len(tokens) == 0:
            print([str(i) for i in storage.all().values()])
        elif tokens[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        else:
            print([
                str(i) for i in storage.all().values()
                if tokens[0] == i.__class__.__name__
            ])

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

    def do_count(self, args):
        """counts number of instances of a class"""
        count = 0
        tokens = args.split()
        all_objects = storage.all()
        for obj in all_objects.values():
            if obj.__class__.__name__ == tokens[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
