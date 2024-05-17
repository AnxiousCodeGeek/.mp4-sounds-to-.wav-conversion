from moviepy.editor import AudioFileClip
import os

def convert_mp4_audio_to_wav(input_file, output_file):
    # Load the audio clip
    audio_clip = AudioFileClip(input_file)
    
    # Write the audio clip to a WAV file
    audio_clip.write_audiofile(output_file)
    
    # Close the audio clip
    audio_clip.close()

# File paths
input_file = "input/WhatsApp Audio 2024-05-15 at 11.38.07 AM.mp4"
output_file = "input/heartbeat_audio.wav"

# Convert .mp4 to .wav
convert_mp4_audio_to_wav(input_file, output_file)

print("Conversion complete!")