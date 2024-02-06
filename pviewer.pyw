import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QSizePolicy
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt


class PhotoViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.image_paths = []
        self.current_index = -1
        self.initUI()

    def initUI(self):
        self.setWindowTitle('pviewer')
        self.setMinimumSize(400, 300)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image_label.setScaledContents(True)

        self.open_button = QPushButton('Open Image', self)
        self.open_button.clicked.connect(self.openImage)

        self.prev_button = QPushButton('Previous', self)
        self.prev_button.clicked.connect(self.showPrevious)

        self.next_button = QPushButton('Next', self)
        self.next_button.clicked.connect(self.showNext)

        self.rotate_clockwise_button = QPushButton('Rotate Clockwise', self)
        self.rotate_clockwise_button.clicked.connect(self.rotateClockwise)

        self.rotate_counterclockwise_button = QPushButton('Rotate Counterclockwise', self)
        self.rotate_counterclockwise_button.clicked.connect(self.rotateCounterclockwise)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.open_button)
        self.layout.addWidget(self.prev_button)
        self.layout.addWidget(self.next_button)
        self.layout.addWidget(self.rotate_clockwise_button)
        self.layout.addWidget(self.rotate_counterclockwise_button)

    def openImage(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Open Folder', '.')
        if folder_path:
            self.image_paths = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path)
                                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
            if self.image_paths:
                self.current_index = 0
                self.showImage()

    def showImage(self):
        if self.current_index >= 0 and self.current_index < len(self.image_paths):
            pixmap = QPixmap(self.image_paths[self.current_index])
            self.image_label.setPixmap(pixmap)
            self.image_label.adjustSize()

    def showPrevious(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.showImage()

    def showNext(self):
        if self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            self.showImage()

    def rotateClockwise(self):
        if self.current_index >= 0 and self.current_index < len(self.image_paths):
            pixmap = self.image_label.pixmap()
            pixmap = pixmap.transformed(QTransform().rotate(90))
            self.image_label.setPixmap(pixmap)

    def rotateCounterclockwise(self):
        if self.current_index >= 0 and self.current_index < len(self.image_paths):
            pixmap = self.image_label.pixmap()
            pixmap = pixmap.transformed(QTransform().rotate(-90))
            self.image_label.setPixmap(pixmap)


def main():
    app = QApplication(sys.argv)
    viewer = PhotoViewer()
    viewer.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
