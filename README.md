# BrebeufHx 4 - Python Workshop (Web Development Version) (Part 2/2)

Hello there!

This is the web development version of the workshop.

If you are a beginner to Python, it would be best to first master the [simple version
of this workshop (part 1)](https://github.com/TheFloatingString/bhx-4-python-simple) before
starting this web development version.

The goal is to integrate an HTML frontend that can call Python functions through a 
[Flask](https://flask.palletsprojects.com/en/1.1.x/) web app.

The concepts that are used are:
- variable types
- if/else statements
- functions
- modules 
- package installation
- HTTP routing
- HTML layout

## Python Installation

Python installation instructions are also found in 
the [simple workshop repository's `README.md` file](https://github.com/TheFloatingString/bhx-4-python-simple).

## Installing Flask locally

Flask (version 1.1.2) can be installed through cmd or Terminal with the following command for Windows:

```bash
pip install flask==1.1.2
```

and the following command for MacOs/Linux:

```bash
pip3 install flask==1.1.2
```

## Installing Flask on Repl.it

Create a Python Repl. On the left sidebar, go to `Packages`, click the plus button, and add Flask.

## Directory structure

- `main.py` is the web app 

- `templates` is a mandatory folder for Flask to identify HTML pages

- `index.html` is the HTML file that `main.py` renders

## Running on Repl.it

On the right side of the screen, go to shell and type

```bash
python main.py
```

Ensure that in `app.run()`, host is `0.0.0.0` and port is `5000`.

A web browswer should appear, containing the page corresponding to the `/` route.

## Running Locally

Execute `python main.py` (Windows) or `python3 main.py` (MacOS/Linux)

Open a browser (such as Google Chrome) at the address `http://localhost:5000`.

## Using Various Pizza Parameters

Enter the URL with the following parameters:

```http://localhost:5000/identify/{cheese strips}/{pepperoni slices}/{pineapple chunks}```

Where cheese strips, pepperoni slices and pineapple chunks are all integers.

When you submit this URL, it invokes the `identify()` function which returns a Python dictionary 
with two keys: the estimated time to eat a pizza with those parameters, and 
the type of pizza that was created.

---
Workshop date: January 9, 2021
