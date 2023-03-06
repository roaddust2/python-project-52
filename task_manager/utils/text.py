from django.utils.translation import gettext_lazy as _


class Titles:
    def __init__(self):
        self.user_create = _('UserCreateTitle')
        self.users_read = _('UsersReadTitle')
        self.user_update = _('UserUpdateTitle')
        self.user_delete = _('UserDeleteTitle')


class Messages:
    def __init__(self):
        self.user_create_succ = _('UserCreateMessageSucc')
        self.user_update_succ = _('UserUpdateMessageSucc')
        self.user_update_err = _('UserUpdateMessageErr')
        self.user_delete_succ = _('UserDeleteMessageSucc')
        self.user_delete_err = _('UserDeleteMessageErr')

        self.user_login_succ = _('UserLoginMessageSucc')
        self.user_logout_succ = _('UserLogoutMessageSucc')
        
