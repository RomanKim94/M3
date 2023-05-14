from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .controller import observer
from .ui import PermissionAddWindow


class UserPack(ObjectPack):
    model = User
    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model)
    columns = [{'data_index': field.name, 'header': field.name, 'width': 1} for field in model._meta.get_fields()]


class GroupPack(UserPack):
    model = Group
    add_window = edit_window = ModelEditWindow.fabricate(model)
    columns = [{'data_index': field.name, 'header': field.name, 'width': 1} for field in model._meta.get_fields()]


class PermissionPack(ObjectPack):
    add_to_menu = True
    model = Permission
    # add_window = edit_window = ModelEditWindow.fabricate(model)
    add_window = edit_window = PermissionAddWindow

    columns = [
        {
            'data_index': '__unicode__',
            'hidden': True,
        },
        {
            'data_index': 'name',
            'width': 1,
            'header': u'Name',
        },
        {
            'data_index': 'content_type.name',
            'width': 1,
            'header': 'Контент тайп',
        },
        # {
        #     'header': 'Group column',
        #     'columns': [
        #         {
        #             'data_index': 'content_type.name',
        #             'width': 1,
        #             'header': 'Контент тайп',
        #         },
        #         {
        #             'data_index': 'content_type.app_label',
        #             'width': 1,
        #             'header': 'Label',
        #         },
        #                ]
        # }
    ]


class ContentTypePack(UserPack):
    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model)
    columns = [{'data_index': field.name, 'header': field.name, 'width': 1} for field in model._meta.get_fields()]
