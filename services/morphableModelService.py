import eos
import numpy as np
import cv2
import dlib




# Load an image passed in by Flask API
image = cv2.imread("") 



# Load the 3D Morphable Model
model = eos.morphablemodel.load_model("../share/sfm_shape_3448.bin")
blendshapes = eos.morphablemodel.load_blendshapes("../share/expression_blendshapes.bin")

# Load a pre-trained facial landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("")

# Detect landmarks in the image
faces = detector(image)
landmarks = predictor(image, faces[0])

# Fit the model, get the shape coefficients
model_shape = eos.fitting.fit_shape(model, landmarks)
blendshapes_coefficients = np.zeros(len(blendshapes))
shape_coefficients = np.hstack((model_shape.get_coeffs(), blendshapes_coefficients))

# Obtain the fitted mesh
mesh = eos.morphablemodel.draw_sample(model, shape_coefficients, blendshapes, [], [])

# Extract the texture from the image using given mesh and landmarks
texture = eos.render.extract_texture(mesh, landmarks, image)

# Save the mesh as textured obj:
eos.core.write_textured_obj(mesh, "out.obj")

# Save the texture:
cv2.imwrite("out.png", texture)

# Display the mesh:
cv2.imshow("mesh", texture)


def main():
    pass;


if __name__ == "__main__":
    main();