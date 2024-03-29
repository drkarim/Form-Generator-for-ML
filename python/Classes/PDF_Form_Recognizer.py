
'''
    PDF Form Recognizer 
    
    Tim Santos, Rashed Karim

'''
from collections import OrderedDict
from PyPDF2 import PdfFileWriter, PdfFileReader

from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
from PIL import Image
import io

class PDF_Form_Recognizer: 


    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file


    def _getFields(obj, tree=None, retval=None, fileobj=None):
        """
        Extracts field data if this PDF contains interactive form fields.
        The *tree* and *retval* parameters are for recursive use.

        :param fileobj: A file object (usually a text file) to write
            a report to on all interactive form fields found.
        :return: A dictionary where each key is a field name, and each
            value is a :class:`Field<PyPDF2.generic.Field>` object. By
            default, the mapping name is used for keys.
        :rtype: dict, or ``None`` if form data could not be located.
        """
        fieldAttributes = {'/FT': 'Field Type', '/Parent': 'Parent', '/T': 'Field Name', '/TU': 'Alternate Field Name',
                        '/TM': 'Mapping Name', '/Ff': 'Field Flags', '/V': 'Value', '/DV': 'Default Value'}
        if retval is None:
            retval = OrderedDict()
            catalog = obj.trailer["/Root"]
            # get the AcroForm tree
            if "/AcroForm" in catalog:
                tree = catalog["/AcroForm"]
            else:
                return None
        if tree is None:
            return retval

        obj._checkKids(tree, retval, fileobj)
        for attr in fieldAttributes:
            if attr in tree:
                # Tree is a field
                obj._buildField(tree, retval, fileobj, fieldAttributes)
                break

        if "/Fields" in tree:
            fields = tree["/Fields"]
            for f in fields:
                field = f.getObject()
                obj._buildField(field, retval, fileobj, fieldAttributes)

        return retval


    def get_form_fields():
        infile = PdfFileReader(open(self.input_file, 'rb'))
        fields = _getFields(self.input_file)
        return OrderedDict((k, v.get('/V', '')) for k, v in fields.items())


    def update_form_values(newvals=None):
        pdf = PdfFileReader(open(self.input_file, 'rb'))
        writer = PdfFileWriter()

        for i in range(pdf.getNumPages()):
            page = pdf.getPage(i)
            try:
                if newvals:
                    writer.updatePageFormFieldValues(page, newvals)
                    print(newvals)
                else:
                    writer.updatePageFormFieldValues(page,
                                                    {k: f'#{i} {k}={v}'
                                                    for i, (k, v) in enumerate(get_form_fields(infile).items())
                                                    })
                writer.addPage(page)
            except Exception as e:
                print(repr(e))
                writer.addPage(page)

        with open(outfile, 'wb') as out:
            writer.write(out)

    def set_need_appearances_writer(writer):
        # See 12.7.2 and 7.7.2 for more information:
        # http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
        try:
            catalog = writer._root_object
            # get the AcroForm tree and add "/NeedAppearances attribute
            if "/AcroForm" not in catalog:
                writer._root_object.update({
                    NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

            need_appearances = NameObject("/NeedAppearances")
            writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
            return writer

        except Exception as e:
            print('set_need_appearances_writer() catch : ', repr(e))
            return writer


    # Load form templates 
    def load_pdf_reader(infile):
        inputStream = open(self.infile, "rb")

        pdf_reader = PdfFileReader(inputStream, strict=False)
        if "/AcroForm" in pdf_reader.trailer["/Root"]:
            pdf_reader.trailer["/Root"]["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        return pdf_reader


    # Save PDF 
    def load_pdf_writer():
        
        pdf_writer = PdfFileWriter()
        set_need_appearances_writer(pdf_writer)
        if "/AcroForm" in pdf_writer._root_object:
            pdf_writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})
        return pdf_writer

    def save_new_pdf(input_pdf, 
                        outfile="out.pdf",
                        field_dictionary = {"f_1[0]": "Value1", "f_2[0]": "Value2"}):
        inputStream = open(input_pdf, "rb")
        pdf_reader = load_pdf_reader(input_pdf) 
        pdf_writer=load_pdf_writer()
        pdf_writer.addPage(pdf_reader.getPage(0))
        pdf_writer.updatePageFormFieldValues(pdf_writer.getPage(0), field_dictionary)
        outputStream = open(self.outfile, "wb")
        pdf_writer.write(outputStream)
        outputStream.close()
            
    