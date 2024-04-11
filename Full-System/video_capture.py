import threading
import time
import cv2
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VideoCaptureAsync:
    def __init__(self, src=0, width=640, height=480, driver=None):
        self.src = src
        try:
            if driver is None:
                self.cap = cv2.VideoCapture(self.src)
            else:
                self.cap = cv2.VideoCapture(self.src, driver)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        except Exception as e:
            logging.error(f"Failed to initialize video capture: {e}")
            raise

        self.grabbed, self.frame = self.cap.read()
        if not self.grabbed:
            logging.error("Failed to grab initial frame.")
        self.started = False
        self.read_lock = threading.Lock()
        self.thread = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exec_type, exc_value, traceback):
        self.stop()
        self.cap.release()

    def start(self):
        if self.started:
            logging.warning("[!] Asynchronous video capturing has already been started.")
            return None
        self.started = True
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self):
        while self.started:
            try:
                grabbed, frame = self.cap.read()
                with self.read_lock:
                    self.grabbed = grabbed
                    self.frame = frame
                if not grabbed:
                    logging.warning("Failed to grab frame.")
                    break
            except Exception as e:
                logging.error(f"Error capturing frame: {e}")
                break

    def read(self):
        with self.read_lock:
            frame = self.frame.copy() if self.frame is not None else None
            grabbed = self.grabbed
        return grabbed, frame

    def stop(self):
        self.started = False
        if self.thread is not None:
            self.thread.join()

if __name__ == "__main__":
    # Example usage
    with VideoCaptureAsync(0) as cap:
        time.sleep(2)  # Simulate processing for 2 seconds
        grabbed, frame = cap.read()
        if grabbed:
            cv2.imshow("Frame", frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            logging.error("Failed to read frame.")
