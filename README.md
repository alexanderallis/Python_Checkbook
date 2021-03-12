# Python_Checkbook
A python program that acts as a checkbook and facilitates the act of balancing it.

## How to Run
Download the latest version of Python IDLE from https://www.python.org/downloads/

Open main.py in IDLE.

Press F5 or choose Run > Run Module

Interact with IDLE like you would any UNIX Terminal or Command Line, it takes only text input.

## How to Operate the Program
The program will prompt you for a password.
The password is "asdf".

You will see the following menu option:

1: User Verified 	 	Current Balance: $121.00
2: Add, Edit, Void a check
3: Add, Edit, Void a deposit
4: Reconcile with the Bank
5: Exit

The checkbook balance will update when the user adds, edits, or voids checks or balances. "Reconcile with the Bank" allows for the user to override the current balance with the figure from the bank.

## How the Program Works
The program creates a file called "balance.txt" that stores the value of the bank account balance.
The program creates a file called "data.txt" that stores a list of checks.

By storing essential data to the computer's hard drive in a text file, the checkbook data remains continuous even if the user exits the program.
