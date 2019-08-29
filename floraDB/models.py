from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Main_Product_List(models.Model):
  selection = models.BooleanField()
  code = models.CharField(max_length=50)
  description = models.CharField(max_length=50)
  piecework_price = models.DecimalField(max_digits=5, decimal_places=4)
  unit = models.CharField(max_length=50)
  group = models.CharField(max_length=50)
  user_T1_carton = models.CharField(max_length=24)
  sp_code = models.CharField(max_length=25)
  weight = models.FloatField()
  picture_SQ = models.BooleanField()  # = models.CharField(max_length=  
  picture_OB = models.BooleanField()
  poly_bags = models.IntegerField()
  sel_for_summary = models.BooleanField()
  unit_type = models.CharField(max_length=50)
  sub_group = models.CharField(max_length=50)
  price_list = models.BooleanField()
  poly_bag_type = models.CharField(max_length=50)
  price_list_sel_2 = models.BooleanField()
  pw_increased_price = models.DecimalField(max_digits=5, decimal_places=4)
  color = models.CharField(max_length=50)
  sub_carton = models.CharField(max_length=50)
  sub_carton_qty = models.FloatField()
  num_sub_cartons = models.IntegerField()
  pw_desc = models.CharField(max_length=50)
  has_pic = models.BooleanField()
  pw_group = models.CharField(max_length=50)
  spare1 = models.CharField(max_length=50)
  spare2 = models.CharField(max_length=50)
  date_added = models.DateTimeField(default=timezone.now)
  sub_ctn_type = models.CharField(max_length=50)
  tariffcode = models.CharField(max_length=50)
  header_card_type = models.CharField(max_length=255)
  EAN_outer = models.CharField(max_length=255)
  EAN_inner1 = models.CharField(max_length=255)
  EAN_inner2 = models.CharField(max_length=255)
  EAN_inner3 = models.CharField(max_length=255)
  EAN_inner4 = models.CharField(max_length=255)
  
  def publish(self):
  	self.date_added = timezone.now()
  	self.save()
 
  def __str__(self):
  	return self.code
 
class Unit_Code(models.Model):
  unit_code = models.CharField(max_length=100)
  description = models.CharField(max_length=50)
  picture = models.BooleanField()
  customs_group = models.CharField(max_length=50)
  sel = models.BooleanField()
  stock_value = models.DecimalField(max_digits=5, decimal_places=2)
  botanical_name = models.CharField(max_length=50)
  sub_group = models.CharField(max_length=50)
  sub_item_code = models.CharField(max_length=50)
  check_for_pr_summary = models.BooleanField()
  waste_perc = models.IntegerField()
  selling_price = models.DecimalField(max_digits=5, decimal_places=4)
  german_name = models.CharField(max_length=50)
  bleaching_waste_perc = models.DecimalField(max_digits=5, decimal_places=4)
  item_bleached = models.CharField(max_length=50)
  photo = models.CharField(max_length=255) #in Access, this is OLE Object
  item_type = models.CharField(max_length=50)
  color = models.CharField(max_length=50)
  order = models.CharField(max_length=50)
  pic = models.CharField(max_length=255) #in Access, this is OLE Object
  tcode = models.CharField(max_length=50) #Tariff Code
  
  def publish(self):
  	self.save()
  	
  def __str__(self):
  	return self.unit_code + ' ' + self.description

