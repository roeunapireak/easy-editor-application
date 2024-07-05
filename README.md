# easy-editor-application

### Task 1. Create an interface for the application.

<img src="interface-guideline.png" width="700"/>

1) Import the necessary modules from the PyQt5 library.
2) Create an application object (and application window).
3) Create widgets: 
— A folder button,
— A list with items selected, 
— An image label,
— A set of buttons for editing photos: “Left,” “Right,” “Mirror,” “Sharpness,” “B/W.”
4) Place the buttons on the layouts.
5) Run the software and adjust the interface, if necessary.

### Task 2. Program the display of a set of images (from a random folder) in the widget

1) Import the os module.

2) Program the processing of pressing the Folder button.

2.1. Create the chooseWorkdir() function to select the work folder. Use the following command: QFileDialog.getExistingDirectory(). The work folder is defined as a global variable.

2.2. Create the filter() function to select files of suitable formats from the list. Use the filename.endswith(extension) command in order to find out whether the filename field ends with the extension line.

2.3. Create the handler function for the Folder button click. The function will allow you to select the folder (referring to chooseWorkdir()) and files with graphic extensions (referring to filter()), as well as to display the list of graphic file names in the list widget.

3) Enable event handling. Run the software and make sure that the widget is filled with the names of graphic files.