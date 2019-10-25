# -*- coding: utf-8 -*-

from faker import Faker
import pandas as pd




def GenerateData(size, locale):
    fake = Faker(locale)
    gen = Faker()  
    name = []
    bname = []
    tax = []
    instructions = []
    exemptions = []
    exemptionCode = []
    address = []
    city = []
    requester = []
    account = []
    social =[]
    empid = []
    #classif = []
    for i in range(size):
        name.append('- ')
        bname.append(fake.name())
        tax.append('Individual/sole proprietor or single-member LLC')
        #classif.append(' -')
        instructions.append(' -')
        exemptions.append(' -')        
        exemptionCode.append('- ')
        address.append('- ')
        city.append(fake.street_address().replace('\n', ' '))
        requester.append(fake.city()+ ' ' + fake.postcode())
        account.append('- ')
        social.append(fake.bban())
        empid.append(gen.itin())
        load= {'Name':name,'BussinesName':bname, 'Tax':tax,
       'Instructions':instructions, 'Exemptions':exemptions, 'ExemptionCode':exemptionCode, 'Address':address,
       'City':city, 'Requester':requester,'Account':account,'SocialSeciurityNumber':social, 'EmpIdentificationNumber':empid}  
    df = pd.DataFrame(data=load)
    return df



