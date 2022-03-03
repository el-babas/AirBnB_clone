#!/usr/bin/env python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Interprete de comandos"""
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """EOF command to exit the program\n"""
        return(True)

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return(True)

    def emptyline(self):
        """No realiza ninguna accion"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
