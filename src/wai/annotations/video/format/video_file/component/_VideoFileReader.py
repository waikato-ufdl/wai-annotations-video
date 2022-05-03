import cv2

from wai.annotations.core.component import SourceComponent
from wai.annotations.core.stream import ThenFunction, DoneFunction
from wai.annotations.domain.image import Image, ImageFormat
from wai.annotations.domain.image.object_detection import ImageObjectDetectionInstance

from wai.common.cli.options import TypedOption
from wai.common.adams.imaging.locateobjects import LocatedObjects


class VideoFileReader(
    SourceComponent[ImageObjectDetectionInstance]
):

    input_file: str = TypedOption(
        "-i", "--input",
        type=str,
        default="",
        help="the video file to read"
    )

    nth_frame: str = TypedOption(
        "-n", "--nth-frame",
        type=int,
        default=1,
        help="determines whether frames get skipped and only evert nth frame gets forwarded"
    )

    """
    The source of elements in a stream.
    """
    def produce(
            self,
            then: ThenFunction[ImageObjectDetectionInstance],
            done: DoneFunction
    ):
        """
        Produces elements and inserts them into the stream. Should call 'then'
        for each element produced, and then call 'done' when finished.

        :param then:    A function which forwards elements into the stream.
        :param done:    A function which closes the stream when called.
        """
        # open video file
        if not hasattr(self, "_cap"):
            self._cap = cv2.VideoCapture(self.input_file)
            self._frame_no = 0

        # next frame?
        count = 0
        while (self._cap is not None) and self._cap.isOpened():
            # next frame
            self._frame_no += 1
            count += 1
            retval, frame_curr = self._cap.read()

            if retval:
                # skip frame?
                if (self.nth_frame > 1) and (count < self.nth_frame):
                    continue
                count = 0
                data = cv2.imencode(".jpg", frame_curr)[1].tobytes()
                filename = "%08d.jpg" % self._frame_no
                height, width, _ = frame_curr.shape
                image = Image(filename=filename, data=data, format=ImageFormat.JPG, size=(width, height))
                instance = ImageObjectDetectionInstance(data=image, annotations=LocatedObjects())
                then(instance)
            else:
                self._cap.release()
                self._cap = None
                done()

        # close video file
        if self._cap is not None:
            self._cap.release()
            done()
