from django.db import models
from django import forms

class Type(models.Model):
    type_choices = (
        ('COFFEE', 'Coffee'),
        ('TEA', 'Tea'),
    )

    menu_type = models.CharField(max_length=200, choices=type_choices) 

    def __str__(self):
        return self.menu_type

class Menu(models.Model):
    menu_type = models.ForeignKey(Type, on_delete=models.CASCADE) 
    menu_text = models.CharField(max_length=200)
    size_text = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "%s, %s, %s, %s" % (self.menu_type, self.menu_text, self.size_text, self.price)

# class Size(models.Model):
#     size_choices = (
#         ('TALL', 'Tall'),
#         ('GRANDE', 'Grande'),
#         ('VENTI', 'Venti'),
#     )

#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     size_text = models.CharField(max_length=200, choices=size_choices)
#     price = models.DecimalField(max_digits=6, decimal_places=2)

#     def __str__(self):
#         return "%s, %s, %s" % (self.menu.menu_text, self.size_text, self.price)

class Orders(models.Model):
    # size = models.ForeignKey(Size, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.menu.menu_text, self.menu.size_text, self.menu.price, self.order, self.order_date)

