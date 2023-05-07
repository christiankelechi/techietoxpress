from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from .forms import CommentForm
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity
from .models import Post,Comment
# Create your views here.
def postlist(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return  render(request,'blog/postlist.html',context)

def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,status=Post.Status.PUBLISHED,slug=post,publish__year=year,publish__month=month,publish__day=day)
    
    # comments=post.comments.filter(active=True)

    form=CommentForm()

    # post_tags_ids = post.tags.values_list('id', flat=True)
    # similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                #   .exclude(id=post.id)
    # similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                # .order_by('-same_tags','-publish')[:4]
    return render(request,
                  'blog/postdetail.html',
                  {'post': post,
                   'form': form,})