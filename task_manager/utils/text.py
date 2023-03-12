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

        self.label_create = _('LabelCreateTitle')
        self.labels_list = _('LabelsListTitle')
        self.label_update = _('LabelUpdateTitle')
        self.label_delete = _('LabelDeleteTitle')

        self.task_create = _('TaskCreateTitle')
        self.tasks_list = _('TasksListTitle')
        self.task_update = _('TaskUpdateTitle')
        self.task_delete = _('TaskDeleteTitle')


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
        self.status_delete_err = _('StatusDeleteMessageErr')

        self.label_create_succ = _('CreateMessageSucc')
        self.label_update_succ = _('LabelUpdateMessageSucc')
        self.label_delete_succ = _('LabelDeleteMessageSucc')
        self.label_delete_err = _('LabelDeleteMessageErr')

        self.task_create_succ = _('TaskCreateMessageSucc')
        self.task_update_succ = _('TaskUpdateMessageSucc')
        self.task_delete_succ = _('TaskDeleteMessageSucc')
        self.task_delete_err = _('TaskDeleteMessageErr')


class Buttons:
    def __init__(self):
        self.status_create_btn = _('StatusCreateBtn')
        self.label_create_btn = _('LabelCreateBtn')
        self.task_create_btn = _('TaskCreateBtn')
        self.user_create_btn = _('UserCreateBtn')


class FormFields:
    def __init__(self):
        self.user_create_first_name = _('UserCreateFormFirstName')
        self.user_create_last_name = _('UserCreateFormLastName')

        self.status_create_name = _('StatusCreateFormName')

        self.label_create_name = _('LabelCreateFormName')
        self.label_create_color = _('LabelCreateFormColor')

        self.task_create_name = _('TaskCreateFormName')
        self.task_create_description = _('TaskCreateFormDescription')
        self.task_create_executor = _('TaskCreateFormExecutor')
        self.task_create_status = _('TaskCreateFormStatus')
        self.task_create_labels = _('TaskCreateFormLabels')
        self.tasks_filter_status = _('TasksFilterStatus')
        self.tasks_filter_executor = _('TasksFilterExecutor')
        self.tasks_filter_labels = _('TasksFilterLabels')
        self.tasks_filter_self_tasks = _('TasksFilterSelfTasks')


class Colors:
    def __init__(self):
        self.red = _('Red')
        self.green = _('Green')
        self.blue = _('Blue')
        self.gray = _('Gray')
