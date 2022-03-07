
<h1 align="center" >
<br>
    <img src="https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg" height="50%" width="30%">
</h1>

<h2 align="center">
    AirBnB (clone)
</h2>

<p align="center">
<img src="https://user-images.githubusercontent.com/68792144/141602345-7b71c4ea-a4dd-42d9-b706-7fc2c7b85ca5.png" height="50%" width="20%">
</p>

<p align="center">
    <a href="https://github.com/cristhian1107/printf/commits/main">
        <img src="https://img.shields.io/github/last-commit/cristhian1107/AirBnB_clone.svg?style=flat-square&logo=github&logoColor=white" alt="GitHub last commit">
    </a>
    <a href="https://github.com/cristhian1107/printf/issues">
    <img src="https://img.shields.io/github/issues-raw/cristhian1107/AirBnB_clone.svg?style=flat-square&logo=github&logoColor=white"
         alt="GitHub issues">
    </a>
    <a href="https://github.com/cristhian1107/printf/pulls">
    <img src="https://img.shields.io/github/issues-pr-raw/cristhian1107/AirBnB_clone.svg?style=flat-square&logo=github&logoColor=white"
         alt="GitHub pull requests">
    </a>
</p>

<h4 align="center"> This project is WepApp in Python </h4>

<p align="center">
    <a href="#Description">Description</a> •
    <a href="#The console">The console</a> •
    <a href="#Contact Information">Contact Information</a> •
</p>


# Description
This project is the first step of the AirBnB project, which is an AirBnB clone that includes design, layout, infrastructure and database.

It consists of the implementation of a command line interface in the PYTHON programming language, which simulates the interaction with a RESTful API and data persistence. As well as basic functions such as create, show, update, destroy that simulate a CRUD (Create, Read, Update, Delete) of a lifetime towards a database.

We will not implement all the features, just some of them to cover all the fundamental concepts of the higher level programming track.

# The console

<p align="center"><img src="https://user-images.githubusercontent.com/68792144/141602516-90e36740-e66e-4edd-8baf-08f318b10a58.png" width="700"></p>

## Install
```shell
git clone https://github.com/cristhian1107/AirBnB_clone.git
```

## Execution
`Interactive Mode`
 ```shell
 $ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
 ```
`Non-Interactive Mode`
```shell
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Commands
| CMD   | Description | Usage |
|--------|--------|--------|
| **`help`**   | Displays help manual and usage of command specified | `help` `<command>` <br> `help`|
| **`quit`**   | Exit the program | `quit` |
| **`EOF`**    | Exit the program | `EOF` <br>`Ctrl + D`|
| **`create`** | Creates new id for a new class | `create <class name>` |
| **`show`**   |  Prints the string representation of an instance based on the class name  | `show <class name> id`|
| **`destroy`**| Deletes an instance based on the class name and id | `destroy <class name> id`|
| **`all`**    | Prints all string representation of all instances based or not on the class name | `all` <br> `all <class name>`|
| **`update`** | Updates an instance based on the class name and id by adding or updating attribute | `update <class name> <id> <attribute> <value>` |

# Contact Information
Please feel free to contact us regarding any matter (specially about mistakes, recomendations and gramar errors)

<p align="center">
Cristhian Apaza - 
<a href="https://github.com/cristhian1107">
        <img src="https://img.shields.io/badge/Cristhian-mainPage-blue">
</a>
</p>



<p align="center">
Jairo Castillo -
<a href="https://github.com/j4ir0st">
        <img src="https://img.shields.io/badge/Jairo-mainPage-blue">
</a>
</p>
