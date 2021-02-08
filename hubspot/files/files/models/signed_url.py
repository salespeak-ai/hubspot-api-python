# coding: utf-8

"""
    Files

    Upload and manage files.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.files.files.configuration import Configuration


class SignedUrl(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "expires_at": "datetime",
        "url": "str",
        "name": "str",
        "extension": "str",
        "type": "str",
        "size": "int",
        "height": "int",
        "width": "int",
    }

    attribute_map = {
        "expires_at": "expiresAt",
        "url": "url",
        "name": "name",
        "extension": "extension",
        "type": "type",
        "size": "size",
        "height": "height",
        "width": "width",
    }

    def __init__(
        self,
        expires_at=None,
        url=None,
        name=None,
        extension=None,
        type=None,
        size=None,
        height=None,
        width=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SignedUrl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._expires_at = None
        self._url = None
        self._name = None
        self._extension = None
        self._type = None
        self._size = None
        self._height = None
        self._width = None
        self.discriminator = None

        self.expires_at = expires_at
        self.url = url
        self.name = name
        self.extension = extension
        self.type = type
        self.size = size
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width

    @property
    def expires_at(self):
        """Gets the expires_at of this SignedUrl.  # noqa: E501

        Timestamp of when the URL will no longer grant access to the file.  # noqa: E501

        :return: The expires_at of this SignedUrl.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this SignedUrl.

        Timestamp of when the URL will no longer grant access to the file.  # noqa: E501

        :param expires_at: The expires_at of this SignedUrl.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and expires_at is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `expires_at`, must not be `None`"
            )  # noqa: E501

        self._expires_at = expires_at

    @property
    def url(self):
        """Gets the url of this SignedUrl.  # noqa: E501

        Signed URL with access to the specified file. Anyone with this URL will be able to access the file until it expires.  # noqa: E501

        :return: The url of this SignedUrl.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SignedUrl.

        Signed URL with access to the specified file. Anyone with this URL will be able to access the file until it expires.  # noqa: E501

        :param url: The url of this SignedUrl.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and url is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `url`, must not be `None`"
            )  # noqa: E501

        self._url = url

    @property
    def name(self):
        """Gets the name of this SignedUrl.  # noqa: E501

        Name of the requested file.  # noqa: E501

        :return: The name of this SignedUrl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SignedUrl.

        Name of the requested file.  # noqa: E501

        :param name: The name of this SignedUrl.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def extension(self):
        """Gets the extension of this SignedUrl.  # noqa: E501

        Extension of the requested file.  # noqa: E501

        :return: The extension of this SignedUrl.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this SignedUrl.

        Extension of the requested file.  # noqa: E501

        :param extension: The extension of this SignedUrl.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and extension is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `extension`, must not be `None`"
            )  # noqa: E501

        self._extension = extension

    @property
    def type(self):
        """Gets the type of this SignedUrl.  # noqa: E501

        Type of the file. Can be IMG, DOCUMENT, AUDIO, MOVIE, or OTHER.  # noqa: E501

        :return: The type of this SignedUrl.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SignedUrl.

        Type of the file. Can be IMG, DOCUMENT, AUDIO, MOVIE, or OTHER.  # noqa: E501

        :param type: The type of this SignedUrl.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501

        self._type = type

    @property
    def size(self):
        """Gets the size of this SignedUrl.  # noqa: E501

        Size in bytes of the requested file.  # noqa: E501

        :return: The size of this SignedUrl.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SignedUrl.

        Size in bytes of the requested file.  # noqa: E501

        :param size: The size of this SignedUrl.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and size is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `size`, must not be `None`"
            )  # noqa: E501

        self._size = size

    @property
    def height(self):
        """Gets the height of this SignedUrl.  # noqa: E501

        For image and video files. The height of the file.  # noqa: E501

        :return: The height of this SignedUrl.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this SignedUrl.

        For image and video files. The height of the file.  # noqa: E501

        :param height: The height of this SignedUrl.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this SignedUrl.  # noqa: E501

        For image and video files. The width of the file.  # noqa: E501

        :return: The width of this SignedUrl.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this SignedUrl.

        For image and video files. The width of the file.  # noqa: E501

        :param width: The width of this SignedUrl.  # noqa: E501
        :type: int
        """

        self._width = width

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SignedUrl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignedUrl):
            return True

        return self.to_dict() != other.to_dict()
