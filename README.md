# debit-credit-capital-bank

**Techstack:** Python-Django Stack

**Languages:** HTML, CSS, SQL, Python

**Business Rules and Requirements**

The bank name is Debit-Credit Capital. The database name is the bank name as well.

The bank has multiple branches throughout the world and is identified by a unique Branch ID. Each branch also has a name and address. Every branch is assigned with a manager and an assistant manager.

The bank has numerous customers. The customers are identified by the Social Security Number. The basic demographic information like the customer’s name, address are collected in the branch. One customer is associated with at least one branch. A customer can have bank accounts in multiple branches and in every branch, the customer is assigned a personal banker who helps with the day-to-day banking activities and transactions.

Debit-Credit Capital employs a variety of people around the world and every employee is identified using their Social Security Number. Furthermore, the employee details such as Address, Phone Number and Designation are collected for auditing purposes. If the employee has dependents, the dependents details are collected as well. An employee works at only one branch at a given time and the start date and length of employment are stored in order to award the employees on their work anniversaries. Every employee reports directly to the Branch Manager and the branch manager is ultimately responsible for the branch.

There are different types of accounts offered namely, Savings, Checking, Money Market and Loan accounts. Accounts can be held by more than one customer leading to a joint account and one customer is allowed the option to hold multiple account types as well. The account of a customer is identified by a unique account number and details such as the current account balance, account opening date, closing date, account type and the latest account access date time is recorded. Moreover, the overdraft amount of the checking account is recorded and the interest rates offered for savings, money market and loan accounts are also recorded.

In today’s world, most transactions are digital. Every customer gets the option of having a card for their account. Types of cards offered are Credit Card and Debit Card. The card details like card number, cardholder name, cvv, valid from date time and expiry date time are stored in the system. An account can have multiple cards like credit and debit and if the account is a joint account, each account holder has the option to have individual cards.

The deposits offered to the customers are fixed deposits and recurring deposits. An account can have multiple deposits to its name and it is identified using a unique Deposit Number. Deposit Date Time, Deposit type, Interest Frequency, Maturity Date Time and Deposit Amount are the information stored in the system.

Loan accounts are one of the key features of the bank. A customer can have multiple loans to his name and account. A loan is identified using a unique Loan Number. Information about the loan like Loan amount and monthly loan repayment amount is stored in the system. A loan belongs to a branch to indicate its origination. 

Every single transaction is recorded against the accounts and it is uniquely identified using the Transaction Code. In order to indicate whether a transaction is debit or credit, a debit_credit_flag is used. Transaction amount, transaction date and time, account number and transaction type are information that identifies a transaction. An account can have a tonne of transactions going through and away from it. The bank does not charge for digital transactions.

**Entities & Relationships**
The entities identified are BRANCH, CUSTOMER, ACCOUNTS, EMPLOYEE, TRANSACTION_LOG, DEPOSITS, CARDS, LOAN, DEPENDENTS.

The relationships identified and the assumptions made are:

Branch_Cust - A customer belongs to the branch and one customer can belong to multiple branches and one branch can have multiple customers. Hence, a many-to-many relationship exists between Branch and Customer entities with Total Participation from both.

Cust_Employee - A customer is assigned a personal banker and there can be many personal bankers for the customer but there is no need for an employee to be a personal banker. Hence, a many-to-many relationship is identified between Customer and Employee entities with Total Participation from Customer and Partial Participation from Employee.

Brnch_Employee - One employee belongs to only one branch but more than one employee can be in a branch. Hence, many-to-one participation between employee and branch with total participation from both.

Dependents_Of - This is a weak relationship since the dependents is a weak entity with partial participation from employee and total participation from dependents and many-to-one relationship between dependents and employee.

Depositor - Customer deposits amount to Account, Total Participation from both entities and 1-to-many relationship since customers can have many accounts but one account belongs to one customer.

Loan_Taken - Customers take many loans. One loan belongs to many customers. Many-to-many relationship with total participation from loans and partial from customer.

Acct_trans - Account and Transaction_Log entities. One-To-many relationship with total participation from both.

Card_Acct - Cards and Accounts entities. One-to-many relationship with total participation from Cards and partial participation from accounts.

Dpst_Acct - Deposit and Account entities. One-to-many relationship with total participation from deposits and partial from deposits.

Savings accounts, checking accounts, money market accounts and loan accounts are specialization entities (i.e.) subclasses of the entity Accounts.

**Entity Relationship**
![image](https://user-images.githubusercontent.com/101942244/209606049-e43fca9b-74a8-4566-9dd4-b7fcc766dd79.png)

**Relational Schema**
![image](https://user-images.githubusercontent.com/101942244/209608844-98ca873e-6c81-458a-833f-222dcebe49e3.png)

**Application Program Design**
![image](https://user-images.githubusercontent.com/101942244/209609102-d73ca173-3745-4e2d-87b6-5c5b7f4096ab.png)
