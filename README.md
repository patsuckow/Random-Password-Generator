# Random-Password-Generator

The easiest and most reliable password generator in Python3.

![GNU GPL v 3 0](https://user-images.githubusercontent.com/12321741/67310082-c4636280-f505-11e9-83a7-d23e8037c54f.png)

Versions
--------
Random-Password-Generator works with ![version](https://user-images.githubusercontent.com/12321741/67310245-0ab8c180-f506-11e9-993e-5ad8c39feea3.png)

Installation
------------
```
$ wget -O pass_gen.py https://raw.githubusercontent.com/patsuckow/Random-Password-Generator/master/rpg.py
```

Usage
-----
```
$ python3 pass_gen.py
```
**output example:** 

DPuZ33JKQWwfJQvvRJBVl

7dnGagtpEPOjfzaRGo7wR

viRLPpTdCrV9obm4PpO27

or

```
$ python3 pass_gen.py --len=11
```
**output example:**

RgF8nTEmWwd

rUM2659g6HM

4DNfosfCB2O
    
All you need to do is just determine how long the password is to generate. By default, a string of 21 characters will be displayed.

You can change the number of generated strings using the --str parameter. For example, let it generate 5 password strings:

```
$ python3 rpg.py --str=5
```
**output example:**

qJ5tRpQdsgPyotRHt1m7L

rPnUMlEglAXYnu9ka6wlK

mORJ09Ttk5dD5nS477mld

8ptymHyTSi9n0cVLVKXhX

nsqO74kZ4e2tHrjnHedj3

Symbols to be used to create a password and how to get them (speed tests 🚀): ![see](speed_tests.md)
