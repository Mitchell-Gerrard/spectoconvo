from spectoconvo.spectoconvo import add_message_to_spectrogram

sound_file = 'audio.wav'

message = 'Hello, Human!'

output_file = 'output_spectrogram.png'

output_sound_file = 'output_with_message.wav'

output_spectrogram_file = 'output_with_message_spectrogram.png'

changes_spectrogram_file = 'changes_spectrogram.png'

image_path = 'output_image.png'

add_message_to_spectrogram(sound_file, message, output_file, output_sound_file, output_spectrogram_file, changes_spectrogram_file, image_path)
from spectoconvo.spectoconvo import decode


sound_file_to_decode = 'output_with_message.wav'


image_path = 'output_image_decode.png'

decode( sound_file_to_decode, image_path)