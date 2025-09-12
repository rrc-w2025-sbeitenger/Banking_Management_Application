# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.
Each assignment will build on the work done in the previous assignment(s).
Ultimately, an entire system will be created to manage bank transactions 
for clients who have one or more bank accounts.

## Author
Sven Beitenger

## Assignment
Assignment 1: This assignment will be using encapsulation and unit testing to 
build a client and bank account systems.

## Encapsulation
Encapsulation was achieved by making 'private' attributes. Name mangling the in
the constructor by adding double underscore to the atrributes, and then creating
getter properties so I can access the attributes without accidentally bypassing
encapsulation and messing with attribute directly. I am using getter propeties
so I can prevent direct access and raise valuerrors if the wrong argument was
entered. Within all my functions in the BankAccount class I am using the
name mangled attributes.