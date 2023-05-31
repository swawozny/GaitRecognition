import os
import sys
import pathlib
import cv2
from src.gui.VideoWindow import VideoWindow
from PyQt5.QtWidgets import QApplication

result_path = "/home/fksiezyc/Pobrane/testmp4/"
#result_path = str(pathlib.Path(__file__).parent.resolve()) + '/results'

app = QApplication(sys.argv)
player = VideoWindow(result_path)
player.showMaximized()
sys.exit(app.exec_())
