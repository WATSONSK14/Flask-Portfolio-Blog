from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from models import db, User, Message

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/custom_master.html')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_superuser

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin_login'))

#User Kontrol
class UserAdmin(ModelView):
    column_list= ('username','email')
    column_filters = ('is_superuser',)
    can_create = False
    can_edit = False
    can_delete = False

#Message Kontrol
class MessageAdmin(ModelView):
    column_list = ('name', 'surname', 'email', 'subject', 'read', 'user_id')
    column_filters = ('read',)
    column_editable_list = ['read']
    form_excluded_columns = ('name','surname','email','subject','message')
    can_delete = False
    can_view_details = True
    

admin = Admin(name="Admin Panel", template_mode="bootstrap4", index_view=MyAdminIndexView())
admin.add_view(UserAdmin(User, db.session))
admin.add_view(MessageAdmin(Message, db.session))