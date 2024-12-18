# Spectoconvo

Spectoconvo is a Python package to embed messages into spectrograms.

## Installation

You can install the package using pip:

```sh
pip install spectoconvo
```

## Usage

Here's an example of how to encode a message using `spectoconvo` package:

```python
from spectoconvo import add_message_to_spectrogram

sound_file = 'audio.wav'

message = 'Hello, Spectrogram!'

output_file = 'output_spectrogram.png'

output_sound_file = 'output_with_message.wav'

output_spectrogram_file = 'output_with_message_spectrogram.png'

changes_spectrogram_file = 'changes_spectrogram.png'

image_path = 'output_image.png'

scale_freq,scale_time=add_message_to_spectrogram(sound_file, message, output_file, output_sound_file, output_spectrogram_file, changes_spectrogram_file, image_path,scale_freq,scale_time)
```
Edit scale_freq and scale_time to scale the message in the spectrum after running the drfult setting, the defult is to the largest message possibe with the  at 20 kHz.

Here's an example of how to decode a message using `spectoconvo` package:
```python
from spectoconvo import add_message_to_spectrogram


sound_file_to_decode = 'output_with_message.wav'


image_path = 'output_image_decode.png'

decode( sound_file_to_decode, image_path)

```