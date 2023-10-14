from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    feeds = Post.objects.all()
    return render(request, 'index.html', {'contents': feeds})

def post(req, var):
    display = Post.objects.get(id=var)
    return render(req, 'posts.html', {'context': display})

def addpost(request):
    if request.method == 'POST':
        data = request.POST  # see what this data variable is doing here 
        titl = data['title']
        bod = data['body']
        time = data['time']
        new_post = Post.objects.create(title=titl, body=bod, post_time=time)
        # new_post varaible assiognment not really neccesary 
        return redirect('index')
    return render(request, 'postform.html')
# check what the errors 301 and 302 stand for and revise other errors
# "POST /add HTTP/1.1" 302 0
# RuntimeWarning: DateTimeField Post.post_time received a naive datetime 
# (2022-04-08 00:00:00) while time zone support is active


# try the multi val dic get GET.get and that used in the open AI app also 
#TOdo: make the post body form bigger ...
# allow for addition of pictures to the post if need be in a n upgraded version 

#try to add a addition of post template 
# add try except block incase where post Id is deleted ..or on click more 

# def add(request):
#     categoryes = Categories.objects.all()  # see to change the name of the class later on ..use singular
#     context = {'categories': categoryes}
#     if request.method == 'POST':
#         data = request.POST
#         picture = request.FILES.get('image')  # the name is accessed from the name in the form  
#         if data['category'] != 'none':
#             category = Categories.objects.get(id=data['category'])
#             pic = Product.objects.create(
#             category=category,
#             description=data['description'],
#             image=picture
#         )
#             # add the else part to pop up message that product was not added 

#     return render(request, 'ilorintemp/add.html', context) 