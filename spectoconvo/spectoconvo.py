import numpy as np
from scipy.io import wavfile
from scipy.signal import stft, istft
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from skimage import io, color, transform
import os
def text_to_image(text, font_path='fonts/NotoSansSC-Bold.ttf', font_size=20, image_path='message_image.png'):
    # Create a font object
    print(os.path.exists(font_path))
    font = ImageFont.truetype(font_path,font_size)
    
    # Determine the size of the text
    text_bbox = font.getbbox(text)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    
    # Create a new image with a white background
    image = Image.new('RGB', (text_width + 20, text_height + 20), 'white')
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    # Draw the text on the image
    draw.text((10, 10), text, font=font, fill='black')
    
    # Save the image
    image.save(image_path)

def plot_inverted_image(image_path='output_image.png'):
    # Load the image
    image = io.imread(image_path)
    gray_image = color.rgb2gray(image)

    # Flip the image vertically
    gray_image = np.flipud(gray_image)

    # Invert the grayscale image
    grey_image = np.abs(-1 * (gray_image - 1))

    return grey_image

def add_message_to_spectrogram(sound_file, message, inital_spectrum_image, output_sound_file, output_spectrogram_file,scale_freq=0,scale_time=0):
    # Read the sound file
    text_to_image(message)
    sample_rate, samples = wavfile.read(sound_file)
    
    # Convert to mono if the audio has multiple channels
    if samples.ndim > 1:
        samples = np.mean(samples, axis=1)
    
    # Generate the STFT with increased frequency resolution
    nperseg = 4096  # Increase this value to increase the number of frequency bins
    noverlap = nperseg // 2
    frequencies, times, Zxx = stft(samples, sample_rate, nperseg=nperseg, noverlap=noverlap)
    
    # Convert the complex STFT result to magnitude
    Sxx = np.abs(Zxx)
    
    # Avoid log of zero by adding a small constant
    Sxx += 1e-10
    
    # Print the maximum value of Sxx

    
    # Plot the original spectrogram
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud', cmap='inferno')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    
    # Add the message to the spectrogram

    # Save the original spectrogram image
    plt.savefig(inital_spectrum_image)
    plt.close()
    
    # Encode the message into the spectrogram
    message_encoded = np.array([ord(char) for char in message])
    message_encoded = np.pad(message_encoded, (0, Sxx.shape[1] - len(message_encoded)), 'constant')
    
    # Find the index corresponding to 20kHz
    freq_index = np.argmin(np.abs(frequencies - 20000))
    
    # Load and process the image
    grey_image = plot_inverted_image('message_image.png')

    
    # Resize the grey_image to match the desired range in Sxx
    if scale_freq==0:
        scale_freq= Sxx.shape[0] - freq_index
    if scale_time==0:
        scale_time= Sxx.shape[1]
    freq_range =  scale_freq # Number of frequency bins to use
    time_range = scale_time# Number of time bins to use
    grey_image_resized = transform.resize(grey_image, (freq_range, time_range))
    
    # Embed the grey_image into the spectrogram
    Sxx[freq_index:freq_index + freq_range, :time_range] += grey_image_resized * np.max(Sxx) * 1e-5  # Adjust the intensity
    
    # Print the maximum value of Sxx after embedding the image

    
    # Convert the modified spectrogram back to time domain
    _, modified_samples = istft(Sxx * np.exp(1j * np.angle(Zxx)), sample_rate, nperseg=nperseg, noverlap=noverlap)
    
    # Normalize the modified samples to avoid clipping
    modified_samples = np.int16(modified_samples / np.max(np.abs(modified_samples)) * 32767)
    
    # Save the modified sound file
    wavfile.write(output_sound_file, sample_rate, modified_samples)
    
    # Generate the spectrogram of the modified audio
    frequencies, times, Zxx = stft(modified_samples, sample_rate, nperseg=nperseg, noverlap=noverlap)
    Sxx = np.abs(Zxx)
    
    # Avoid log of zero by adding a small constant
    Sxx += 1e-10
    
    # Plot the spectrogram of the modified audio
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud', cmap='inferno')  # Use a different color map
    plt.colorbar(label='Intensity [dB]')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    
    # Save the spectrogram image of the modified audio
    plt.savefig(output_spectrogram_file)
    plt.close()
    return scale_freq, scale_time
def decode(sound_file, image_path):
    # Read the sound file
    sample_rate, samples = wavfile.read(sound_file)

    # Convert to mono if the audio has multiple channels
    if samples.ndim > 1:
        samples = np.mean(samples, axis=1)

    # Generate the STFT
    nperseg = 4096
    noverlap = nperseg // 2
    frequencies, times, Zxx = stft(samples, sample_rate, nperseg=nperseg, noverlap=noverlap)

    # Convert the complex STFT result to magnitude
    Sxx = np.abs(Zxx)

    # Avoid log of zero by adding a small constant
    Sxx += 1e-10

    # Plot the spectrogram
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud', cmap='inferno')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.colorbar(label='Intensity [dB]')
    plt.savefig(image_path)
    plt.close()
    print(f'{image_path} saved')
    

