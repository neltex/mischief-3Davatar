import mediapipe as mp
from mediapipe.tasks import python 
from mediapipe.tasks.python import vision 

# define an image
# define a live stream video 

# Face Detection Model
faceDetectionModel_path = '../models/blaze-faceDetection.tflite'


#Face Landmark Model
faceLandmarkModel_path = '../models/face_landmarker.task'


mp_image = mp.Image.create_from_file('../images/girl.jpg')


## Face Detection
BaseOptions = mp.tasks.BaseOptions 
FaceDetector = mp.tasks.vision.FaceDetector
FaceDetectorOptions = mp.tasks.vision.FaceDetectorOptions
VisionRunningMode = mp.tasks.python.VisionRunningMode


## Face Landmark
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions


facelandmarkOptions = FaceLandmarkerOptions(
    base_options=BaseOptions(),
    running_mode=VisionRunningMode.Image)
with FaceLandmarker.create_from_options(facelandmarkOptions) as landmarker:
    pass

faceDetectionOptions = FaceDetectorOptions(
    base_options=BaseOptions(),
    running_mode=VisionRunningMode.Image)
with FaceDetector.create_from_options(faceDetectionOptions) as detector:
    if detector == None:
        print("No face detected. Please use your face.")
    if mp_image == None:
        print("No Image Detected")

    results = detector.process(mp_image)
    
    