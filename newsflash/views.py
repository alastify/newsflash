from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def info(request, extra_context=None, **kwargs):

    context = {

    }

    template = loader.get_template('newsflash/info.html')
    context.update(extra_context or {})

    #return TemplateResponse(request, template, context).render()
    return HttpResponse(template.render(context, request))


def kontakt(request, extra_context=None, **kwargs):

    context = {

    }

    template = loader.get_template('newsflash/kontakt.html')
    context.update(extra_context or {})

    #return TemplateResponse(request, template, context).render()
    return HttpResponse(template.render(context, request))
