from services import detectionService, morphableModelService, blenderService
import eos 

def create_avatar(request):
    # Retrieve image from API call
    image = request.files['image']
    ## Retrieve the landmarks
    landmarks = detectionService.retrieve_landmarks(image)
    ## Pass image / landmarks to model.
    model = morphableModelService.create_model(landmarks)
    mesh = blenderService.create_mesh(model)
    # save and return mesh

def retrieve_avatar(request):
    mesh = blenderService.final_mesh()
    # retrieve final mesh. request and response. Should include user ID.

def delete_avatar(request):
    mesh = blenderService.final_mesh()
    if mesh is not None:
        blenderService.delete_mesh(mesh)
    # delete the users mesh.


def update_avatar(request):
    pass
    # update and return updated mesh.
