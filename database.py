class InMemoryDB:
    """Class for a database stored in memory that supports transactions"""
    def __init__(self):

        self.__data: dict = {}
        self.__temp: dict = {}
        self.__transaction: bool = False

    def get(self, key: str) -> int | None:
        return self.__data.get(key, None) # lookup the key, return None if not found
    
    def put(self, key: str, val: int) -> None:
        if self.__transaction is False:
            raise ValueError("Transaction not in progress")
        
        self.__temp[key] = val # put the value in the temporary map

    def begin_transaction(self) -> None:
        if self.__transaction is True:
            raise ValueError("Transaction already in progress")
        
        self.__transaction = True # start the transaction
        self.__temp = {} # reset temporary data

    def commit(self) -> None:
        if self.__transaction is False:
            raise ValueError("Transaction not in progress")
        
        self.__transaction = False # stop the transaction
        self.__data |= self.__temp # merge temp data to main data
        self.__temp = {} # reset temporary data
        

    def rollback(self) -> None:
        if self.__transaction is False:
            raise ValueError("Transaction not in progress")
        
        self.__transaction = False # stop the transaction
        self.__temp = {} # reset temporary data

    
def main() -> None:
    inmemoryDB: InMemoryDB = InMemoryDB()
    
    # returns None because A doesn't exist in the database
    print(inmemoryDB.get("A"))

    # throws an error because the transaction is not in progress
    try:
        inmemoryDB.put("A", 5)
    except ValueError as e:
        print(e)
    
    # starts a transaction
    inmemoryDB.begin_transaction()

    # set's value of A to 5, but not committed yet
    inmemoryDB.put("A", 5)

    # returns None because updates to A are not committed yet
    print(inmemoryDB.get("A"))

    # update A's value to 6 within the transaction
    inmemoryDB.put("A", 6)

    # commits the transaction
    inmemoryDB.commit()

    # returns 6 because that was the last value of A to be committed
    print(inmemoryDB.get("A"))

    # Throws an error, because there is no open transaction
    try:
        inmemoryDB.commit()
    except ValueError as e:
        print(e)

    # Throws an error becasue there is no open transaction
    try:
        inmemoryDB.rollback()
    except ValueError as e:
        print(e)

    # Returns None because B doesn't exist in the database
    print(inmemoryDB.get("B"))

    # starts a new transaction
    inmemoryDB.begin_transaction()

    # set key B's value to 10 within the transaction
    inmemoryDB.put("B", 10)

    # Rollback the transaction (reverts any changes made to B)
    inmemoryDB.rollback()

    # returns None because the changes to B were rolled back
    print(inmemoryDB.get("B"))


if __name__ == "__main__":
    main()