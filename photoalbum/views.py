from django.shortcuts import render

# Create your views here.
from django.views import View

from photoalbum.forms import AddPhotoForm
from photoalbum.models import Photo


class MainView(View):
    def get(self, request):
        form = AddPhotoForm()
        photos = Photo.objects.all()
        ctx = {
            'objects': photos,
            'form': form
        }
        return render(request, 'photoalbum/main.html', ctx)

    def post(self, request):
        new_photo = Photo(users=request.user)
        form = AddPhotoForm(request.POST, files=request.FILES, instance=new_photo)
        print(request.POST.get('submit'))
        print(form.is_valid())
        if request.POST.get('submit')=='add' and form.is_valid():
            print('jestem w if')

            form.save()
            # new_photo.users = request.user
            # new_photo.save()
            photos = Photo.objects.all()
            ctx = {
                'objects': photos,
                'form': form
            }
            return render(request, 'photoalbum/main.html', ctx)
        else:
            print('jestem w else')
            return render(request, 'photoalbum/main.html', {'form':form})
            form = AddPhotoForm()

            like_id = request.POST.get('photo_like')
            unlike_id = request.POST.get('photo_unlike')
            photo = Photo.objects.get(id=like_id or unlike_id)
            if like_id:
                photo.misa_like_it += 1
                photo.likers.add(request.user)
            else:
                photo.misa_like_it -= 1
                photo.likers.remove(request.user)
            photo.save()
            photos = Photo.objects.all()
            ctx = {
                'objects': photos,
                'form': form
            }
            return render(request, 'photoalbum/main.html', ctx)
