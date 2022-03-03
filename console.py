#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Interprete de comandos"""
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """EOF command to exit the program\n"""
        print()
        return(True)

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return(True)

    def emptyline(self):
        """No realiza ninguna accion"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel\n"""
        if args == "":
            print("** class name missing **")
        elif args == "BaseModel":
            new = BaseModel()
            storage.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance based on the class name and id\n"""
        list_ = args.split()
        if len(list_) == 0:
            print("** class name missing **")
        elif list_[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(list_) == 1:
            print("** instance id missing **")
        else:
            list_key = list_[0] + "." + list_[1]
            #storage.all() es un diccionario de varios elementos
            #{key1,val1;key2,val2;...}
            dict_ = storage.all()
            #Falta revisar si encuantra key
            if list_key in dict_.keys():
                print(dict_[list_key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id\n"""
        list_ = args.split()
        if len(list_) == 0:
            print("** class name missing **")
        elif list_[0] != "BaseModel":
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
        """Quit command to exit the program\n"""
        return(True)

    def do_update(self, args):
        """Quit command to exit the program\n"""
        return(True)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
