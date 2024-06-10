#!/usr/bin/env python3

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit command toe exit the code.
        Args:
            arg: any argument passed after thec command(not used)
        Returns:
            true to signal program terminateion
        """

        return True
    def do_EOF(self, arg):
        """
        End of file program to exit the file

        """
        return True
    def emptyline(self):
        """
        an empty line+Enter shouldnt execute anything.
        """
        pass

    def help_quit(self):
        """
        help text for the quit command.

        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        helps for the EOF command
        """
if __name__ == '__main__':
    HBNBCommand().cmdloop()
