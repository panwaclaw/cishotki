from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, JsonResponse

from django.views import View

from .models import TShirt, Tag, Topic, Rate
from users.models import User, Comment, Like
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.utils.timezone import timedelta
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

class TShirtsView(View):
	def get(self, request, tshirt_id):
		tshirt = get_object_or_404(TShirt, id=tshirt_id)

		comments = Comment.objects.filter(tshirt=tshirt_id)
		likes = Like.objects.none()
		for i in comments:
			l = Like.objects.filter(comment=i)
			print(l)
			likes = likes.union(l);

		print(likes)


		data = {
			"tshirt": tshirt,
			"comments": comments,
			"likes": likes,
		}
		
		return render(request, "tshirts/design_view.html", context=data)

class ForeignTShirtsView(View):
	def get(self, request, user_name):
		u = get_object_or_404(User, username=user_name)
		tshirts = TShirt.objects.all()
		ts = tshirts.filter(user=u.id)
		data = {
			"tshirts": ts,
			"u": u,
		}

		return render(request, "tshirts/foreign_tshirts.html", context=data)


class AjaxCommentLoadView(View):

	def get(self, request, tshirt_id):
		now=timezone.now() - timedelta(seconds=2);
		if not request.is_ajax():
			return HttpResponse()
		tshirt = get_object_or_404(TShirt, id=tshirt_id)
		comments = Comment.objects.filter(tshirt=tshirt, created__gte=now)

		comments_list = {}
		for i in comments:
			comments_list.update({str(i.id): {
				"user": i.user.username,
				"comment": i.comment,
				"comment_id": i.id,
			}})
		return JsonResponse(comments_list)

@login_required
def ajax_save_comment(request, tshirt_id):
	tshirt = TShirt.objects.get(id=tshirt_id)
	user = User.objects.get(id=request.POST["user"])
	comment = Comment.objects.create(
		user=user,
		tshirt=tshirt,
		comment=request.POST["comment"]
	)
	return JsonResponse({"status": comment.id})


@login_required
def ajax_save_like(request, comment_id):
	#tshirt = TShirt.objects.get(id=tshirt_id)
	print(comment_id)
	comment = Comment.objects.get(id=comment_id)

	try:
		l = Like.objects.get(comment=comment, user=request.user)
	except ObjectDoesNotExist:
		like = Like.objects.create(
			comment=comment,
			user=request.user
		)
		comment.like_counter += 1
		comment.save()
	else:
		pass

	return JsonResponse({"status": comment.like_counter})



		