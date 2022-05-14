# Smart Mirror DIY

**Status**: In Progress

**Inspiration**: This project is inspired by a DIY smart mirror [Youtube video](https://www.youtube.com/watch?v=fkVBAcvbrjU&list=WL&index=10&t=2s) and its corresponding [repo](https://github.com/HackerShackOfficial/Smart-Mirror).

**Purpose**: The purpose of this repo is to house the code to generate an interface for a smart mirror.

The smart mirror will display:
- [Done] Greeting
- [In Progress] Day of Week, Date
- [In Progress] Time of day
- [In Progress] Weather information
  - Temperature, feels like, high, low, and current weather icon
- [In Progress] WMATA next train information
- [On Hold] DASH next bus information

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

## Resources:
There are some of the resources that I have found helpful in working on this project (not an exhaustive list).
1. [Python Class vs. Static vs. Instance Methods](https://pynative.com/python-class-method-vs-static-method-vs-instance-method/)
2. [tkinter TreeView](https://www.pythontutorial.net/tkinter/tkinter-treeview/)
3. [tkinter after method](https://stackoverflow.com/questions/44085554/how-to-use-the-after-method-to-make-a-callback-run-periodically) practical example at the end !
