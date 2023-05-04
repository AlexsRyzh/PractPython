import deal


@deal.inv(lambda account: account.balance >= 0)
class BankAccount:

    @deal.pre(lambda self, account_number, balance=0: type(account_number) == type('') and balance >= 0)
    def __init__(self, account_number, balance=0):
        self.balance = balance
        self.account_number = account_number

    @deal.pre(lambda self, amount: amount > 0)
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    @deal.pre(lambda self, amount: amount > 0)
    def withdraw(self, amount):
        self.balance -= amount
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        return f"Баланс счета {self.account_number}: {self.balance}"
