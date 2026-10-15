# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several sprints.
Each sprint will build on the work done in the previous sprint(s).
Ultimately, an entire system will be created to manage bank transactions 
for clients who have one or more bank accounts.

## Author
Sven Beitenger

## Sprint
Sprint 1: This sprint will be using encapsulation and unit testing to 
build a client and bank account systems.

Sprint 2: This sprint will be using superclasses and subclasses using
inheritance hierarchy. Will include the use of polymorphism and abstraction.

Sprint 3: This sprint will be using Strategy Patterns to simplify and 
add scalability, including observer patterns to send notifications to clients.

Sprint 4: This sprint will include a graphical user interface where users
can select their bank account data and deposit or withdraw transactions.

## Encapsulation (A1):
Encapsulation was achieved by making the class attributes private through name mangling.
In the constructor, I added double underscores (__) to the attributes, which prevents direct
access from outside the class. I then created getter properties to provide controlled access
to these attributes without bypassing encapsulation or modifying them directly. Getter properties
also allow me to validate input and raise ValueError exceptions when invalid arguments are provided.
Throughout the BankAccount class, all methods access the name-mangled attributes directly to maintain
encapsulation and ensure consistent data handling.

## Polymorphism (A2):
Polymorphism was achieved by implementing abstract classes and abstract methods. Polymorphism allows
subclasses to provide their own implementation of a method that is declared in an abstract
superclass. For example, I declared the abstract get_service_charges() method in the superclass,
and each subclass, such as ChequingAccount, InvestmentAccount, and SavingsAccount, implements this
method differently. This approach allows each account type to calculate and apply its own service
charges while maintaining a consistent method interface across all account classes. As a result,
the program can treat all account types uniformly while still executing account-specific behavior.

## Strategy Pattern (A3):
The Strategy Pattern was implemented to allow classes that inherit from BankAccount to use interchangeable
algorithms for calculating service charges. Examples of these algorithms include overdraft fees,
management fees, and minimum balance fees. Instead of hard-coding these calculations into each
account class, the logic is encapsulated within separate strategy classes, each responsible for
its own calculation algorithm. This design reduces code redundancy and improves maintainability
by separating business rules from the account classes. It also makes the system more scalable,
as new account types or service charge rules can be added without modifying existing code.
Each subclass that inherits from BankAccount selects and uses the appropriate strategy pattern
to perform the calculations required by its get_service_charges() method. This allows account-specific
behavior while promoting code reuse and flexibility.

## Observer Pattern (A3):
The Observer Pattern was implemented in the application to allow the client to act as an observer of a BankAccount.
The Client class inherits from the Observer class, while the BankAccount class inherits from the Subject class.
The Subject class maintains a relationship with its observers and notifies them whenever significant events occur.
For example, alerts are generated when a withdrawal exceeds the $9,999.99 threshold or when an account balance falls
below the minimum required balance. In these situations, the observer (Client) is notified of the change.
Since BankAccount inherits from Subject, all subclasses of BankAccount are also subjects. As a result,
classes such as SavingsAccount, ChequingAccount, and InvestmentAccount can notify observers when account-specific
events or alerts occur. This design promotes loose coupling between account objects and clients, allowing notifications
to be sent automatically without requiring direct dependencies between the classes.

## Event-Driven programming paradigm (A4):
Event-Driven programming was added into this application by creating event handlers methods and event listeners from pyside6.
It responds to user driven events, such as mouse clicks, or button presses, by signaling the correct slot method.
For client_look_up.py and manage_data.py modules the init() method acts as a 'connection hub' for most of the
event handlers and event listeners (slot methods, and signals). Each @Slot() method is a event handler that reacts
to a specific event/signal when it occurs, the slot will execute it's inner code. In this application event listener
signals are emitted by pyside6 widgets, such as QPushButtons, QLineEdits, QTableWidget and even a custom signal that connects
the object of AccountDetailWindow to update_data. For example: The buttons widgets clicked signals the the slot method,
button.clicked.connect.(@Slot()).

## Filtering Data and Creating Installer (A5):
Note: In this context, the terms item and cell are used interchangeably.

Filtering was implemented by iterating through each row of the accounts table and checking whether the selected
table cell contains the filter text entered by the user. The selected cell is determined using the current row
index from the iteration and the column index obtained from filter_combo_box.currentIndex().
This approach works because each option in the filter_combo_box corresponds directly to a column in the accounts
table, such as Account Number, Balance, Creation Date, or Account Type. In other words, the index of the selected
combo box item matches the index of the column that should be filtered.

When the filter button's text is set to "Apply Now", the filtering process begins. For each row, the program retrieves
the value in the selected column and checks whether it contains the specified filter text. If the filter text is not
found within the cell, the entire row is hidden. Otherwise, the row remains visible. After the filtering process is complete,
the __toggle_filter(True) method is called to indicate that the table is currently filtered. This updates the user interface
to show that a filter is active and prevents the filter criteria from being modified until the filter is reset.

When __toggle_filter(False) is called, the filter is removed. The method iterates through all table rows, unhides any hidden rows, and restores the original table view so that all account records are visible again.

