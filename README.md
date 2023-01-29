## Inspiration
If you've ever used **TikTok**, I'm certain that you've spent a good amount of time watching videos with Reddit stories read out loud over video game clips, such as minecraft parkour or subway surfers. Although it seems counterintuitive, having multiple things to focus on actually **helped me and many others listen to the stories.** This gave me the grand idea to find a way to bring that experience to studying. Rather than forcing myself to sit for an hour reading a dull 10 year old textbook on statistics, I'd love to take in _the same information in a more fun way_. So, I created **FoClips, an app that takes any text and converts it into an exciting and informative text to speech over gameplay, just like on TikTok!**

## What it does
FoClips has a simple modern GUI, where the user can paste any kind of text into the textbox as input. FoClips will then use AI to generate a new text, in the format of an "AskReddit" post, that imitates a question and reply going over the concepts of the original text. Then, the new text is spoken out loud through TTS with live captions, and at the same time, there is a gameplay video that plays in the background to keep you stimulated

## How we built it
I built FoClips primarily using PyQt5, which is GUI module that integrates many of Qt's C++ Toolkits into Python. I used Qt Designer to design the GUI. I also used a package integrating Selenium and Requests to imitate the OpenAI API, avoiding token costs and other procedures.

##Usage
`pip3 install -r requirements.txt`

To use the OpenAI API, you will need to provide your browser session token in the config.json file. I have provided one temporarily. This means that there might be too many requests and the AI portion of FoClips won't work, so if that is the case, insert your token into the config.json. 
You can find the session token manually from your browser:
Go to https://chat.openai.com/api/auth/session
Press F12 to open console
Go to Application > Cookies
Copy the session token value in __Secure-next-auth.session-token
Paste it into config.json in the current working directory

After that, FoClips is ready to be ran either through an IDE or with 'python FoClips.py'

## Challenges we ran into
Media playing was definitely a challenge I faced while using PyQt. There were often some modules that  I was not able to use because they were either outdated or replaced. Eventually I settled on an older version of PyQt5 to solve my issue. Another issue was the time constraint. Working with PyQt is brand new to me, so I needed time to read the documentation and learn how the toolkit worked. It may have taken an all-nighter, but I'm happy to say that I learned some new skills throughout the process.

## Accomplishments that we're proud of
I'm proud to learn about PyQt, I feel that I will be using the toolkit in many of my own projects in the future. I'm also very happy to have finished my submission for Swamphacks.

## What's next for FoClips
I have a list of features I have plans to work on, including:
- Custom video selection.
- UX Controls.
- Different video formatting.
- Saving user data
