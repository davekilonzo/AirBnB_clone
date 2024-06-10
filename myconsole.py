#!/usr/bin/env python3

import cmd

class command(cmd.Cmd):

    """this is a simple command line interpreter"""


    def do_greet(self,line):
        """greet the person <person>"""
        if line:
            print("Hello, ", line)
        else:
            print("Hi ")

    def help_greet(self):
        help_text = ["Greet the person.", "Usage: greet <person>"]
        print('\n'.join(help_text))


    def do_EOF(self, line):
        """Exit the console gracefuly"""
        return True

    def do_quit(self, line):
        """quit the application"""
        print("Quiting")
        return True
    def do_exit(self, line):
        """exit the application"""
        print("Exiting")
        return True
    def default(self, line):
        print(f"unknown command: {line}")
        return True

    



if __name__ ==  '__main__':
    command().cmdloop()



