# MP4 Audio to WAV Audio Conversion
The code helps convert audio sounds in .mp4 format to .wav format. I know .mp4 format audio, sounds hard to believe but i encountered a case in my project and was able to code for the conversion.

## Introduction
Converting audio files from one format to another can be useful in various applications, such as audio processing, analysis, or simply to make the files compatible with specific software. This project uses ```moviepy```, a powerful library for video editing in Python, to extract audio from an ```.mp4``` sound file and save it as a ```.wav``` file.

## Installation
Install the library first:
```bash
pip install moviepy
```
## Working
 - To use the script, you need to provide the input MP4 file path and the desired output WAV file path. The script will convert the audio and save it to the specified output location.
 - ```AudioFileClip``` from ```moviepy.editor``` is used to load and manipulate audio files.
```python
from moviepy.editor import AudioFileClip
audio_clip = AudioFileClip(input_file)
```

 - The function ```convert_mp4_audio_to_wav()``` is called with the specified input and output file paths.
```python
# Convert .mp4 to .wav
convert_mp4_audio_to_wav(input_file, output_file)
```

 1. Edit the file paths in the script to match your input and output file locations.
 2. Run the script using Python.

After running the script, you should see the message **"Conversion complete!"** and the WAV file should be available at the specified output location.
