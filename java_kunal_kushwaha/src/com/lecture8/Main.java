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
    }
}

/*
    -during compilation of .java  files, we can specify the folder in which we wish to store the .class files
    (this is standard practice, source code -> 'src' folder, byte code -> 'out' folder)
    syntax: javac -d .. fileName.java (the .. represent the previous/parent directory)
*/