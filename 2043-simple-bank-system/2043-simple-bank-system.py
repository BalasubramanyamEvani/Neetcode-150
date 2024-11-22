class Bank:

    def __init__(self, balance: List[int]):
        self._N = len(balance)
        self._accounts = {i: balance[i] for i in range(self._N)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not(self._check_account_number(account1) and self._check_account_number(account2)):
            return False
        if not self._has_money(account1, money):
            return False
        self._accounts[account1 - 1] -= money
        self._accounts[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._check_account_number(account):
            return False
        self._accounts[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._check_account_number(account):
            return False
        # check if money
        if not self._has_money(account, money):
            return False
        self._accounts[account - 1] -= money
        return True
    
    def _check_account_number(self, account: int) -> bool:
        return 1 <= account <= self._N
    
    def _has_money(self, account: int, money: int) -> bool:
        return self._accounts[account - 1] >= money

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)