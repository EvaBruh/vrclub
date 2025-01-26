from models.user import User, Role  # Пример модели
from sqladmin import Admin, ModelView


# Настройка модели для админки
def register_views(admin):
    class UserAdmin(ModelView, model=User):
        column_list = [User.id, User.name, User.username, User.email, User.roles]
        name = "User"
        name_plural = "Users"

    admin.add_view(UserAdmin)

    class RoleAdmin(ModelView, model=Role):
        column_list = [Role.id, Role.title, Role.description, Role.user_links, Role.users]
        name = "Role"
        name_plural = "Roles"

    admin.add_view(RoleAdmin)
