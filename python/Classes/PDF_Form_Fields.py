        
'''
    PDF Form Fields 
    
    Tim Santos, Rashed Karim

'''
from collections import OrderedDict
from PyPDF2 import PdfFileWriter, PdfFileReader

from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
from PIL import Image
import io

class PDF_Form_Fields:

  def __init__(self, field_dict):
    self.field_dict = field_dict
    self.name = field_dict['f_1[0]']
    self.citizenship = field_dict['f_2[0]']
    self.perm_addr = field_dict['f_3[0]']
    self.perm_city = field_dict['f_4[0]']
    self.mail_addr = field_dict['f_5[0]']
    self.mail_city = field_dict['f_6[0]']
    self.tin_us = field_dict['f_9[0]']

  def set_name(self,new):
    self.name=new
    self.field_dict['f_1[0]'] = new
    # TODO: change positioning in the field
    
  def set_citizenship(self,new):
    self.citizenship=new
    self.field_dict['f_2[0]'] = new
  def set_tin_us(self,new):
    self.tin_us=new
    self.field_dict['f_9[0]'] = new
    
  def set_name_handwritten(self,new):
    pass
  
    
  def saveform(self,outfile):
    save_new_pdf(input_pdf='fw8ben.pdf',outfile=outfile,field_dictionary=self.field_dict)
    
    
  def saveimg(self,outfile):
    save_new_pdf(input_pdf='fw8ben.pdf',outfile=outfile,field_dictionary=self.field_dict)    