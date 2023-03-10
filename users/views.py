from django.shortcuts import render, get_object_or_404

from django.views.generic.detail import DetailView

from users.models import Profile


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'base/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
