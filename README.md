# BaixeTube

BaixeTube is a simple script for downloading audio and videos from YouTube. You can download a single video or an entire playlist.


## Environment Setup

Before you begin, download the **FFmpeg** program to convert mp4 files into mp3.


### Download FFmpeg

- FFmpeg windows: [FFmpeg-master-latest-win64-gpl-shared](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/FFmpeg-master-latest-win64-gpl-shared.zip)
- FFmpeg linux: [FFmpeg-master-latest-linux64-gpl-shared](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/FFmpeg-master-latest-linux64-gpl-shared.tar.xz)
- Github with all builds: [FFmpeg builds (BtbN)](https://github.com/BtbN/FFmpeg-Builds/releases)

### Prerequisites

Ensure you have Python installed on your system. You'll need pip to install the dependencies.

Tested libraries and versions:
- pydub 0.25.1 
- mutagen 1.47.0 
- pytube  15.0.0


### Setting Up

1. **Clone the Repository**

   Use he following command to clone the project repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-project.git
   ```

2. **Install the Dependeces**
   
   I recommend creating a virtual environment to install the dependencies’ versions:

   ```
   pip install -r requirements.txt
   ```
   
## Usage

1. **Run the ```main.py``` File:**

   - Navigate to the project directory.
   - Execute the ```main.py``` file.

2. **Provide the FFmpeg Path:**

   The program may prompt you to provide the path where the FFmpeg folder is located (usually in a "bin" folder)

3. **Start Downloading:**
   - Once everything is set up, the program will start properly.
   - you'll need the link to the video or playlist
   - if there's a playlist or a video within a playlist, the program will ask if you want to download the entire playlist or just the video.
   - additionally, it will inquire whether you want to download only the audio or the complete video.

# License

