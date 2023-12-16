import pyaudio

def list_audio_devices():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    print("Available audio devices:")
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id {} - {}".format(i, p.get_device_info_by_host_api_device_index(0, i).get('name')))
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels')) > 0:
            print("Output Device id {} - {}".format(i, p.get_device_info_by_host_api_device_index(0, i).get('name')))

if __name__ == "__main__":
    list_audio_devices()
