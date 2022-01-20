# Smart Mirror DIY

**Status**: IN PROGRESS

**Purpose**: The purpose of this repo is to house the code to generate an interface for a smart mirror.

The smart mirror will display:
- [DONE] Greeting
- Day of Week, Date
- Time of day
- [IN PROGRESS] Weather information
  - Temperature, feels like, high, low, and current weather icon
- [IN PROGRESS] WMATA next train information
- [ON HOLD] DASH next bus information


**Lessons Learned**:
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


**Inspiration**: This project is inspired by a DIY smart mirror [Youtube video](https://www.youtube.com/watch?v=fkVBAcvbrjU&list=WL&index=10&t=2s) and its corresponding [repo](https://github.com/HackerShackOfficial/Smart-Mirror).


**Resources**:
There are some of the resources that I have found helpful in working on this project (not an exhaustive list).
1. (Python Class vs. Static vs. Instance Methods)[https://pynative.com/python-class-method-vs-static-method-vs-instance-method/]
2. (tkinter TreeView)[https://www.pythontutorial.net/tkinter/tkinter-treeview/]
3. (tkinter after method)[https://stackoverflow.com/questions/44085554/how-to-use-the-after-method-to-make-a-callback-run-periodically] practical example at the end !
