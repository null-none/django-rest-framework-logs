from .models import Logger


class LoggingMixin(object):

    def log(self, request, data, kwargs, text):
        Logger.objects.create(params=kwargs,
                              method_class=self.__class__.__name__,
                              query=request.POST,
                              result=data,
                              status=data['status'],
                              text=data['text_error'])

