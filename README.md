<h1 align="center">alu-AirBnB</h1>
<p align="center">An AirBnB clone project.</p>

---

## Description

alu-AirBnB is a full stack web application that replicates main functionalities of AirBnB App. It integrates database, a back-end API, and a front-end. This is the foundational of a larger project, with CLI for managing data, including user and place objects, and setting up the base classes for future expansions like HTML/CSS , database storage, APIs, and front-end integration etc.

### Key Features
- Custom CLI to manage application data
- Supports(CRUD) operations, create, read, update, and delete for different objects 
- BaseModel class for handling serialization/deserialization of objects
- File storage engine 
- Unit tests 

## How to Start

To start the command interpreter:

 Clone this repository:
    ```bash
    using git clone 
    cd cloned project
    ```
 Start the command interpreter:
    ```bash
    ./console.py
    ```

## Usage

In the command-line interpreter, you can:

- Create a new object (e.g., User, Place):
    ```bash
     create User
     create Place
    ```

- Retrieve an object:
    ```bash
    show User <user_id>
    ```

- Update attributes of an object:
    ```bash
     update User <user_id> name "New Name"
    ```

- Delete an object:
    ```bash
     destroy User <user_id>
    ```

- Quit the interpreter:
    ```bash
    quit
    ```

## Author

- **Elissa Twizeyimana** - [twizelissa](https://github.com/twizelissa) - <e.twizeyima@alustudent.com>
- **Carine Ahishakiye YIBUKABAYO** - [carine-ahishakiye](https://github.com/carine-ahishakiye) - <c.yibukabay@alustudent.com>
 