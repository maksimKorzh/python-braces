# Python Braces
Write python code with curly braces instead of indents

# What is this
It's a simple python script that takes code like this as an input

```python
if True {
  print('hello');print('more')
} else { 
  print('else')
   print('end')
}
```

and generates a valid python code as an output:

```python
if True:
    print('hello')
    print('more')
else:
    print('else')
    print('end')
```

# Limitations
';' is replaced with a new line, so it overrides the default python
interpretation of ';', make sure to avoid using spaces after ';' for
otherwise indents would be broken

# How to use it
    python3 pb.py input.pb output.py
