from PIL import Image

field_coord = {'Name':(190,255),'Business':(196,331),'Address':(197,700),'City':(195,760),'AccNo':(191,830)}


def super_impose(location):
    name_img = crop_image(Image.open(location + "Name.png"))
    business_img = crop_image(Image.open(location + "Business.png"))
    address_img = crop_image(Image.open(location + "Address.png"))
    city_img = crop_image(Image.open(location + "City.png"))
    accno_img = crop_image(Image.open(location + "AccNo.png"))
    background = crop_image(Image.open(location + "Form.png"))
    background.paste(name_img, field_coord['Name'], name_img)
    background.paste(business_img, field_coord['Business'], business_img)
    background.paste(address_img, field_coord['Address'], address_img)
    background.paste(city_img, field_coord['City'], city_img)
    background.paste(accno_img, field_coord['AccNo'], accno_img)
    background.save(location + 'superimposed.png',"PNG")
    return background