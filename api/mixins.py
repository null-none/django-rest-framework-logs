from .models import Logger


class LoggingMixin(object):

    def log(self, request, data, kwargs):
        if settings.DEBUG:
            Logger.objects.create(params=kwargs,
                                  method_class=self.__class__.__name__,
                                  query=request.DATA,
                                  result=data,
                                  status=data['status'])
