class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name

        if not hasattr(self, 'value'):
            self.value = 0

        if isinstance(self.value, int):
            if self.value < 0:
                raise AttributeError("Attribute value cannot be negative.")
            if not isinstance(self.name, str):
                raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if isinstance(new_account, Account) and not new_account.id in [account.id for account in self.accounts]:
            self.accounts.append(new_account)
            return True
        return False

    @staticmethod
    def __donothing(self):
        pass
    @staticmethod
    def __checkNbAttr(account):
        if len(account.__dict__) % 2 == False:
            return False
        return True

    @staticmethod
    def __fixNbAttr(account):

        test = 0
        for attr in account.__dict__:
            if attr != 'name' and attr != 'zip' and attr != 'value' and attr != 'id' and attr != 'ID_COUNT':
                test = attr
        if test:
            account.__dict__.pop(test)
        else:
            account.foo = 'bar'

    @staticmethod
    def __checkLocation(account):
        attrList = dir(account)
        for attr in attrList:
            if attr[0:3] == 'zip' or attr[0:4] == 'addr':
                return True
        return False

    @staticmethod
    def __fixLocation(account):
        account.__dict__.update(zip='911-745')

    @staticmethod
    def __checkName(account):
        attrList = dir(account)
        if 'name' in attrList:
            return True
        return False

    @staticmethod
    def __fixName(account):
        pass

    @staticmethod
    def __checkId(account):
        attrList = dir(account)
        if 'id' in attrList:
            return True
        return False

    @staticmethod
    def __fixID(account):
        account.__dict__.update(id=account.ID_COUNT)
        Account.ID_COUNT += 1

    @staticmethod
    def __checkValue(account):
        attrList = dir(account)
        if 'value' in attrList:
            return True
        return False

    @staticmethod
    def __fixValue(account):
        account.__dict__.update(value=0.0)

    @staticmethod
    def __checkIdType(account):
        if isinstance(account.id, int):
            return True
        return False

    @staticmethod
    def __checkValueType(account):
        if isinstance(account.value, int) or isinstance(account.value, float):
            return True
        return False

    @staticmethod
    def __checkB(account):
        attrList = dir(account)
        for attr in attrList:
            if attr[0] == 'b':
                return False
        return True

    @staticmethod
    def __fixB(account):
        attrList = dir(account)
        for attr in attrList:
            if attr[0] == 'b':
                account.__dict__.pop(attr)


    controllers = [
                    (__checkName, __fixName),
                    (__checkLocation, __fixLocation),
                    (__checkId, __fixID),
                    (__checkIdType, __fixID),
                    (__checkValue, __fixValue),
                    (__checkValueType, __fixValue),
                    (__checkB, __fixB),
                    (__checkNbAttr, __fixNbAttr)
                ]

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        client = [0, 0]
        for account in self.accounts:
            if account.name == origin:
                if False in [func[0](account) for func in self.controllers]:
                    return False
                client[0] = account
            if account.name == dest:
                if False in [func[0](account) for func in self.controllers]:
                    return False
                client[1] = account

        if amount > 0 and client[0].value >= amount:
            client[0].transfer(amount * (-1))
            client[1].transfer(amount)
            return True
        return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        wichAccount = 0
        for account in self.accounts:
            if account.name == name:
                wichAccount = account
                break
        else:
            return False
        testList = []
        for checker in self.controllers:
            testList.append(checker[0](wichAccount))
            if checker[0](wichAccount) == False:
                checker[1](wichAccount)
        return True


