from django.shortcuts import render
from .models import Blog
from django.contrib import messages
from django.db.models import Q 

def blog_view(request):
    blogs = Blog.objects.all() 
    query=""
    
    if request.method == "POST":
        if "add" in request.POST:
            Title = request.POST.get("Title")
            Subtitle = request.POST.get("subTitle")
            Image = request.POST.get("Image")
            Description = request.POST.get("Desc")
            Blog.objects.create(
                Title=Title,
                Subtitle=Subtitle,
                Image=Image,
                Description=Description
            )
            messages.success(request, "Blog added successfully")
            
        elif "update" in request.POST:
            id = request.POST.get("id")
            Title = request.POST.get("Title")
            Subtitle = request.POST.get("subTitle")
            Image = request.POST.get("Image")
            Description = request.POST.get("Desc")
            
            update_blog = Blog.objects.get(id=id)
            update_blog.Title = Title
            update_blog.Subtitle = Subtitle
            update_blog.Image = Image
            update_blog.Description = Description
            update_blog.save()
            
            messages.success(request, "Blog updated successfully")
            
            
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Blog.objects.get(id=id).delete()
            messages.success(request, "Blog deleted successfully")
            
            
        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            blogs = Blog.objects.filter(Q(Title__icontains=query)| Q(Subtitle__icontains=query)| Q(Image__icontains=query)| Q(Description__icontains=query))
    
    context = {
        "blogs": blogs,
        "query": query
    }
    return render(request, 'home/blog.html', context=context)