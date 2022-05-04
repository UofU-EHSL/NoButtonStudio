import os
import multiprocessing
import time
import lights

def record():
    lights.lightScene("scene.start_recording")
    os.system("ffmpeg -hide_banner -nostats -y -f avfoundation -framerate 30 -pixel_format yuyv422 -i \"0:1\" out.mp4 > /dev/null 2>&1 < /dev/null")

def stop():
    print("Stop: ")
    state = input()
    print(state)
    os.system("pkill ffmpeg")
    lights.lightScene("scene.stop_recording")

if __name__ == '__main__':
    print("Starting the no button studio")
    while True:
        print("UID: ")
        uid = input()
        print(uid)
        recordVideo = multiprocessing.Process(target=record)
        recordVideo.start()
        time.sleep(5)
        stop()
        recordVideo.terminate()

