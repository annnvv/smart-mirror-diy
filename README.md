# Smart Mirror DIY

**Status**: In Progress

**Inspiration**: This project is inspired by a DIY smart mirror [Youtube video](https://www.youtube.com/watch?v=fkVBAcvbrjU&list=WL&index=10&t=2s) and its corresponding [repo](https://github.com/HackerShackOfficial/Smart-Mirror).

**Purpose**: The purpose of this repo is to house the code to generate an interface for a smart mirror.

The smart mirror will display:
- [DONE] Greeting
- [DONE] Day of Week, Date
- [DONE] Time of day
- [IN PROGRESS] Weather information
  - Temperature, feels like, high, low, and current weather icon
- [IN PROGRESS] WMATA next train information
- [ON HOLD] DASH next bus information

**Data Sources**:
- Weather: [Open Weather Map Api](https://openweathermap.org/api)
- Metro: [WMATA API](https://developer.wmata.com/)

## Lessons Learned:
- Creating a GUI using tkinter
  - Using Frames to create a grid, using pack within Frames
  - .grid() versus .pack() methods
  - Displaying images
  - Using TreeView to display data tabularly (in progress)
  - .after method (in progress)
- Python Object Orientation
  - instance versus class methods
  - inheritance of classes
- Decoupling the classes from the GUI (at least attempting to do this, surprisingly challenging)
- Calling REST APIs using requests

**Resources**:
[Event Driven Programming in Python](https://odsc.medium.com/decoupling-complex-systems-with-event-driven-python-programming-d67092d45939)
There are some of the resources that I have found helpful in working on this project (not an exhaustive list).
1. [Python Class vs. Static vs. Instance Methods](https://pynative.com/python-class-method-vs-static-method-vs-instance-method/)
2. [tkinter TreeView](https://www.pythontutorial.net/tkinter/tkinter-treeview/)
3. [tkinter after()](https://stackoverflow.com/questions/44085554/how-to-use-the-after-method-to-make-a-callback-run-periodically) practical example at the end !
4. [last answer on SO: StringVar(), .set(), and after()](https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop)
https://maldus512.medium.com/how-to-setup-correctly-an-application-with-python-and-tkinter-107c6bc5a45 !!!!
https://docs.python.org/3/library/tkinter.html#coupling-widget-variables
https://stackoverflow.com/questions/9342757/tkinter-executing-functions-over-time
https://stackoverflow.com/questions/25753632/tkinter-how-to-use-after-method
https://pythonbasics.org/tkinter-label/
https://www.journaldev.com/48165/tkinter-working-with-classes
https://forums.raspberrypi.com/viewtopic.php?t=137597
https://blog.teclado.com/write-snake-game-python-tkinter-part-2/
https://subscription.packtpub.com/book/application-development/9781788627481/1/ch01lvl1sec14/using-variables
https://linuxconfig.org/how-to-build-a-tkinter-application-using-an-object-oriented-approach
