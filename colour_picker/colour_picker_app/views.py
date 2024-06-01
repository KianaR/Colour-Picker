import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image_Upload, Colour_Store
from PIL import Image
import colorsys

def main(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()

            form = ImageForm()
            img_obj = Image_Upload.objects.latest("date_uploaded")
            img = img_obj.image.url
            id = img_obj.id
            context = {
                "form": form,
                "image": img,
                "id": id
            }
            colours_stores = Colour_Store.objects.all()
            for col in colours_stores: #clear recent colours per picture/refresh
                col.delete()

            return render(request, "main.html", context)

        else:
            form = ImageForm()
            context = {
                "form": form
            }
            return render(request, "main.html", context)
    else:
        form = ImageForm()
        context = {
            "form": form
        }
        return render(request, "main.html", context)
    

def request_colour(request):
    img_id = request.POST["img_id"]
    x = float(request.POST["x"])
    y = float(request.POST["y"])
    img_file = Image_Upload.objects.get(id=img_id).image

    img = Image.open(img_file)
    px = img.load()
    px_colour = px[x, y]

    rgb = ",".join(str(x) for x in px_colour)
    
    try:
        hex = '#%02x%02x%02x' % px_colour
    except:
        hex = 0

    colour = Colour_Store(colour_value=rgb, type="RGB")
    colour.save()

    recent_colours = Colour_Store.objects.order_by('-id')[:10]
    recents = []
    for colour in recent_colours:
        recents.append((colour.type, colour.colour_value))

    return HttpResponse(json.dumps({"rgb":rgb, "hex":hex, "recents":recents}))
