from spectoconvo import add_message_to_spectrogram

sound_file = 'uplift.mp3'

message = '我去见阿纳敌人!'

inital_spectrum_image = 'output_spectrogram.png'

output_sound_file = 'output_with_message.mp3'
output_spectrogram_file = 'output_with_message_spectrogram.png'



scale_freq,scale_time=add_message_to_spectrogram(sound_file, message, inital_spectrum_image, output_sound_file, output_spectrogram_file,start_freq=10*10**3,intensity=1e-3)
print(f'Scale frequency: {scale_freq}', f'Scale time: {scale_time}')
from spectoconvo import decode


sound_file_to_decode = 'output_with_message.mp3'


image_path = 'output_image_decode.png'

decode( sound_file_to_decode, image_path)