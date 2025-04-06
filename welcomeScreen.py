from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl

class WelcomeScreen(QMainWindow):
    def __init__(self, on_finished_callback):
        super().__init__()
        self.setWindowTitle("Soup Is Getting Cooked")

        self.resize(480, 480)

        # Create a central widget
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # Set the background color of the central widget
        centralWidget.setStyleSheet("background-color: #F4EDD8;")

        # Create a layout
        layout = QVBoxLayout(centralWidget)

        # Create a video widget
        self.videoWidget = QVideoWidget(self)
        layout.addWidget(self.videoWidget)

        # Create a media player
        self.mediaPlayer = QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        # Set the video source
        self.mediaPlayer.setSource(QUrl.fromLocalFile("Multimedia/soup_loading.mp4")) 

        # Connect the media player's finished signal to the callback
        self.mediaPlayer.mediaStatusChanged.connect(self.check_video_status)
        self.on_finished_callback = on_finished_callback

        # Play the video
        self.mediaPlayer.play()

    def check_video_status(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.mediaPlayer.stop()
            self.close()
            self.on_finished_callback()