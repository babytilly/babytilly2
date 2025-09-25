from django.contrib import admin
from django.utils.translation import gettext_lazy
from django.db.models import OuterRef, Subquery

from commercial.models import Departament, CategoryProperties, ArticleProperties, Message


class ArticlePublishedFilter(admin.SimpleListFilter):
    title = gettext_lazy('published')
    parameter_name = 'is_published'

    def lookups(self, request, model_admin):
        return (
            ('1', gettext_lazy('Yes')),
            ('0', gettext_lazy('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            queryset = queryset.filter(articleproperties__published=True).distinct()
        elif self.value() == '0':
            queryset = queryset.filter(articleproperties__published=False).distinct()
        return queryset

class ArticleNewFilter(admin.SimpleListFilter):
    title = gettext_lazy('new')
    parameter_name = 'is_new'

    def lookups(self, request, model_admin):
        return (
            ('1', gettext_lazy('Yes')),
            ('0', gettext_lazy('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            queryset = queryset.filter(articleproperties__is_new=True).distinct()
        elif self.value() == '0':
            queryset = queryset.filter(articleproperties__is_new=False).distinct()
        return queryset


class ArticleSaleFilter(admin.SimpleListFilter):
    title = gettext_lazy('sale')
    parameter_name = 'is_special'

    def lookups(self, request, model_admin):
        return (
            ('1', gettext_lazy('Yes')),
            ('0', gettext_lazy('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            queryset = queryset.filter(articleproperties__is_special=True).distinct()
        elif self.value() == '0':
            queryset = queryset.filter(articleproperties__is_spacial=False).distinct()
        return queryset


class CategoryPublishedFilter(admin.SimpleListFilter):
    title = gettext_lazy('published')
    parameter_name = 'is_published'

    def lookups(self, request, model_admin):
        return (
            ('1', gettext_lazy('Yes')),
            ('0', gettext_lazy('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            queryset = queryset.filter(categoryproperties__published=True).distinct()
        elif self.value() == '0':
            queryset = queryset.filter(categoryproperties__published=False).distinct()
        return queryset


class DepartamentFilterMixin:
    title = gettext_lazy('departament')
    parameter_name = 'departament_id'

    def lookups(self, request, model_admin):
        return Departament.objects.all().values_list('id', 'country')

class CategoryDepartamentFilter(DepartamentFilterMixin, admin.SimpleListFilter):

    def queryset(self, request, queryset):
        if self.value():
            category_id_list = CategoryProperties.objects.filter(departament_id=self.value()).values_list('category_id', flat=True).distinct()
            queryset = queryset.filter(id__in=category_id_list)
        return queryset


class ArticleDepartamentFilter(DepartamentFilterMixin, admin.SimpleListFilter):
    def queryset(self, request, queryset):
        if self.value():
            article_id_list = ArticleProperties.objects.filter(departament_id=self.value()).values_list('article_id', flat=True).distinct()
            queryset = queryset.filter(id__in=article_id_list)
        return queryset


class ComplaintHasAnswerFilter(admin.SimpleListFilter):
    title = gettext_lazy('has answer')
    parameter_name = 'has_answer'

    def lookups(self, request, model_admin):
        return (
            ('1', gettext_lazy('Yes')),
            ('0', gettext_lazy('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            # Filter complaints that have an answer (last message from staff)
            # Get the latest message for each complaint and check if it's from staff
            latest_message_is_staff = Subquery(
                Message.objects.filter(
                    complaint=OuterRef('pk')
                ).order_by('-created_date').values('user__is_staff')[:1]
            )
            
            queryset = queryset.annotate(
                latest_message_is_staff=latest_message_is_staff
            ).filter(latest_message_is_staff=True)
            
        elif self.value() == '0':
            # Filter complaints that don't have an answer (last message not from staff or no messages)
            latest_message_is_staff = Subquery(
                Message.objects.filter(
                    complaint=OuterRef('pk')
                ).order_by('-created_date').values('user__is_staff')[:1]
            )
            
            queryset = queryset.annotate(
                latest_message_is_staff=latest_message_is_staff
            ).filter(latest_message_is_staff__in=[False, None])
            
        return queryset