from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import CropAddForm
from .models import Crop
from .utils import pred_tomato_disease
import os
import shutil

# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required
def addCropImage(request):

    status = False

    if request.method == "POST":
        form = CropAddForm(request.POST)

        if form.is_valid():
            status = True
            instance = form.save(commit=False)
            instance.user = request.user
            instance.photo = request.FILES["photo"]
            instance.save()

            file = instance.photo
            # # file_path = f"../media/{file.name}"
            # file_path = os.path.join(settings.BASE_DIR, "media", file.name.replace("/", "\\"))
            # shutil.copyfile(file_path, os.path.join(settings.BASE_DIR, "display_images", file.name.replace("/", "\\")))
            # # file.save(file_path)

            return redirect(reverse("detector:predict_disease") + f"?file_name={file.name}&id={instance.id}")
        
        else:
            print(form.errors)
            print(form.non_field_errors)
            status = False
            form = CropAddForm()
    
    else:
        form = CropAddForm()
    
    context = {
        "form": form,
        "status": status,
        "user": request.user,
    }

    return render(request, "upload_image.html", context)
    
    # else:
    #     print("Check request method in /detect/upload_image route")

@login_required
def predict(request):

    # if request.method == "POST" or request.method == "GET":
    file_name = request.GET.get("file_name")
    id = request.GET.get("id")
    # print(file_name)
    # print(file_name.replace("/", "\\"))
    # print(os.path.join(settings.BASE_DIR, "display_images", file_name.replace("/", "\\")))

    print("########")
    print(file_name)
    disease, remedy = pred_tomato_disease(os.path.join(settings.BASE_DIR, "media", file_name.replace("/", "\\")))
    print(disease)
    print(remedy)

    instance = Crop.objects.filter(id=id).first()
    instance.disease = disease
    instance.remedy = remedy
    instance.save()

    print(file_name)

    category = -1
    if file_name.startswith("crop_images/Tomato___Bacterial_spot"):
        category = 0
    elif file_name.startswith("crop_images/Tomato___Early_blight"):
        category = 1
    elif file_name.startswith("crop_images/Tomato___healthy"):
        category = 2
    elif file_name.startswith("crop_images/Tomato___Late_blight"):
        category = 3
    elif file_name.startswith("crop_images/Tomato___Leaf_Mold"):
        category = 4
    elif file_name.startswith("crop_images/Tomato___Septoria_leaf_spot"):
        category = 5
    elif file_name.startswith("crop_images/Tomato___Spider_mites "):
        category = 6
    elif file_name.startswith("crop_images/Tomato___Target_Spot"):
        category = 7
    elif file_name.startswith("crop_images/Tomato___Tomato_mosaic_virus"):
        category = 8
    elif file_name.startswith("crop_images/Tomato___Tomato_Yellow_Leaf_Curl_Virus"):
        category = 9
    
    print(category)

    context = {
        "disease": disease,
        "remedy": remedy,
        # "uploaded_image": os.path.join(settings.BASE_DIR, "media", file_name.replace("/", "\\")),
        # "uploaded_image": file_name,
        "category": category,
    }

    return render(request, "result.html", context)