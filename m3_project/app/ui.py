from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext


class PermissionAddWindow(BaseEditWindow):
    def _init_components(self):
        super(PermissionAddWindow, self)._init_components()
        self.field__group = ext.ExtStringField(
            label=u'Группа',
            name='group',
            anchor='100%',
        )
        self.field__user = ext.ExtStringField(
            label=u'User',
            name='user',
            anchor='100%',
        )
        self.field__id = ext.ExtNumberField(
            label=u'ID',
            name='id',
            anchor='100%',
        )
        self.field__name = ext.ExtStringField(
            label=u'Name',
            name='name',
            anchor='100%',
        )
        self.field__content_type = ext.ExtComboBox(
            label='Content_type',
            name='content_type__name',
            anchor='100%',
            action_context='content_type',
        )
        # self.field__content_type = ext.ExtGridColumn(
        #     label='Content_type',
        #     name='content_type',
        #     anchor='100%',
        # )

        self.field__codename = ext.ExtStringField(
            label=u'Codename',
            name='codename',
            anchor='100%',
        )

    def _do_layout(self):
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__group,
            self.field__user,
            self.field__id,
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'


class UserAddEditWindow(BaseEditWindow):
    def _init_components(self):
        super(UserAddEditWindow, self)._init_components()
        self.field__logentry = ext.ExtDisplayField(
            label=u'Вход',
            name='logentry',
            anchor='100%',
        )
        self.field__id = ext.ExtNumberField(
            label=u'ID',
            name='id',
            anchor='100%',
        )
        self.field__last_login = ext.ExtDateField(
            label=u'Last login',
            name='last_login',
            anchor='100%',
        )
        self.field__is_superuser = ext.ExtCheckBox(
            label=u'Is superuser',
            name='is_superuser',
            anchor='100%',
        )
        self.field__username = ext.ExtStringField(
            label=u'Username',
            name='username',
            anchor='100%',
        )
        self.field__first_name = ext.ExtStringField(
            label=u'First name',
            name='first_name',
            anchor='100%',
        )
        self.field__last_name = ext.ExtStringField(
            label=u'Last name',
            name='last_name',
            anchor='100%',
        )
        self.field__email = ext.ExtStringField(
            label=u'Email',
            name='email',
            anchor='100%',
        )
        self.field__is_staff = ext.ExtCheckBox(
            label=u'Is staff',
            name='is_staff',
            anchor='100%',
        )
        self.field__is_active = ext.ExtCheckBox(
            label=u'Is active',
            name='is_active',
            anchor='100%',
        )
        self.field__date_joined = ext.ExtDateField(
            label=u'Date joined',
            name='date_joined',
            anchor='100%',
        )
        self.field__groups = ext.ExtMultiSelectField(
            label=u'Groups',
            name='groups',
            anchor='100%'
        )

    # def _do_layout(self):
    #     super(PermissionAddWindow, self)._do_layout()
    #     self.form.items.extend((
    #         self.field__group,
    #         self.field__user,
    #         self.field__id,
    #         self.field__name,
    #         self.field__content_type,
    #         self.field__codename,
    #     ))
    #
    # def set_params(self, params):
    #     super(PermissionAddWindow, self).set_params(params)
    #     self.height = 'auto'

