# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from abc import ABCMeta, abstractproperty, abstractmethod
from six import with_metaclass


class APIArgumentSerializer(with_metaclass(ABCMeta, object)):
    @abstractmethod
    def to_api(self, python_value):
        """
        """
        pass

    @abstractmethod
    def to_python(self, api_value):
        pass


class APIArgument(with_metaclass(ABCMeta, object)):
    def __init__(self, name, description=None, required=True):
        self.name = name
        self.description = description
        self.required = required

    @abstractproperty
    def serializer_class(self):
        pass


class API(with_metaclass(ABCMeta, object)):
    @abstractproperty
    def method(self):
        """
        Returns the exact name of the XMLRPC API method to call
        :rtype: str
        :return: Name of the XMLRPC API method to call
        """

    @abstractproperty
    def arguments(self):
        """
        Returns an (ordered) list of APIArgument objects.
        :rtype: Iterable
        :return: An iterable containing the arguments
        """

    @property
    def authenticate(self):
        """
        Defines whether or not we should authenticate when calling this API
        :return:
        """
        return True

    def transform_arguments(self, context, **kwargs):
        """
        Handler method to transform an argument before processing
        :param context: A dictionary containing client context info
        :type context: dict
        :param kwargs: Named argument dictionary
        :type kwargs: dict
        :rtype: dict
        :return:
        """
        return kwargs

    def validate_response(self, context, api, arguments, response):
        """
        Handler to validate the API response. Can be used to raise an exception to indicate failure. If it does not
          raise an exception, the pipeline will continue with the 'transform_response' method.
        :param context: A dictionary containing client context info
        :type context: dict
        :param api: The api object that has been used for the call
        :type api: py:class:API
        :param arguments: The dictionary containing the arguments that have ben used to perform the call
        :type arguments: dict
        :param response:
        :type response: object
        :rtype: object
        :return:
        """

    def transform_response(self, context, api, arguments, response):
        """
        Handler method to process the response. The output of this method will be returned as the output of the API
          call.
        :param context: A dictionary containing client context info
        :type context: dict
        :param api: The api object that has been used for the call
        :type api: py:class:API
        :param arguments: The dictionary containing the arguments that have ben used to perform the call
        :type arguments: dict
        :param response:
        :type response: object
        :rtype: object
        :return:
        """
        return response
