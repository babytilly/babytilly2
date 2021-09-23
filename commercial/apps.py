from django.apps import AppConfig
from django.contrib import admin
from django.contrib.auth import get_user_model


class CommercialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'commercial'

    def ready(self):
        from .admin import (
            DepartamentAdmin, CategoryAdmin, UserAdmin, ImportPriceAdmin, ArticleAdmin, OrderAdmin, StartPageAdmin
        )

        Departament = self.get_model('Departament')
        Category = self.get_model('Category')
        Article = self.get_model('Article')
        ImportPrice = self.get_model('ImportPrice')
        Order = self.get_model('Order')
        StartPage = self.get_model('StartPage')
        User = get_user_model()

        admin.site.unregister(User)

        admin.site.register(Departament, DepartamentAdmin)
        admin.site.register(Category, CategoryAdmin)
        admin.site.register(Article, ArticleAdmin)
        admin.site.register(User, UserAdmin)
        admin.site.register(ImportPrice, ImportPriceAdmin)
        admin.site.register(Order, OrderAdmin)
        admin.site.register(StartPage, StartPageAdmin)
