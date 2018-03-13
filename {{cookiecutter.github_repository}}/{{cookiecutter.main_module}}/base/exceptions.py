# Third Party Stuff
from django.core.exceptions import PermissionDenied as DjangoPermissionDenied
from django.http import Http404
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions, status
from rest_framework.response import Response


class BaseException(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Unexpected error')

    def __init__(self, detail=None):
        self.detail = detail or self.default_detail


class NotFound(BaseException, Http404):
    """Exception used for not found objects.
    """

    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('Not found.')


class NotSupported(BaseException):
    status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    default_detail = _('Method not supported for this endpoint.')


class BadRequest(BaseException):
    """Exception used on bad arguments detected on api view.
    """
    default_detail = _('Wrong arguments.')


class WrongArguments(BadRequest):
    """Exception used on bad arguments detected on service. This is same as `BadRequest`.
    """
    default_detail = _('Wrong arguments.')


class RequestValidationError(BadRequest):
    default_detail = _('Data validation error')


class PermissionDenied(exceptions.PermissionDenied):
    """Compatibility subclass of restframework `PermissionDenied` exception.
    """
    pass


class IntegrityError(BadRequest):
    default_detail = _('Integrity Error for wrong or invalid arguments')


class PreconditionError(BadRequest):
    """Error raised on precondition method on viewset.
    """
    default_detail = _('Precondition error')


class NotAuthenticated(exceptions.NotAuthenticated):
    """Compatibility subclass of restframework `NotAuthenticated` exception.
    """
    pass


def parse_field_errors(field, error_msg, error_values, depth=0):
    # We only parse errors upto 10 nested serializers
    if depth is not None:
        assert depth >= 0, "'depth' may not be negative."
        assert depth <= 10, "'depth' may not be greater than 10."

    errors = []

    if isinstance(error_msg, dict):
        for error_msg_key, error_msg_values in list(error_msg.items()):
            for msg in error_msg_values:
                errors.append(
                    {
                        'field': field,
                        'message': None,
                        'errors': parse_field_errors(error_msg_key, msg, error_values, depth=depth + 1)
                    }
                )
    else:
        errors.append(
            {
                'field': error_msg if error_msg and error_values and type(error_values) != list else field,
                'message': ' '.join(error_values[error_msg]) if error_msg and error_values and
                           type(error_values) != list else error_msg,
            }
        )

    return errors


def format_exception(exc):
    class_name = exc.__class__.__name__
    detail = {
        'errors': [],
        'error_type': class_name,
    }
    if isinstance(exc.detail, dict):
        for error_key, error_values in list(exc.detail.items()):
            for error_msg in error_values:
                # Special Case for model clean
                if error_key == 'non_field_errors':
                    detail['errors'].append(
                        {
                            'message': error_msg,
                        }
                    )
                else:
                    detail['errors'] = detail['errors'] + parse_field_errors(error_key, error_msg, error_values)
    elif isinstance(exc.detail, list):
        for error_msg in exc.detail:
            detail['errors'].append(
                {
                    'message': error_msg,
                }
            )
    else:
        detail['errors'].append(
            {
                'message': force_text(exc.detail),
            }
        )

    return detail


def exception_handler(exc, context=None):
    """Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's builtin `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['X-Throttle-Wait-Seconds'] = '%d' % exc.wait

        detail = format_exception(exc)
        return Response(detail, status=exc.status_code, headers=headers)

    elif isinstance(exc, Http404):
        return Response({'error_type': exc.__class__.__name__,
                         'errors': [{'message': str(exc)}]},
                        status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, DjangoPermissionDenied):
        return Response({'error_type': exc.__class__.__name__,
                         'errors': [{'message': str(exc)}]},
                        status=status.HTTP_403_FORBIDDEN)

    # Note: Unhandled exceptions will raise a 500 error.
    return None
