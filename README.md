# Spectoconvo

Spectoconvo is a Python package to embed messages into spectrograms.

## Installation

You can install the package using pip:

```sh
pip install spectoconvo
from spectoconvo import add_message_to_spectrogram

sound_file = 'audio.wav'
message = 'Hello, Spectrogram!'
output_file = 'output_spectrogram.png'
output_sound_file = 'output_with_message.wav'
output_spectrogram_file = 'output_with_message_spectrogram.png'
changes_spectrogram_file = 'changes_spectrogram.png'
image_path = 'output_image.png'

add_message_to_spectrogram(sound_file, message, output_file, output_sound_file, output_spectrogram_file, changes_spectrogram_file, image_path)
```