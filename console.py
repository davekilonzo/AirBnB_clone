<<<<<<< HEAD
#!/usr/bin/env python3
=======
#!/usr/bin/env python 3
>>>>>>> e2766cfbe3c1419f1e776f1ea115e5154f214786

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    """"HBNBCommand cmd that includes quit, EOF nad handling empty lines"""

    def do_quit(self, arg):
<<<<<<< HEAD
        """quit command toe exit the code.
        Args:
=======
        """quit command toe exit the code.  
        Args: 
>>>>>>> e2766cfbe3c1419f1e776f1ea115e5154f214786
            arg: any argument passed after thec command(not used)
        Returns:
            true to signal program terminateion
        """
        print("QUITING...")

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
    def do_hbnb(self,arg):
        """
        display a welcome message

        """
        print("WELCOME:")
    def help_prompt(self):
        """helpf for prompt message"""
        print("Display a welcome message")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
<<<<<<< HEAD

=======
>>>>>>> e2766cfbe3c1419f1e776f1ea115e5154f214786
