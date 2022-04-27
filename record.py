from fileinput import filename
import cv2
import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)

def recordVideo():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Check if camera opened successfully
    if (cap.isOpened() == False): 
        print("Unable to read camera feed")

    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc('m','p','4','v'), 30, (frame_width,frame_height))

    while(True):
        ret, frame = cap.read()

        if ret == True: 
        
            # Write the frame into the file 'output.avi'
            out.write(frame)

            # Display the resulting frame    
            cv2.imshow('frame',frame)

            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break  

    # When everything done, release the video capture and video write objects
    cap.release()
    out.release()

    # Closes all the frames
    cv2.destroyAllWindows()
    
def recordAudio():
    q = queue.Queue()
    filename = "audio.wav"
    device = 0
    samplerate = 44100
    channels = 1
    subtype = "PCM_24"


    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())


    try:
        if samplerate is None:
            device_info = sd.query_devices(device, 'input')
            # soundfile expects an int, sounddevice provides a float:
            samplerate = int(device_info['default_samplerate'])
        if filename is None:
            filename = tempfile.mktemp(prefix='delme_rec_unlimited_',
                                            suffix='.wav', dir='')

        # Make sure the file is opened before recording anything:
        with sf.SoundFile(filename, mode='x', samplerate=samplerate,
                        channels=channels, subtype=subtype) as file:
            with sd.InputStream(samplerate=samplerate, device=device,
                                channels=channels, callback=callback):
                print('#' * 80)
                print('press Ctrl+C to stop the recording')
                print('#' * 80)
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(filename))
        exit(0)
    except Exception as e:
        exit(type(e).__name__ + ': ' + str(e))

if __name__ == '__main__':
    #recordVideo()
    recordAudio()