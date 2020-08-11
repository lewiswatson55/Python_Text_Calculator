# For clearing the screen and press any key to continue.md
**Note. This file was directly imported from an answer I put on SO. The question was later deleted by the Community bot.**

As @esqew and @CoryKramer said, it is only an issue if it responds to user input. Thanks the both of you :)

@ErdoğanOnal suggested some very useful code, thanks so much :)

His code:
```
import sys 
try:
     import msvcrt
     _IS_WINDOWS = True
except ImportError:
     import tty
     import termios
     _IS_WINDOWS = False
print(_("Press any key to continue..."), end='', flush=True)
if _IS_WINDOWS:
     msvcrt.getch()
else:
     fd = sys.stdin.fileno()
     settings = termios.tcgetattr(fd)
     try:
         tty.setraw(sys.stdin.fileno())
         sys.stdin.read(1)
     finally:
         termios.tcsetattr(fd, termios.TCSADRAIN, settings)
```

And I found [this guide](https://www.geeksforgeeks.org/clear-screen-python/) and used it to use ANSI escape sequences:

```
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
```

Thank you everyone! :)
