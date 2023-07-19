from services import detectionService, morphableModelService, blenderService

def create_avatar(request):
    image = request.files['image']
    landmarks = detectionService.detect_landmarks(image)
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
