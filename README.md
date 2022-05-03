# wai-annotations-video
wai.annotations plugin for video support.

## Plugins
### FROM-VIDEO-FILE-OD
Reads frames from a video file.

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: from-video-file-od [-f FROM_FRAME] [-i INPUT_FILE] [-m MAX_FRAMES] [-n NTH_FRAME] [-p PREFIX] [-t TO_FRAME]

optional arguments:
  -f FROM_FRAME, --from-frame FROM_FRAME
                        determines with which frame to start the stream (1-based index)
  -i INPUT_FILE, --input INPUT_FILE
                        the video file to read
  -m MAX_FRAMES, --max-frames MAX_FRAMES
                        determines the maximum number of frames to read; ignored if <=0
  -n NTH_FRAME, --nth-frame NTH_FRAME
                        determines whether frames get skipped and only evert nth frame gets forwarded
  -p PREFIX, --prefix PREFIX
                        the prefix to use for the frames
  -t TO_FRAME, --to-frame TO_FRAME
                        determines after which frame to stop (1-based index); ignored if <=0
```

### FROM-WEBCAM-OD
Reads frames from a webcam.

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: from-webcam-od [-f FROM_FRAME] [-m MAX_FRAMES] [-n NTH_FRAME] [-p PREFIX] [-t TO_FRAME] [-i WEBCAM_ID]

optional arguments:
  -f FROM_FRAME, --from-frame FROM_FRAME
                        determines with which frame to start the stream (1-based index)
  -m MAX_FRAMES, --max-frames MAX_FRAMES
                        determines the maximum number of frames to read; ignored if <=0
  -n NTH_FRAME, --nth-frame NTH_FRAME
                        determines whether frames get skipped and only evert nth frame gets forwarded
  -p PREFIX, --prefix PREFIX
                        the prefix to use for the frames
  -t TO_FRAME, --to-frame TO_FRAME
                        determines after which frame to stop (1-based index); ignored if <=0
  -i WEBCAM_ID, --webcam-id WEBCAM_ID
                        the webcam ID to read from
```
