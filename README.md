# Data Processing and Storage Assignment

## Writeup
To further clarify the instructions, websites that have an interactive demo of a transactional database would be nice. I think that this assignment could also have the students implement a Unit Test in their desired language to also teach how to test code. This could also make it easier to grade, as the students could submit a screenshot of their tests passing, for example.

## Requirements

1. **Clone the repository:**  
    ```sh
    git clone https://github.com/Seedname/DataProcessing.git
    cd DataProcessing
    ```

2. **Python version >=3.10**  
    Link to install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Using the API

To test the database API for the `InMemoryDB` class, you can run `database.py` and it will automatically print the expected outputs of the program from the assignment to the terminal. 

To test the API directly, I recommend using `test.py` and calling functions after line 7. Make sure to put methods that can throw errors in `try/except` blocks to avoid crashes. A reference can be found below.

### API Reference

#### Constructor

##### `__init__()`
- **Description**:  
  Initializes the InMemoryDB class

---

#### Methods

##### `get(key: str) -> int | None`
- **Description**:  
    Retrieve the value from the database, or `None` if not found
- **Input**:  
  - `key` (str):  
    Lookup key for value
- **Output**:  
  - `int` or `None`:  
    Value if found or `None` if not found
- **Errors**:  
  - _None_

---

##### `put(key: str, val: int) -> None`
- **Description**:  
  Puts the key/value pair in the database
- **Input**:  
  - `key` (str):  
    Lookup key for value
  - `val` (int):  
    Value to put in database
- **Output**:  
  - _None_
- **Errors**:  
  - `ValueError`  
    Throws an error if this is called and a transaction has not been started 

---

##### `begin_transaction() -> None`
- **Description**:  
  Start a new transaction
- **Input**:  
  - _None_
- **Output**:  
  - _None_
- **Errors**:  
  - `ValueError`  
    Throws an error if this is called and a transaction has already been started

---

##### `commit() -> None`
- **Description**:  
  Commit the temporary changes to the database
- **Input**:  
  - _None_
- **Output**:  
  - _None_
- **Errors**:  
  - `ValueError`  
    Throws an error if this is called and a transaction has not been started 

---

##### `rollback() -> None`
- **Description**:  
  Rollback the changes (erase the temporary data)
- **Input**:  
  - _None_
- **Output**:  
  - _None_
- **Errors**:  
  - `ValueError`  
    Throws an error if this is called and a transaction has not been started 
