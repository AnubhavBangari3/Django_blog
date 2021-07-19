from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . models import *
from . forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse #for reversing URL before your project url config is loaded
# Create your views here.
#def home(request):

 #   return render(request,"myblog/home.html",
  #                {})

class HomeView(ListView):
    model=Post           #will list our posts
    template_name="myblog/home.html"
    ordering=['-id']

    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context
def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:

        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))


class ArticleDetailView(DetailView):
    model=Post                             ##shows our article
    template_name="myblog/article_details.html"

    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(ArticleDetailView,self).get_context_data(*args,**kwargs)

        stuff=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()

        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True


        context["cat_menu"]=cat_menu
        context["total_likes"]=total_likes
        context["liked"]=liked

        return context

class AddPostView(CreateView):
    model=Post                      #adds post
    form_class=PostForm
    template_name="myblog/add_post.html"
    #fields="__all__"

class AddCommentView(CreateView):
    model=Comment                    
    form_class=CommentForm
    template_name="myblog/add_comment.html"
    #fields="__all__"
    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)

    success_url=reverse_lazy('home')



class AddCategoryView(CreateView):
    model=Category                   #adds 
    #form_class=PostForm
    template_name="myblog/add_category.html"
    fields="__all__"

def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))

    return render(request,"myblog/categories.html",
                  {
                    'cats':cats.replace('-',' '),
                    'category_posts':category_posts
                    })
def CategoryListView(request):
    cat_menu_list=Category.objects.all()

    return render(request,"myblog/category_list.html",
                  {
                    'cat_menu_list':cat_menu_list
                    })

class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm      #update post
    template_name="myblog/update_post.html"
    #fields="__all__"

class DeletePostView(DeleteView):
    model=Post
    template_name="myblog/delete_post.html"
    success_url=reverse_lazy('home') #for providing url to delete post before it is loaded 
                                          #in our url config
