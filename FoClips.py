import nltk
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtTextToSpeech import QTextToSpeech
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtTextToSpeech import QTextToSpeech
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtMultimediaWidgets import QVideoWidget
import FoClipsLogo_rc
import random


'''
Main GUI Class.
Contains QtWidgets including buttons, text editors, labels, etc.
Links widgets to default or defined slots.
Handles Media Player via QMultimedia.
Handles TTS via QTextToSpeech
Handles captions syncronized with TTS.

Notes: 
- Captions could possibly not fit, need to segment by character count to avoid
- Video needs loop functionality
- Needs moving window functionality
- Add option to disable AI version
- Add volume controls
- Add gui menu

'''

class Ui_MainWindow(object):
	'''
	Creates and sets attributes for all widgets

	'''
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(880, 600)
		#MainWindow.setWindowFlags(Qt.FramelessWindowHint)
		#MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		# Central widget is above all widgets in heirarchy, keep as MainWindow
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		# Set layout for the background
		self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
		self.drop_shadow_layout.setSpacing(0)
		self.drop_shadow_layout.setObjectName("drop_shadow_layout")

		# Set frame for the background
		self.background_frame = QtWidgets.QFrame(self.centralwidget)
		self.background_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(18, 72, 102, 255), stop:1 rgba(70, 0, 106, 255));border-radius: 10px")
		self.background_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.background_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.background_frame.setObjectName("background_frame")

		# Set vertical layout for background frame
		self.verticalLayout = QtWidgets.QVBoxLayout(self.background_frame)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")

		# Set frame for header
		self.header_frame = QtWidgets.QFrame(self.background_frame)
		self.header_frame.setMaximumSize(QtCore.QSize(16777215, 40))
		self.header_frame.setStyleSheet("background-color: rgba(55, 42, 121, 30);")
		self.header_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.header_frame.setObjectName("header_frame")

		# Set horizontal layout for header frame
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")

		# Set title frame
		self.title_frame = QtWidgets.QFrame(self.header_frame)
		font = QtGui.QFont()
		font.setFamily("Eras Medium ITC")
		font.setPointSize(14)
		self.title_frame.setFont(font)
		self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.title_frame.setObjectName("title_frame")

		# Set title label for FoClips Logo
		self.title_label = QtWidgets.QLabel(self.title_frame)
		self.title_label.setGeometry(QtCore.QRect(10, 10, 71, 21))
		font = QtGui.QFont()
		font.setFamily("Leelawadee UI")
		font.setPointSize(9)
		font.setBold(True)
		font.setItalic(False)
		font.setUnderline(False)
		font.setWeight(75)
		self.title_label.setFont(font)
		self.title_label.setAutoFillBackground(False)

		# Set FoClips Logo image
		self.title_label.setStyleSheet("image: url(:/FoClipsLogo/FoClipsLogo.png);border-radius: 5")
		self.title_label.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.title_label.setFrameShadow(QtWidgets.QFrame.Plain)
		self.title_label.setText("")
		self.title_label.setScaledContents(False)
		self.title_label.setObjectName("title_label")

		# Set horizontal layout for title frame
		self.horizontalLayout.addWidget(self.title_frame)

		# Set frame for header buttons
		self.header_buttons_frame = QtWidgets.QFrame(self.header_frame)
		self.header_buttons_frame.setMaximumSize(QtCore.QSize(100, 16777215))
		self.header_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.header_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.header_buttons_frame.setObjectName("header_buttons_frame")

		# Set horizontal layout for header button frame
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_buttons_frame)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")

		# Set maximize button
		self.maximize_button = QtWidgets.QPushButton(self.header_buttons_frame)
		self.maximize_button.setMinimumSize(QtCore.QSize(16, 16))
		self.maximize_button.setMaximumSize(QtCore.QSize(17, 17))
		self.maximize_button.setStyleSheet(
			"QPushButton {"
			"    border: none;\n"
			"    border-radius: 8px;\n"
			"    background-color: rgb(0, 255, 0);\n"
			"}\n"
			"QPushButton:hover {\n"
			"    background-color: rgba(0, 255, 0, 150);\n"
			"}"
			)
		self.maximize_button.setText("")
		self.maximize_button.setObjectName("maximize_button")
		self.horizontalLayout_2.addWidget(self.maximize_button)

		# Set minimize button
		self.minimize_button = QtWidgets.QPushButton(self.header_buttons_frame)
		self.minimize_button.setMinimumSize(QtCore.QSize(16, 16))
		self.minimize_button.setMaximumSize(QtCore.QSize(17, 17))
		self.minimize_button.setStyleSheet(
			"QPushButton {\n"
			"    border: none;\n"
			"    border-radius: 8px;\n"
			"    background-color: rgb(255, 170, 0);\n"
			"}\n"
			"QPushButton:hover {\n"
			"    background-color: rgba(255, 170, 0, 150);\n"
			"}"
			)
		self.minimize_button.setText("")
		self.minimize_button.setObjectName("minimize_button")
		self.horizontalLayout_2.addWidget(self.minimize_button)

		# Set close button
		self.close_button = QtWidgets.QPushButton(self.header_buttons_frame)
		self.close_button.setMinimumSize(QtCore.QSize(16, 16))
		self.close_button.setMaximumSize(QtCore.QSize(17, 17))
		self.close_button.setStyleSheet(
			"QPushButton {\n"
			"    border: none;\n"
			"    border-radius: 8px;\n"
			"    background-color: rgb(255, 0, 0);\n"
			"}\n"
			"QPushButton:hover {\n"
			"    background-color: rgba(255, 0, 0, 150);\n"
			"}"
			)
		self.close_button.setText("")
		self.close_button.setObjectName("close_button")
		self.horizontalLayout_2.addWidget(self.close_button)
		self.horizontalLayout.addWidget(self.header_buttons_frame)
		self.verticalLayout.addWidget(self.header_frame)

		# Set frame for middle content
		self.content_frame = QtWidgets.QFrame(self.background_frame)
		self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.content_frame.setObjectName("content_frame")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.content_frame)
		self.verticalLayout_3.setObjectName("verticalLayout_3")

		# Set stacked widget inside content frame
		self.stackedWidget = QtWidgets.QStackedWidget(self.content_frame)
		self.stackedWidget.setObjectName("stackedWidget")

		# Main page with text input
		self.main_page = QtWidgets.QWidget()
		self.main_page.setObjectName("main_page")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main_page)
		self.verticalLayout_4.setObjectName("verticalLayout_4")

		# Text input widget
		self.text_input = QtWidgets.QTextEdit(self.main_page)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.text_input.sizePolicy().hasHeightForWidth())
		self.text_input.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Segoe MDL2 Assets")
		font.setPointSize(10)
		self.text_input.setFont(font)
		self.text_input.setAutoFillBackground(False)
		self.text_input.setStyleSheet("background-color: rgba(0, 0, 0, 50);color: rgba(255, 255, 255, 200);")
		self.text_input.setObjectName("text_input")
		self.verticalLayout_4.addWidget(self.text_input)

		# Submit button
		self.submit_button = QtWidgets.QPushButton(self.main_page)
		font = QtGui.QFont()
		font.setFamily("Segoe MDL2 Assets")
		font.setPointSize(16)
		font.setBold(True)
		font.setWeight(75)
		self.submit_button.setFont(font)
		self.submit_button.setStyleSheet(
			"QPushButton {\n"
			"    border: none;\n"
			"    border-radius: 8px;\n"
			"    color: rgba(255, 255, 255, 200);\n"
			"    background-color: rgba(0, 169, 253, 150);\n"
			"}\n"
			"QPushButton:hover {\n"
			"    background-color: rgba(0, 169, 253, 100);\n"
			"}")
		self.submit_button.setObjectName("submit_button")
		self.verticalLayout_4.addWidget(self.submit_button)
		self.stackedWidget.addWidget(self.main_page)

		# Video page with video output and TTS and captions
		self.video_page = QtWidgets.QWidget()
		self.video_page.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
		self.video_page.setObjectName("video_page")
		self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.video_page)
		self.verticalLayout_5.setObjectName("verticalLayout_5")

		# Captions label widget
		self.captions_label = QtWidgets.QLabel(self.video_page)
		self.captions_label.setMaximumSize(QtCore.QSize(16777215, 60))
		font = QtGui.QFont()
		font.setFamily("Segoe MDL2 Assets")
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		font.setStrikeOut(False)
		font.setKerning(True)
		self.captions_label.setFont(font)
		self.captions_label.setAutoFillBackground(False)
		self.captions_label.setStyleSheet("color: rgba(255, 255, 255, 200);background-color: rgba(0, 0, 0, 100);border-radius: 10px;")
		self.captions_label.setAlignment(QtCore.Qt.AlignCenter)
		self.captions_label.setWordWrap(True)
		self.captions_label.setObjectName("captions_label")
		self.verticalLayout_5.addWidget(self.captions_label)

		# Video Widget, child of QMultiMedia 
		self.video_widget = QVideoWidget(self.video_page)
		self.video_widget.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
		self.video_widget.setObjectName("video_widget")
		self.verticalLayout_5.addWidget(self.video_widget)
		self.stackedWidget.addWidget(self.video_page)
		self.verticalLayout_3.addWidget(self.stackedWidget)
		self.verticalLayout.addWidget(self.content_frame)

		# Frame for footer/credits
		self.footer_frame = QtWidgets.QFrame(self.background_frame)
		self.footer_frame.setMaximumSize(QtCore.QSize(16777215, 30))
		self.footer_frame.setStyleSheet("background-color:none;")
		self.footer_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.footer_frame.setObjectName("footer_frame")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.footer_frame)
		self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_3.setSpacing(0)
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")

		# Frame for credits
		self.credits_frame = QtWidgets.QFrame(self.footer_frame)
		font = QtGui.QFont()
		font.setFamily("Arial")
		self.credits_frame.setFont(font)
		self.credits_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.credits_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.credits_frame.setObjectName("credits_frame")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.credits_frame)
		self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
		self.verticalLayout_2.setSpacing(0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")

		# Credits label
		self.credits_label = QtWidgets.QLabel(self.credits_frame)
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(8)
		self.credits_label.setFont(font)
		self.credits_label.setStyleSheet("color: rgba(255, 255, 255, 150);")
		self.credits_label.setObjectName("credits_label")
		self.verticalLayout_2.addWidget(self.credits_label)
		self.horizontalLayout_3.addWidget(self.credits_frame)

		# Grip frame to hold frame size
		self.frame_grip = QtWidgets.QFrame(self.footer_frame)
		self.frame_grip.setMinimumSize(QtCore.QSize(30, 30))
		self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
		self.frame_grip.setStyleSheet("padding: 5px;")
		self.frame_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_grip.setObjectName("frame_grip")
		self.horizontalLayout_3.addWidget(self.frame_grip)
		self.verticalLayout.addWidget(self.footer_frame)

		self.drop_shadow_layout.addWidget(self.background_frame)
		MainWindow.setCentralWidget(self.centralwidget)

		# Call function to reassign text to widgets
		self.retranslateUi(MainWindow)

		# Set page to text input page
		self.stackedWidget.setCurrentIndex(0)

		# Connect widgets to default slots
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		# Adding MediaPlayer for video playback
		self.mediaPlayer = QMediaPlayer()
		self.mediaPlayer.setVideoOutput(self.video_widget)
		videos = ["vid1.mp4", "vid2.mp4", "vid3.mp4", "vid4.mp4", "vid5.mp4", "vid6.mp4", "vid7.mp4"]
		self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(random.choice(videos)))) # Change video path
		self.mediaPlayer.setVolume(1)
	
		# Connect buttons to slot functions
		self.submit_button.clicked.connect(self.on_submit_button_clicked)
		self.maximize_button.clicked.connect(on_maximize_button_clicked)
		self.close_button.clicked.connect(on_close_button_clicked)
		self.minimize_button.clicked.connect(on_minimize_button_clicked)

		# TTS Engine
		self.ttsengine = None

		# Searches for available TTS engines
		engineNames = QTextToSpeech.availableEngines()
		if len(engineNames) > 0:
			engineName = engineNames[0]
			self.ttsengine = QTextToSpeech(engineName)
			self.voices = []
			for voice in self.ttsengine.availableVoices():
				self.voices.append(voice)
		else:
			print("TTS Engine unavailable")

		# Connect TTS engine to slot function on state change
		self.ttsengine.stateChanged.connect(self.tts_on_state_changed)
		
	'''
	Controls what happens when a state change occurs on the TTS engine.
	Recursively steps through each segment of text for the TTS to read,
	while simultainiously updating caption label.
	
	'''
	def tts_on_state_changed(self, state):
		if state == QTextToSpeech.Ready:
			if self.current_sentence < len(self.sentences):
				self.captions_label.setText(self.sentences[self.current_sentence])
				self.ttsengine.say(self.sentences[self.current_sentence])
				self.current_sentence += 1    

	'''
	Initiates TTS engine, controls volume and rate of speech

	'''
	def say_text(self):
		self.sentences = nltk.sent_tokenize(self.text) ###
		if self.sentences:	
			self.current_sentence = 0
			self.ttsengine.setVolume(0.1)
			self.ttsengine.setRate(0.2)
			self.captions_label.setText(self.sentences[self.current_sentence])
			self.ttsengine.say(self.sentences[self.current_sentence])
			self.current_sentence += 1
	
	'''
	Controls submit button clicked event
	Plays media player video and calls TTS engine

	'''
	def on_submit_button_clicked(self):
		self.togglegpt = True # Placeholder to toggle on/off AI functionality
		self.captions_label.raise_()
		self.text = self.text_input.toPlainText()
		if self.togglegpt: self.request_gpt()
		self.stackedWidget.setCurrentIndex(1)
		self.mediaPlayer.play()
		self.say_text()

	'''
	Makes a request to the gpt-3 AI for a "redditized" response text
	
	'''
	def request_gpt(self):
		import gptRequest as gpt
		response = gpt.get_gpt_response(
			gpt.PROMPT_OPENER + self.text_input.toPlainText()
		)
		username = response[response.find("USERNAME:")+9:response.find("QUESTION:")].strip()
		question = response[response.find("QUESTION:")+9:response.find("REPLY:")].strip()
		reply = response[response.find("REPLY:")+6:].strip()

		self.text = "From User " + username + ", in r/AskReddit: " + question + " " + reply

	'''
	Sets text of various widgets

	'''
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.submit_button.setText(_translate("MainWindow", "Submit Text"))
		self.captions_label.setText(_translate("MainWindow", "Please submit text to start FoClipping!"))
		self.credits_label.setText(_translate("MainWindow", "By Kevin Wagner"))

# Max, min, and close button functions
def on_maximize_button_clicked(): MainWindow.showMaximized()
def on_minimize_button_clicked(): MainWindow.showMinimized()
def on_close_button_clicked(): MainWindow.close()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
