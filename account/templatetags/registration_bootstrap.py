# coding=utf-8
from django import template
signup = template.Library()

@signup.filter()
def add_class(field, css):
   return field.as_widget(attrs={"class":css})
