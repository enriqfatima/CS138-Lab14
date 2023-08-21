from tkinter import * # gui module
import vaccine_record 

#this method should be called when "Submit"   button is clicked
def process():
  my_vax = vaccine_record.VaccineRecord(fname_entry.get(), flname_entry.get(), dob_entry.get(), manufac_entry.get(), batch_entry.get(), d1_date_entry.get(), location_entry.get(), manufacturer2_entry.get(), batch2_entry.get(), date2_entry.get(), location2_entry.get())
  my_vax.printCard()

  if no_second_dose.get() == 1:
    print("You should get your second dose, if appropriate, 3 or 4 weeks after your first dose. Please check with your healthcare provider to verify and schedule an appointment if necessary")

  
#this method should be called when checkbox is ticked/unticked. Have an IF for off, ELSE   for on
def checkbox_process():
  if no_second_dose.get() == 1:
    #clear out entries for 2nd dose 
    manufacturer2_entry.delete(0,END)
    date2_entry.delete(0,END)
    batch2_entry.delete(0,END)
    location2_entry.delete(0,END)

    #remove from gui
    manufacturer2_label.grid_remove()
    manufacturer2_entry.grid_remove()
    
    date2_label.grid_remove()
    date2_entry.grid_remove()
    
    batch2_label.grid_remove()
    batch2_entry.grid_remove()
    
    location2_label.grid_remove()
    location2_entry.grid_remove()
  else:
    manufacturer2_label.grid(row = 9, column = 0)
    manufacturer2_entry.grid(row = 9, column = 1)
    batch2_label.grid(row = 10, column = 0)
    batch2_entry.grid(row = 10, column = 1)
    date2_label.grid(row = 11, column = 0)
    date2_entry.grid(row = 11, column = 1)
    location2_label.grid(row = 12, column = 0)
    location2_entry.grid(row = 12, column = 1)

    
    
    

#begin code for GUI 
window = Tk()
window.title("Vaccine Entry") #title 
window.geometry("600x600") 

#checkbox variable 
no_second_dose = IntVar()
cbox = Checkbutton(window, text = "No second dose", variable = no_second_dose, onvalue = 1, offvalue = 0, command = checkbox_process)
cbox.grid(row = 8, column = 2)

#personal info section 
fname_label = Label(window, text = "Fist Name")
fname_entry = Entry(window, bd = 5)

flname_label =Label(window, text = "Last Name")
flname_entry = Entry(window, bd = 5)

dob_label = Label(window, text = "Date of birth(mm/dd/yyyy)")
dob_entry = Entry(window, bd = 5)


##GUI LAYOUT###
#personal info layout 
fname_label.grid(row = 0, column = 0)
fname_entry.grid(row = 0, column = 1)

flname_label.grid(row = 1, column = 0)
flname_entry.grid(row = 1, column = 1)

dob_label.grid(row = 2, column = 0)
dob_entry.grid(row = 2, column = 1)

#first dode layout 
vax_label1 = Label(window, text = "First Dose Information")
vax_label1.grid(row = 3, column = 1)

manufac_label = Label(window, text = "Manufacturer" )
manufac_entry = Entry(window, bd = 5)
manufac_label.grid(row = 4, column = 0)
manufac_entry.grid(row = 4, column = 1)

batch_label = Label(window, text = "Batch" )
batch_entry = Entry(window, bd = 5)
batch_label.grid(row = 5, column = 0)
batch_entry.grid(row = 5, column = 1)

d1_date_label = Label(window, text = "Date(mm/dd/yyyy)")
d1_date_entry = Entry(window, bd = 5)
d1_date_label.grid(row = 6, column = 0)
d1_date_entry.grid(row = 6, column = 1)

location_label = Label(window, text = "Location")
location_entry = Entry(window, bd = 5)
location_label.grid(row = 7, column = 0)
location_entry.grid(row = 7, column = 1)
#second dose label 
vax_label2 = Label(window, text = "Second Dose Information")
vax_label2.grid(row = 8, column = 1)

manufacturer2_label = Label(window, text = "Manufacturer")
manufacturer2_entry = Entry(window, bd = 5)

manufacturer2_label.grid(row = 9, column = 0)
manufacturer2_entry.grid(row = 9, column = 1)

batch2_label = Label(window, text = "Batch")
batch2_entry = Entry(window, bd = 5)
batch2_label.grid(row = 10, column = 0)
batch2_entry.grid(row = 10, column = 1)

date2_label = Label(window, text = "Date(mm/dd/yyyy)")
date2_entry = Entry(window, bd = 5)
date2_label.grid(row = 11, column = 0)
date2_entry.grid(row = 11, column = 1)

location2_label = Label(window, text = "Location")
location2_entry = Entry(window, bd = 5)
location2_label.grid(row = 12, column = 0)
location2_entry.grid(row = 12, column = 1)

#submit button widget 
submit_button = Button(text = "Submit", command = process)
submit_button.grid(row = 10, column = 2)

