from tkinter import *
import csv
import math

master = Tk()

with open('business_data_record.csv', 'w', newline='') as csvfile:
    new_file_writer = csv.writer(csvfile)
    fields = ['CENT_X', 'CENT_Y', 'BusinessID', 'Name', 'StreetNumber', 'StreetName', 'UnitNumber',\
              'PostalCode', 'Location', 'Ward', 'NAICSSector', 'EmployeeRange', 'Phone', 'Fax',\
              'Email', 'WebAddress']
    new_file_writer.writerow(fields)




class add_business(Frame):
    def __init__(self):
        super().__init__()

        self.master.columnconfigure(2, weight=1)

        # FOCUSOUT VALIDATION:

        def longitude_error(event):
            if longitude_var.get() == '':
                longitude_label.config(fg='white', bg='red')
                longitude_entry.config(fg='white', bg='red')
                longitude_message.config(bg='red', fg='white')
                longitude_message.config(text="Please fill entry.")
            elif math.ceil(float(longitude_var.get())) not in range(-179,181) and (float(longitude_var.get()) != -180):
                longitude_label.config(fg='white', bg='red')
                longitude_entry.config(fg='white', bg='red')
                longitude_message.config(bg='red', fg='white')
                longitude_message.config(text= "Longitude must be between -180.00 and 180.00")
            elif '.' not in str(longitude_var.get()):
                longitude_label.config(fg='white', bg='red')
                longitude_entry.config(fg='white', bg='red')
                longitude_message.config(bg='red', fg='white')
                longitude_message.config(text="Longitude must be a decimal number rounded to 2 to 4 decimal degrees.")
            elif len(str(longitude_var.get()[str(longitude_var.get()).index('.')+1:])) < 2 or len(str(longitude_var.get()[str(longitude_var.get()).index('.')+1:])) > 4:
                longitude_label.config(fg='white', bg='red')
                longitude_entry.config(fg='white', bg='red')
                longitude_message.config(bg='red', fg='white')
                longitude_message.config(text="Longitude must be rounded to 2 to 4 decimal degrees.")
            else:
                longitude_label.config(fg='black', bg='#90ee90')
                longitude_entry.config(fg='black', bg='#90ee90')
                longitude_message.config(bg='#90ee90', fg='#90ee90')

        def latitude_error(event):
            if latitude_var.get() == '':
                latitude_label.config(fg='white', bg='red')
                latitude_entry.config(fg='white', bg='red')
                latitude_message.config(bg='red', fg='white')
                latitude_message.config(text="Please fill entry.")
            elif math.ceil(float(latitude_var.get())) not in range(-179,181) and (float(latitude_var.get()) != -180):
                latitude_label.config(fg='white', bg='red')
                latitude_entry.config(fg='white', bg='red')
                latitude_message.config(bg='red', fg='white')
                latitude_message.config(text= "Latitude must be between -180.00 and 180.00")
            elif '.' not in str(latitude_var.get()):
                latitude_label.config(fg='white', bg='red')
                latitude_entry.config(fg='white', bg='red')
                latitude_message.config(bg='red', fg='white')
                latitude_message.config(text="Latitude must be a decimal number rounded to 2 to 4 decimal degrees.")
            elif len(str(latitude_var.get()[str(latitude_var.get()).index('.') + 1:])) < 2 or len(
                    str(latitude_var.get()[str(latitude_var.get()).index('.') + 1:])) > 4:
                latitude_label.config(fg='white', bg='red')
                latitude_entry.config(fg='white', bg='red')
                latitude_message.config(bg='red', fg='white')
                latitude_message.config(text="Latitude must be rounded to 2 to 4 decimal degrees.")
            else:
                latitude_label.config(fg='black', bg='#90ee90')
                latitude_entry.config(fg='black', bg='#90ee90')
                latitude_message.config(bg='#90ee90', fg='#90ee90')

        def id_error(event):
            if id_var.get() == '':
                id_label.config(fg='white', bg='red')
                id_entry.config(fg='white', bg='red')
                id_message.config(bg='red', fg='white')
                id_message.config(text="Please fill entry.")
            elif len(id_var.get()) < 4:
                id_label.config(fg='white', bg='red')
                id_entry.config(fg='white', bg='red')
                id_message.config(bg='red', fg='white')
                id_message.config(text="Please enter a valid 4-5 digit business ID.")
            else:
                id_label.config(fg='black', bg='#90ee90')
                id_entry.config(fg='black', bg='#90ee90')
                id_message.config(bg='#90ee90', fg='#90ee90')

        def name_error(event):
            if str(name_var.get()).strip() == '':
                name_label.config(fg='white', bg='red')
                name_entry.config(fg='white', bg='red')
                name_message.config(bg='red', fg='white')
                name_message.config(text="Please fill entry.")
            else:
                name_label.config(fg='black', bg='#90ee90')
                name_entry.config(fg='black', bg='#90ee90')
                name_message.config(bg='#90ee90', fg='#90ee90')


        def street_number_error(event):
            if street_num_var.get() == '':
                street_number_label.config(fg='white', bg='red')
                street_number_entry.config(fg='white', bg='red')
                street_number_message.config(bg='red', fg='white')
                street_number_message.config(text="Please fill entry.")
            else:
                street_number_label.config(fg='black', bg='#90ee90')
                street_number_entry.config(fg='black', bg='#90ee90')
                street_number_message.config(bg='#90ee90', fg='#90ee90')

        def street_name_error(event):
            if str(street_name_var.get()).strip() == '':
                street_name_label.config(fg='white', bg='red')
                street_name_entry.config(fg='white', bg='red')
                street_name_message.config(bg='red', fg='white')
                street_name_message.config(text="Please fill entry.")
            else:
                street_name_label.config(fg='black', bg='#90ee90')
                street_name_entry.config(fg='black', bg='#90ee90')
                street_name_message.config(bg='#90ee90', fg='#90ee90')

        def unit_number_error(event):
            if unit_num_var.get() == '':
                unit_number_label.config(fg='white', bg='red')
                unit_number_entry.config(fg='white', bg='red')
                unit_number_message.config(bg='red', fg='white')
                unit_number_message.config(text="Please fill entry.")
            else:
                unit_number_label.config(fg='black', bg='#90ee90')
                unit_number_entry.config(fg='black', bg='#90ee90')
                unit_number_message.config(bg='#90ee90', fg='#90ee90')

        def postal_code_error(event):
            if postal_code_var.get() == '':
                postal_code_label.config(fg='white', bg='red')
                postal_code_entry.config(fg='white', bg='red')
                postal_code_message.config(bg='red', fg='white')
                postal_code_message.config(text="Please fill entry.")
            elif len(postal_code_var.get()) < 6:
                postal_code_label.config(fg='white', bg='red')
                postal_code_entry.config(fg='white', bg='red')
                postal_code_message.config(bg='red', fg='white')
                postal_code_message.config(text="Please enter a valid postal code with format 'A0A0A0'.")
            else:
                postal_code_label.config(fg='black', bg='#90ee90')
                postal_code_entry.config(fg='black', bg='#90ee90')
                postal_code_message.config(bg='#90ee90', fg='#90ee90')

        def location_error(event):
            if location_var.get() == '':
                location_label.config(fg='white', bg='red')
                location_entry.config(fg='white', bg='red')
                location_message.config(bg='red', fg='white')
                location_message.config(text="Please fill entry.")
            else:
                location_label.config(fg='black', bg='#90ee90')
                location_entry.config(fg='black', bg='#90ee90')
                location_message.config(bg='#90ee90', fg='#90ee90')

        def ward_error(event):
            if ward_var.get() == '':
                ward_label.config(fg='white', bg='red')
                ward_entry.config(fg='white', bg='red')
                ward_message.config(bg='red', fg='white')
                ward_message.config(text="Please fill entry.")
            else:
                ward_label.config(fg='black', bg='#90ee90')
                ward_entry.config(fg='black', bg='#90ee90')
                ward_message.config(bg='#90ee90', fg='#90ee90')

        def naics_sector_error(event):
            if naics_var.get() == '':
                naics_sector_label.config(fg='white', bg='red')
                naics_sector_entry.config(fg='white', bg='red')
                naics_message.config(bg='red', fg='white')
                naics_message.config(text="Please fill entry.")
            else:
                naics_sector_label.config(fg='black', bg='#90ee90')
                naics_sector_entry.config(fg='black', bg='#90ee90')
                naics_message.config(bg='#90ee90', fg='#90ee90')

        def employee_range_error(event):
            if employee_range_var.get() == '':
                employee_range_label.config(fg='white', bg='red')
                employee_range_entry.config(fg='white', bg='red')
                employee_range_message.config(bg='red', fg='white')
                employee_range_message.config(text="Please fill entry.")
            elif '-' not in str(employee_range_var.get()):
                employee_range_label.config(fg='white', bg='red')
                employee_range_entry.config(fg='white', bg='red')
                employee_range_message.config(bg='red', fg='white')
                employee_range_message.config(text="Please enter a range of two numbers using '-'.")
            elif not str(employee_range_var.get())[0].isdigit() or not str(employee_range_var.get())[-1].isdigit():
                employee_range_label.config(fg='white', bg='red')
                employee_range_entry.config(fg='white', bg='red')
                employee_range_message.config(bg='red', fg='white')
                employee_range_message.config(text="Please enter two numbers with a '-' between them.")
            else:
                employee_range_label.config(fg='black', bg='#90ee90')
                employee_range_entry.config(fg='black', bg='#90ee90')
                employee_range_message.config(bg='#90ee90', fg='#90ee90')

        def phone_error(event):
            if phone_var.get() == '':
                phone_label.config(fg='white', bg='red')
                phone_entry.config(fg='white', bg='red')
                phone_message.config(bg='red', fg='white')
                phone_message.config(text="Please fill entry.")
            elif int(phone_var.get()) < 1000000000:
                phone_label.config(fg='white', bg='red')
                phone_entry.config(fg='white', bg='red')
                phone_message.config(bg='red', fg='white')
                phone_message.config(text="Please enter a valid 10 or 11 digit phone number.")
            else:
                phone_label.config(fg='black', bg='#90ee90')
                phone_entry.config(fg='black', bg='#90ee90')
                phone_message.config(bg='#90ee90', fg='#90ee90')

        def fax_number_error(event):
            if fax_var.get() == '':
                fax_number_label.config(fg='white', bg='red')
                fax_number_entry.config(fg='white', bg='red')
                fax_number_message.config(bg='red', fg='white')
                fax_number_message.config(text="Please fill entry.")
            elif int(fax_var.get()) < 1000000000:
                fax_number_label.config(fg='white', bg='red')
                fax_number_entry.config(fg='white', bg='red')
                fax_number_message.config(bg='red', fg='white')
                fax_number_message.config(text="Please enter a valid 10 or 11 digit fax number.")
            else:
                fax_number_label.config(fg='black', bg='#90ee90')
                fax_number_entry.config(fg='black', bg='#90ee90')
                fax_number_message.config(bg='#90ee90', fg='#90ee90')

        def email_error(event):                                                                     # email entry must not be empty
            if email_var.get() == '':
                email_label.config(fg='white', bg='red')
                email_entry.config(fg='white', bg='red')
                email_message.config(bg='red', fg='white')
                email_message.config(text="Please fill entry.")
            elif '@' not in str(email_var.get()) or '.' not in str(email_var.get()):                # email must have @ and .
                email_label.config(fg='white', bg='red')
                email_entry.config(fg='white', bg='red')
                email_message.config(bg='red', fg='white')
                email_message.config(text="Please enter a valid email address.")
            elif not str(email_var.get())[0].isalpha() and not str(email_var.get())[0].isdigit():   # first digit of entry must not be a special character
                email_label.config(fg='white', bg='red')
                email_entry.config(fg='white', bg='red')
                email_message.config(bg='red', fg='white')
                email_message.config(text="Please enter a valid email address.")
            elif not str(email_var.get())[-1].isalpha():                                            # last character of email address must be a letter
                email_label.config(fg='white', bg='red')
                email_entry.config(fg='white', bg='red')
                email_message.config(bg='red', fg='white')
                email_message.config(text="Please enter a valid email address.")
            elif '.' not in str(email_var.get())[str(email_var.get()).index('@')+1:]:               # there must be a . after @ in the entry
                email_label.config(fg='white', bg='red')
                email_entry.config(fg='white', bg='red')
                email_message.config(bg='red', fg='white')
                email_message.config(text="Please enter a valid email address.")
            else:
                email_label.config(fg='black', bg='#90ee90')
                email_entry.config(fg='black', bg='#90ee90')
                email_message.config(bg='#90ee90', fg='#90ee90')

        def url_error(event):
            if url_var.get() == '':                                                                                 # URL entry must not be empty
                url_label.config(fg='white', bg='red')
                url_entry.config(fg='white', bg='red')
                url_message.config(bg='red', fg='white')
                url_message.config(text="Please fill entry.")
            elif str(url_var.get())[0:7] != 'http://':                                                              # URL must begin with 'http://'
                url_label.config(fg='white', bg='red')
                url_entry.config(fg='white', bg='red')
                url_message.config(bg='red', fg='white')
                url_message.config(text="Web Address must begin with 'http://' followed by website name.")
            elif len(str(url_var.get())) < 8:                                                                       # there is no valid url that has one character after 'http://'
                url_label.config(fg='white', bg='red')
                url_entry.config(fg='white', bg='red')
                url_message.config(bg='red', fg='white')
                url_message.config(text="Please enter a valid web address.")
            elif not str(url_var.get())[7].isalpha() and not str(url_var.get())[7].isdigit():                       # first digit after 'http://' must be numeric or a letter
                url_label.config(fg='white', bg='red')
                url_entry.config(fg='white', bg='red')
                url_message.config(bg='red', fg='white')
                url_message.config(text="Website name must begin with a letter or number.")
            elif '.' not in str(url_var.get()):                                                                     # URL must have a period
                url_label.config(fg='white', bg='red')
                url_entry.config(fg='white', bg='red')
                url_message.config(bg='red', fg='white')
                url_message.config(text="Please enter a valid web address.")
            elif '/' in str(url_var.get())[7:str(url_var.get()).index('.')]:                                        # '/' must not precede '.' in URL
                url_label.config(fg='white', bg='red')
                url_entry.config(fg='white', bg='red')
                url_message.config(bg='red', fg='white')
                url_message.config(text="'/' cannot precede '.' in a web address.'")
            elif not str(url_var.get())[-1].isalpha() and not str(url_var.get())[-1].isdigit() and str(url_var.get())[-1] != '/':   # last character in url must be a letter, number, or '/'
                url_label.config(fg='white', bg='red')
                url_entry.config(fg='white', bg='red')
                url_message.config(bg='red', fg='white')
                url_message.config(text="Please enter a valid web address.")
            else:
                url_label.config(fg='black', bg='#90ee90')
                url_entry.config(fg='black', bg='#90ee90')
                url_message.config(bg='#90ee90', fg='#90ee90')

        # VALIDATIONS WITHIN ENTRIES (CALLBACKS)

        def longitude_v1(input, accepted):
            if (input == ''):
                return True
            elif input.isdigit():
                return True
            elif (input == '.'):
                if not '.' in accepted[:-1]:
                    return True
                else:
                    return False
            elif (input == '-'):
                if len(accepted) <= 1:
                    return True
                else:
                    return False
            else:
                return False


        def id_v1(input):
            if (input == ''):
                return True
            elif input.isdigit() and (len(input) <= 5):
                return True
            else:
                return False

        def name_v1(input):
            if (input == ''):
                return True
            elif input.isalpha() or input.isdigit():
                return True
            elif input in '! \' "  #  $  %  &  ’  (  )  *  +  ,  –  .  /  :  ;  >  =  <  ?  [  ]  \  ^  `  ´ ¸ @':
                return True
            else:
                return False

        def street_num_v1(input):
            return input.isdigit()

        def street_name_v1(input):
            if (input == ''):
                return True
            elif input.isalpha() or input.isdigit():
                return True
            elif input in " - ' () ":
                return True
            else:
                return False

        def postal_code_v1(input):
            if (input == ''):
                return True
            elif len(input) > 6:
                return False
            elif len(input) == 1:
                if input.isalpha():
                    return True
                else:
                    return False
            elif len(input) == 2:
                if input[-1].isdigit():
                    return True
                else:
                    return False
            elif len(input) == 3:
                if input[-1].isalpha():
                    return True
                else:
                    return False
            elif len(input) == 4:
                if input[-1].isdigit():
                    return True
                else:
                    return False
            elif len(input) == 5:
                if input[-1].isalpha():
                    return True
                else:
                    return False
            elif len(input) == 6:
                if input[-1].isdigit():
                    return True
                else:
                    return False
            return True

        def ward_v1(input):
            if (input == ''):
                return True
            elif input.isdigit() and (int(input) <= 11):
                return True
            else:
                return False

        def naics_v1(input):
            if (input == ''):
                return True
            elif input.isalpha():
                return True
            elif input in " , ( ) ":
                return True
            else:
                return False

        def employee_range_v1(input, accepted):
            if (input == ''):
                return True
            elif input.isdigit():
                return True
            elif input == '-':
                if not '-' in accepted[:-1]:
                    return True
                else:
                    return False
            else:
                return False

        def phone_v1(input):
            if (input == ''):
                return True
            elif input.isdigit() and (int(input) < 20000000000):
                return True
            else:
                return False

        def email_v1(input, accepted):                      # email addresses containing the characters A-Z and numbers
            if (input == ''):                               # 0-9, and special characters '.', '-', '_', '@' are
                return True                                 # are accepted under the following conditions:
            elif input.isalpha() or input.isdigit():        #
                return True                                 # 1. there is a single '@' in the address
            elif input in ['.', '-']:                       # 2. there is no '_' in the domain name or top level domain
                if len(accepted) > 1:
                    if accepted[-2] in ['.', '-']:              #    (after the '@')
                        return False                            # 3. entries cannot have consecutive periods/dashes
                    else:
                        return True
                else:
                    return False
            elif (input == '@') or (input == '_'):
                if not '@' in accepted[:-1]:
                    return True
                else:
                    return False
            else:
                return False

        def url_v1(input, accepted):
            if (input == ''):
                return True
            elif input.isalpha() or input.isdigit():
                return True
            elif input in ['!', '*', "'", '(', ')',	';', ':', '@', '&',	'=', '+', '$', '/', '?', '#', '[',	']']:
                return True
            elif (input == '.'):
                if len(accepted) > 9:
                    if (accepted[-2] == '.'):
                        return False
                    else:
                        return True
                else:
                    return False
            else:
                return False

        # INVALID COMMANDS

        def longitude_invalid():
            longitude_message.config(text='Please enter a number in range (-180,180) rounded two to four decimals.',
                                     fg='blue')

        def latitude_invalid():
            latitude_message.config(text='Please enter a number in range (-180,180) rounded two to four decimals.',
                                     fg='blue')

        def id_invalid():
            id_message.config(text='Please enter a 4-5 digit number.',
                                     fg='blue')
        def street_num_invalid():
            street_number_message.config(text='This entry only accepts numbers', fg='blue')

        def ward_invalid():
            ward_message.config(text='This entry only accepts numbers', fg='blue')

        def employee_range_invalid():
            employee_range_message.config(text='This entry only accepts numbers', fg='blue')

        def phone_invalid():
            phone_message.config(text='This entry only accepts numbers', fg='blue')

        def fax_number_invalid():
            fax_number_message.config(text='This entry only accepts numbers', fg='blue')

        # VALIDATE COMMANDS:

        long_vcmd = master.register(longitude_v1)
        id_vcmd = master.register(id_v1)
        name_vcmd = master.register(name_v1)
        street_num_vcmd = master.register(street_num_v1)
        street_name_vcmd = master.register(street_name_v1)
        postal_code_vcmd = master.register(postal_code_v1)
        ward_vcmd = master.register(ward_v1)
        naics_vcmd= master.register(naics_v1)
        employee_range_vcmd = master.register(employee_range_v1)
        phone_vcmd = master.register(phone_v1)
        email_vcmd = master.register(email_v1)
        url_vcmd = master.register(url_v1)

        # ENTRIES:

        longitude_var = StringVar()
        longitude_entry = Entry(textvariable=longitude_var, validate='key', validatecommand=(long_vcmd, '%S', '%P'),
                                invalidcommand=longitude_invalid)
        longitude_entry.grid(column=1, row=0, sticky='nse', pady=(10, 0))
        longitude_entry.bind('<FocusOut>', longitude_error)

        latitude_var = StringVar()
        latitude_entry = Entry(textvariable=latitude_var, validate='key', validatecommand=(long_vcmd, '%S', '%P'),
                               invalidcommand=latitude_invalid)
        latitude_entry.grid(column=1, row=1, sticky='nse')
        latitude_entry.bind('<FocusOut>', latitude_error)

        id_var = StringVar()
        id_entry = Entry(textvariable=id_var, validate='key', validatecommand=(id_vcmd, '%P'),
                         invalidcommand=id_invalid)
        id_entry.grid(column=1, row=2, sticky='nse')
        id_entry.bind('<FocusOut>', id_error)

        name_var = StringVar()
        name_entry = Entry(textvariable=name_var, validate='key', validatecommand=(name_vcmd, '%S'))
        name_entry.grid(column=1, row=3, sticky='nse')
        name_entry.bind('<FocusOut>', name_error)

        street_num_var = StringVar()
        street_number_entry = Entry(textvariable=street_num_var, validate='key', validatecommand=(street_num_vcmd, '%S'),
                                    invalidcommand=street_num_invalid)
        street_number_entry.grid(column=1, row=4, sticky='nse')
        street_number_entry.bind('<FocusOut>', street_number_error)

        street_name_var = StringVar()
        street_name_entry = Entry(textvariable=street_name_var, validate='key', validatecommand=(street_name_vcmd, '%S'))
        street_name_entry.grid(column=1, row=5, sticky='nse')
        street_name_entry.bind('<FocusOut>', street_name_error)

        unit_num_var = StringVar()
        unit_number_entry = Entry(textvariable=unit_num_var, validate='key', validatecommand=(street_name_vcmd, '%S'))
        unit_number_entry.grid(column=1, row=6, sticky='nse')
        unit_number_entry.bind('<FocusOut>', unit_number_error)

        postal_code_var = StringVar()
        postal_code_entry = Entry(textvariable=postal_code_var, validate='key', validatecommand=(postal_code_vcmd, '%P'))
        postal_code_entry.grid(column=1, row=7, sticky='nse')
        postal_code_entry.bind('<FocusOut>', postal_code_error)

        location_var = StringVar()
        location_entry = Entry(textvariable=location_var, validate='key', validatecommand=(street_name_vcmd, '%S'))
        location_entry.grid(column=1, row=8, sticky='nse')
        location_entry.bind('<FocusOut>', location_error)

        ward_var = StringVar()
        ward_entry = Entry(textvariable=ward_var, validate='key', validatecommand=(ward_vcmd, '%P'),
                           invalidcommand=ward_invalid)
        ward_entry.grid(column=1, row=9, sticky='nse')
        ward_entry.bind('<FocusOut>', ward_error)

        naics_var = StringVar()
        naics_sector_entry = Entry(textvariable=naics_var, validate='key', validatecommand=(naics_vcmd, '%S'))
        naics_sector_entry.grid(column=1, row=10, sticky='nse')
        naics_sector_entry.bind('<FocusOut>', naics_sector_error)

        employee_range_var = StringVar()
        employee_range_entry = Entry(textvariable=employee_range_var, validate='key', validatecommand=(employee_range_vcmd, '%S', '%P'),
                                     invalidcommand=employee_range_invalid)
        employee_range_entry.grid(column=1, row=11, sticky='nse')
        employee_range_entry.bind('<FocusOut>', employee_range_error)

        phone_var = StringVar()
        phone_entry = Entry(textvariable=phone_var, validate='key', validatecommand=(phone_vcmd, '%P'),
                            invalidcommand=phone_invalid)
        phone_entry.grid(column=1, row=12, sticky='nse')
        phone_entry.bind('<FocusOut>', phone_error)

        fax_var = StringVar()
        fax_number_entry = Entry(textvariable=fax_var, validate='key', validatecommand=(phone_vcmd, '%P'),
                                 invalidcommand=fax_number_invalid)
        fax_number_entry.grid(column=1, row=13, sticky='nse')
        fax_number_entry.bind('<FocusOut>', fax_number_error)

        email_var = StringVar()
        email_entry = Entry(textvariable=email_var, validate='key', validatecommand=(email_vcmd, '%S', '%P'))
        email_entry.grid(column=1, row=14, sticky='nse')
        email_entry.bind('<FocusOut>', email_error)

        url_var = StringVar()
        url_entry = Entry(textvariable=url_var, validate='key', validatecommand=(url_vcmd, '%S', '%P'))
        url_entry.grid(column=1, row=15, sticky='nse', pady=(0,10))
        url_entry.bind('<FocusOut>', url_error)

        # LABELS:

        longitude_label = Label(text='GPS Longitude:')
        longitude_label.grid(column=0, row=0, sticky='w', pady=(11,0))

        latitude_label = Label(text='GPS Latitude:')
        latitude_label.grid(column=0, row=1, sticky='w')

        id_label = Label(text='Business ID:')
        id_label.grid(column=0, row=2, sticky='w')

        name_label = Label(text='Business Name:')
        name_label.grid(column=0, row=3, sticky='w')

        street_number_label = Label(text='Street Number')
        street_number_label.grid(column=0, row=4, sticky='w')

        street_name_label = Label(text='Street Name:')
        street_name_label.grid(column=0, row=5, sticky='w')

        unit_number_label = Label(text='Unit Number:')
        unit_number_label.grid(column=0, row=6, sticky='w')

        postal_code_label = Label(text='Postal Code:')
        postal_code_label.grid(column=0, row=7, sticky='w')

        location_label = Label(text='Location:')
        location_label.grid(column=0, row=8, sticky='w')

        ward_label = Label(text='Ward:')
        ward_label.grid(column=0, row=9, sticky='w')

        naics_sector_label = Label(text='NAICS Sector:')
        naics_sector_label.grid(column=0, row=10, sticky='w')

        employee_range_label = Label(text='Employee Range:')
        employee_range_label.grid(column=0, row=11, sticky='w')

        phone_label = Label(text='Phone Number:')
        phone_label.grid(column=0, row=12, sticky='w')

        fax_number_label = Label(text='Fax Number:')
        fax_number_label.grid(column=0, row=13, sticky='w')

        email_label = Label(text='Email Address:')
        email_label.grid(column=0, row=14, sticky='w')

        url_label = Label(text='URL:')
        url_label.grid(column=0, row=15, sticky='w', pady=(0,10))

        # ERROR LABELS:

        longitude_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        longitude_message.grid(column=2, row=0, pady=(11, 0))

        latitude_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        latitude_message.grid(column=2, row=1)

        id_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        id_message.grid(column=2, row=2)

        name_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        name_message.grid(column=2, row=3)

        street_number_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        street_number_message.grid(column=2, row=4)

        street_name_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        street_name_message.grid(column=2, row=5)

        unit_number_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        unit_number_message.grid(column=2, row=6)

        postal_code_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        postal_code_message.grid(column=2, row=7)

        location_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        location_message.grid(column=2, row=8)

        ward_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        ward_message.grid(column=2, row=9)

        naics_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        naics_message.grid(column=2, row=10)

        employee_range_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        employee_range_message.grid(column=2, row=11)

        phone_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        phone_message.grid(column=2, row=12)

        fax_number_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        fax_number_message.grid(column=2, row=13)

        email_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        email_message.grid(column=2, row=14)

        url_message = Label(text='Placeholder text changes based on type of error', fg='white', bg='white')
        url_message.grid(column=2, row=15, pady=(0,10))

        button_message = Label(text='Please ensure all values above are entered correctly.', fg='white', bg='white',
                               font='arial')
        button_message.grid(column=2, row=16)


        # BUTTON:

        stringvar_list = [longitude_var, latitude_var, id_var, name_var, street_num_var, street_name_var, \
                          unit_num_var, postal_code_var, location_var, ward_var, naics_var, employee_range_var, \
                          phone_var, fax_var, email_var, url_var]
        csv_list=[]

        def write_to_csv(event):

            message_list = [longitude_message, latitude_message, id_message, \
                            name_message, street_number_message, street_name_message, \
                            unit_number_message, postal_code_message, location_message, \
                            ward_message, naics_message, employee_range_message, \
                            phone_message, fax_number_message, email_message, url_message]

            gatekeeper = False
            gatekeeper_jr = 0
            bad_list=[]

            for message in message_list:
                if '#90ee90' != message.cget('bg'):
                    gatekeeper_jr += 1

            if gatekeeper_jr == 0:
                gatekeeper = True
                button_message.config(fg='white')

            if gatekeeper == True:
                with open('business_data_record.csv', 'a', newline='') as csvfile:
                    input_writer = csv.writer(csvfile)
                    for stringvar in stringvar_list:
                        csv_list.append(stringvar.get())
                    input_writer.writerow(csv_list)
                button_message.config(text='Information submitted successfully!', fg='blue')
            else:
                button_message.config(fg='blue')


        button = Button(text='Submit', font='arial', width=56, height=2)
        button.grid(column=0, row=16, columnspan=2, sticky='e')
        button.bind('<Button-1>', write_to_csv)




        # WIDGET FORMATTING:


        entry_list = [longitude_entry, latitude_entry, id_entry, \
                      name_entry, street_number_entry, street_name_entry, \
                      unit_number_entry, postal_code_entry, location_entry, \
                      ward_entry, naics_sector_entry, employee_range_entry, \
                      phone_entry, fax_number_entry, email_entry, url_entry]

        label_list = [longitude_label, latitude_label, id_label, \
                      name_label, street_number_label, street_name_label, \
                      unit_number_label, postal_code_label, location_label, \
                      ward_label, naics_sector_label, employee_range_label, \
                      phone_label, fax_number_label, email_label, url_label]

        message_list = [longitude_message, latitude_message, id_message, \
                        name_message, street_number_message, street_name_message, \
                        unit_number_message, postal_code_message, location_message, \
                        ward_message, naics_message, employee_range_message, \
                        phone_message, fax_number_message, email_message, url_message]

        for entry_name in entry_list:
            entry_name.config(width=60, font='arial')

        for label_name in label_list:
            label_name.config(padx=15, font='arial', bg='white', pady=2, anchor='e')
            label_name.grid(sticky='ew')

        for message_name in message_list:
            message_name.config(padx=15, font='arial', bg='white', pady=2, anchor='w')
            message_name.grid(sticky='ew')


app = add_business()
app.master.title("Business Directory Entry Form")
app.master.config(bg='white')
app.master.geometry("1225x500")
app.mainloop()
