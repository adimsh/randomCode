//  this is a single-line comment
/*
    this is a multi-line comment
*/



/* 
    -Every file w/ extension .java is a class.

    -Classes in java are named groups of properties and functions.
    Class names must start w/ capital letters (convention).

    -So every java file must contain a class within it with the same name.
    All the code we write will be in this class
    This class must be public
*/

//package com.lecture8;
/*
    a package is a way to organize related classes(java files), and it maps directly to a folder (directory)
    
    -compiling a .java file(which is part of a package) is no different(we don't need to go to the root directory) 
    javac fileName.java 
    -but, to run a .class file(which is part of a package) we must go to the root directory(here, src) then specify the fileName along with the package i.e.
    (i) cd ../../ 
    (ii) java com.lecture8.fileName.java
*/

import java.util.Scanner;

public class Main {
    /* 
        -execution of a java prog starts from the main method
        static ensures we can execute the main function without creating an object of the Main class

        -String[] args is an array of String objects named args
        args holds command-line arguments passed when running the program.
        (basically inputs given at the start of program execution($java fileName input1 input2 ...) are stored in args as string values)
    */
    public static void main(String[] args){
        System.out.println("Hello, World!");
        // if we write System.out.print()- it does not add a new line


        // to take input
        Scanner input = new Scanner(System.in); // we need to import java.util.scanner
        // to print that input
        System.out.println(input.nextInt());
    }
}

/*
    -during compilation of .java  files, we can specify the folder in which we wish to store the .class files
    (this is standard practice, source code -> 'src' folder, byte code -> 'out' folder)
    syntax: javac -d .. fileName.java (the .. represent the previous/parent directory)
*/

// the $PATH variable is a colon-separated list of directories that the Bash shell searches to find executable files when you run a command. 
// Is it in .bashrc? --- Not by default. It is usually set system-wide in files like /etc/profile or /etc/environment. However, users often define custom paths in ~/.bashrc or ~/.profile to make changes permanent for their own sessions.
// How it works:    When you type a command, the shell checks each directory in the list from left to right. It executes the first matching file it finds; if nothing is found in those directories, you get a "command not found" error.


// To add a new folder to your $PATH permanently using your ~/.bashrc file, follow these steps:

// Open the file in a text editor like nano:
// nano ~/.bashrc
// Scroll to the very bottom and add this line (replace /your/new/folder with your actual directory):
// export PATH="$PATH:/your/new/folder"
// Save and exit (in nano, press Ctrl+O, Enter, then Ctrl+X).
// Apply the changes immediately to your current terminal session:
// source ~/.bashrc
// Key Command Breakdown
// $PATH (at the start of the value) ensures you keep all your existing search directories.
// :/your/new/folder appends your new folder to the list, using a colon as the separator.
// export ensures the updated variable is available to any programs you launch from that terminal. 