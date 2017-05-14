from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Zpravy, Kolotoc
from .forms import ZpravyForm


def news(request, extra_context=None, **kwargs):

    context = {
        "promo": Kolotoc.objects.all().order_by('-id')[:3],
        "hlavni": Zpravy.objects.filter(hlavni__exact=1).order_by('-datum')[:3],
        "zpravy": Zpravy.objects.filter(hlavni__exact=0).order_by('-datum'),
        "form": ZpravyForm(),
    }

    template = loader.get_template('flashes/index.html')
    context.update(extra_context or {})

    return HttpResponse(template.render(context, request))


def detail(request, id, extra_context=None, **kwargs):

    context = {
        "zprava": Zpravy.objects.get(pk=id)
    }

    template = loader.get_template('flashes/detail.html')
    context.update(extra_context or {})

    return HttpResponse(template.render(context, request))


def promo(request, id, extra_context=None, **kwargs):

    banner = Kolotoc.objects.get(pk=id)

    context = {
        "banner": banner,
        "zprava": banner.zprava,
    }

    template = loader.get_template('flashes/promo.html')
    context.update(extra_context or {})

    return HttpResponse(template.render(context, request))


def pridat(request, extra_context=None, **kwargs):

    if request.POST:
        form = ZpravyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ZpravyForm()

    context = {
        "form": form,
    }

    template = loader.get_template('flashes/pridat.html')
    context.update(extra_context or {})

    return HttpResponse(template.render(context, request))
