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

Assignment 2: This assignment will be using superclasses and subclasses using
inheritance hierarchy. Will include the use of polymorphism and abstaction.

Assigment 3: This assigment will be using Strategy Patterns to simplify and 
add scalability. And will add observer patterns to send notifications to clients.

## Encapsulation (A1)
Encapsulation was achieved by making 'private' attributes. Name mangling the in
the constructor by adding double underscore to the atrributes, and then creating
getter properties so I can access the attributes without accidentally bypassing
encapsulation and messing with attribute directly. I am using getter propeties
so I can prevent direct access and raise valuerrors if the wrong argument was
entered. Within all my functions in the BankAccount class I am using the
name mangled attributes.

## Polymorphism (A2)
Polymorphism was achieved by implementing abstract classes and methods.
Polymorpism allows subclasses to access the abstract method in the abstract
superclass. I can declare the abstract get_service_charges method in the
superclass and then each other subclass, such as ChequingAccount, InvementAccount,
and SavingsAccount can implement this method differently. I used this to
create different service charges for each account type.