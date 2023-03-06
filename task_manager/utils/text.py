from django.utils.translation import gettext_lazy as _


class Titles:
    def __init__(self):
        self.user_create = _('UserCreateTitle')
        self.users_list = _('UsersListTitle')
        self.user_update = _('UserUpdateTitle')
        self.user_delete = _('UserDeleteTitle')

        self.status_create = _('StatusCreateTitle')
        self.statuses_list = _('StatusesListTitle')
        self.status_update = _('StatusUpdateTitle')
        self.status_delete = _('StatusDeleteTitle')

        self.tag_create = _('TagCreateTitle')
        self.tags_list = _('TagsListTitle')
        self.tag_update = _('TagUpdateTitle')
        self.tag_delete = _('TagDeleteTitle')


class Messages:
    def __init__(self):
        self.user_create_succ = _('UserCreateMessageSucc')
        self.user_update_succ = _('UserUpdateMessageSucc')
        self.user_update_err = _('UserUpdateMessageErr')
        self.user_delete_succ = _('UserDeleteMessageSucc')
        self.user_delete_err = _('UserDeleteMessageErr')

        self.user_login_succ = _('UserLoginMessageSucc')
        self.user_logout_succ = _('UserLogoutMessageSucc')

        self.status_create_succ = _('StatusCreateMessageSucc')
        self.status_update_succ = _('StatusUpdateMessageSucc')
        self.status_delete_succ = _('StatusDeleteMessageSucc')

        self.tag_create_succ = _('TagCreateMessageSucc')
        self.tag_update_succ = _('TagUpdateMessageSucc')
        self.tag_delete_succ = _('TagDeleteMessageSucc')


class Buttons:
    def __init__(self):
        self.status_create_btn = _('StatusCreateBtn')
        self.tag_create_btn = _('TagCreateBtn')
