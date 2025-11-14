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

Assigment 3: This assignment will be using Strategy Patterns to simplify and 
add scalability. And will add observer patterns to send notifications to clients.

Assignment 4: This assignment will include a graphical user interface where users
can select their bank account data and deposit or withdraw transactions.

## Encapsulation (A1):
Encapsulation was achieved by making 'private' attributes. Name mangling the in
the constructor by adding double underscore to the atrributes, and then creating
getter properties so I can access the attributes without accidentally bypassing
encapsulation and messing with attribute directly. I am using getter propeties
so I can prevent direct access and raise valuerrors if the wrong argument was
entered. Within all my functions in the BankAccount class I am using the
name mangled attributes.

## Polymorphism (A2):
Polymorphism was achieved by implementing abstract classes and methods.
Polymorpism allows subclasses to access the abstract method in the abstract
superclass. I can declare the abstract get_service_charges method in the
superclass and then each other subclass, such as ChequingAccount, InvementAccount,
and SavingsAccount can implement this method differently. I used this to
create different service charges for each account type.

## Strategy Pattern (A3):
Strategy Patterns are implemented to allow the classes inwhich are inherting from
BankAccount to use innerchangable code/algorthims. Such as overdraft fees, management fees, and 
minimum balance. Instead of hard codeing them into each method, each strategy pattern has their
respected code/algorthim, from which a class can then choose a strategy pattern. This reduces
code reducncy, and supports "scalable when it comes to adding extra BankAccounts or new service
charge rules" - Notes.
Each class of the inhertied BankAccount class is calling a certain strategy pattern to support their
needed calculations within get_service_charges().

## Observer Pattern (A3):
Observer Pattern is implemented into the application so the client can be the observer of the BankAccount.
The client inherits from the Observer class, and the BankAccount inherits from the Subject class.
The Subject class is dependent on the observer class since if any changes happen that raise an alert, like
withdrawing over the 9999.99 threshold, or being bellow the minimum balance limit the observer(client) wants to know.
Since BankAccount is inherting from Subjects, that means all the of BankAccounts subclass are also Subjects.
SavingsAccount, ChequingsAccount, InvestmentAccounts are subjects which will notify the observer.

## Event-Driven programming paradigm (A4):
Event-Driven programming was added into this application by creating event handlers methods and event listeners from pyside6.
It responds to user driven events, such as mouse clicks, or button presses, by signaling the correct slot method.
For client_look_up.py and manage_data.py modules the init() method acts as a 'connection hub' for most of the
event handlers and event listeners (slot methods, and signals). Each @Slot() method is a event handler that reacts
to a specific event/signal when it occurs, the slot will exacute it's inner code. In this application event listner
signals are emitted by pyside6 widgets, such as QPushButtons, QLineEdits, QTableWidget and even a custom singal that connects
the object of AccountDetailWindow to update_data. For example: The buttons widgets clicked signals the the slot method,
button.clicked.connect.(@Slot()).