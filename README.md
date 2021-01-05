# Calculator
A simple python calculator
Calculator currently supports:
  - Addition, subtraction, division and multiplication
  - Square and square root
  - Hold or reset memory and operate on previous value
  - Error handling
  - Invalid input handling
### Upcomming Features!

  - Trigonometric funcions

### Tech
Calculator uses a number of open source projects to work properly:

* [Python](https://www.python.org/) - The programming language for of this project
* [Python Math library](https://docs.python.org/3/library/math.html) - The library to implement square root
* [Pytest](https://docs.pytest.org/en/stable/) - Helps you write better programs by testing

## Installation
* Calculator requires Python 3 to run

#### You can either use the Calculator as a standalone version or as a python package

#### Installation as a standalone python project:

1) Clone the repository to a local directory

2) Create a virtual environment
    ```sh
    $ python -m venv venv
    ```
3) Activate the virtual environment
    ```sh
    $ venv\Scripts\activate.bat
    ```

4) Install required libraries
    ```sh
    $ pip install -r requirements.txt
    ```
    
#### Installation as a python module:
1) Create a virtual environment
    ```sh
    $ python -m venv venv
    ```
2) Activate the virtual environment
    ```sh
    $ venv\Scripts\activate.bat
    ```
3) Install the Calulator with pip
    ```sh
    $ pip install git+https://github.com/valdas-v1/turing_215_calculator
    ```
### Todos

 - Write MORE Tests
 - Add Night Mode

License
----

[MIT](LICENSE)