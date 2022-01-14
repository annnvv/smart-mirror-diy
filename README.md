# Smart Mirror DIY

**Status**: IN PROGRESS

**Purpose**: The purpose of this repo is to house the code to generate an interface for a smart mirror.

The smart mirror will display:
- [DONE] Greeting
- Day of Week, Date
- Time of day
- [IN PROGRESS] Weather information (temperature and current weather icon)
- [IN PROGRESS] WMATA next train information
- [ON HOLD] DASH bus information


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
- Decoupling the classes from the GUI (at least attempting to do this)
- Calling REST APIs using requests


**Inspiration**: This project is inspired by a DIY smart mirror [Youtube video](https://www.youtube.com/watch?v=fkVBAcvbrjU&list=WL&index=10&t=2s) and its corresponding [repo](https://github.com/HackerShackOfficial/Smart-Mirror).
