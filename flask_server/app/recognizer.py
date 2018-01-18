import dlib
import scipy.misc
import numpy as np
import os
from PIL import Image

face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
face_recognition_model = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
TOLERANCE = 0.5

def get_face_encodings(path_to_image):
	image = scipy.misc.imread(path_to_image)
	detected_faces = face_detector(image, 1)
	if len(detected_faces)!=0:
		shapes_faces = [shape_predictor(image, face) for face in detected_faces]
		return [np.array(face_recognition_model.compute_face_descriptor(image, face_pose, 1)) for face_pose in shapes_faces]
	else:
		return None


def find_match(known_enc, test_enc):
	match = compare_face_encodings(known_enc, test_enc)
	if match:
		return match

	return 'Not Found'

def compare_face_encodings(known_enc, test_face):
	for key, value in known_enc.items():
		if (np.linalg.norm(value - test_face) <= TOLERANCE):
			return key
	return None

face_encodings = {}

def train_on_face(path_to_image, personName):
	images = os.listdir(path_to_image)
	enc = []
	for f in images:
		if f.endswith(".jpg"):
			# print d,f
			temp_encoding = get_face_encodings(os.path.join(path_to_image,f))
			if temp_encoding:
				enc.append(list(temp_encoding[0]))
	enc = np.array(enc).mean(axis=0)
	face_encodings[personName] = enc

def test_on_face(path_to_image):
	test_enc = get_face_encodings(path_to_image)
	match = find_match(face_encodings, test_enc)
	return match
