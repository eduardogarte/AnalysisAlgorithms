""" Task definitions for invoke command line utility for python bindings
    overview article."""
    
import invoke 

@invoke.task
def clean(c):
    """Remove any built objects """
    for pattern in ["*.", "*.so"]:
        c.run("rm -rf {}".format(pattern))
@invoke.task
def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))
@invoke.task
def ford(c):
    """ Build the shared library for the sample C code"""
    print_banner("Building C Library")
    invoke.run("gcc -c -Wall -Werror -fpic ford.c -I /usr/include/python3.8")
    invoke.run("gcc -shared -o libford.so ford.o")
    print("* Complete")