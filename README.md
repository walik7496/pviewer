# Photo Viewer

This is a simple image viewer built using the `PyQt5` framework in Python. The application allows users to view, navigate through, and rotate images in a selected folder.

## Features
- **Open Folder**: Load images from a folder on your computer.
- **Next/Previous Image**: Navigate through images using "Next" and "Previous" buttons.
- **Image Rotation**: Rotate images clockwise and counterclockwise.
- **Responsive Layout**: The images are displayed at an appropriate scale while maintaining their aspect ratio.

## Requirements
- Python 3.x
- PyQt5

You can install PyQt5 using pip:

```bash
pip install PyQt5
```

## How to Run

1. Copy the provided Python code into a file, for example, photo_viewer.py.
2. Install PyQt5 using pip (if not already installed).
3. Open the terminal/command prompt and navigate to the directory where the Python file is located.
4. Run the script:

```bash
python photo_viewer.py
```

## Application Controls

- Open Image: Opens a dialog to select a folder containing images.
- Previous: Display the previous image in the folder.
- Next: Display the next image in the folder.
- Rotate Clockwise: Rotate the current image 90 degrees clockwise.
- Rotate Counterclockwise: Rotate the current image 90 degrees counterclockwise.

## How It Works

- The app allows users to open a folder and view all images (.png, .jpg, .jpeg, .bmp) inside it.
- The image is displayed in the center of the window, and you can navigate between images by using the "Next" and "Previous" buttons.
- You can also rotate the image using the rotate buttons.

## License

This project is open-source and free to use. Enjoy!
