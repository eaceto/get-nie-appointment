from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys

driver = webdriver.Firefox()

#scroll to bottom of page
def wait(time):
    WebDriverWait(driver, time)
def scroll():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#click button after scrolling to bottom of page
def click_button(btnid):
    scroll()
    driver.find_element(By.ID, btnid).click()

#select option from a drop down menu
def select_option(menu_id, option):
    select = Select(driver.find_element(By.ID, menu_id))
    select.select_by_visible_text(option)

#fill a text field
def fill_field(fld_id, text):
    field = driver.find_element(By.ID, fld_id)
    field.send_keys(text)

#open the nie website
def start():
    driver.get("https://icp.administracionelectronica.gob.es/icpplustieb/index.html")

#fill in and continue on the select city page
def go_to_city_page(city):
    select_option("form", city)
    click_button("btnAceptar")

#choose the correct type of appointment for NIE page
def go_to_appointment_page(appointmentType):
    scroll()
    select_option("tramiteGrupo[1]", appointmentType)
    click_button("btnAceptar")
#could make this better

#conditions page after appointment page
def go_to_conditions_page():
    click_button("btnEntrar")

#input basic info to ask for appointment
def go_to_info_page(nie, name, country, expiry):
    click_button("rdbTipoDocPas")
    fill_field("txtIdCitado", passport)
    fill_field("txtDesCitado", name)
    click_button("btnEnviar")

#ask for an appointment
def require_appointment():
    click_button("btnEnviar")

#Select second office because it could return a single preselcted office or multiple where you have to make a choice
def go_to_office_page():
    try:
        driver.find_element(By.ID, "idSede").send_keys(Keys.DOWN)
    except:
        pass
    click_button("btnSiguiente")

#if there are no offices to choose from, exit
def no_appointment():
    click_button("btnSalir")

#info to be inputted after office selection - last step
def add_info_compl(tel, email):
    fill_field("txtTelefonoCitado", tel)
    fill_field("emailUNO", email)
    fill_field("emailDOS", email)
    click_button("btnSiguiente")

start()
try:

    city = sys.argv[1] # as defined in the list of cities that the page has
    passport = sys.argv[2]
    name = sys.argv[3]
    country = sys.argv[4]   # as defined in the list of countries that the page has ( in UPPERCASE )
    birthyear = sys.argv[5] 
    tel = sys.argv[6] # Spanish phone number without country code
    email = sys.argv[7]
    appointmentType = sys.argv[8] # as defined in the list of appointment types of the selected city

    print ("Looking for appointment of type: " + appointmentType)
    print ("\tCity of appointment: " + city)
    print ("\tName: " + name)
    print ("\tPassport: " + passport)
    print ("\tCountry: " + country)
    print ("\tYear of birth: " + birthyear)
    print ("\tEmail: " + email)
    print ("\tTelephone: " + tel)
    
    while True:
        go_to_city_page(city)
        go_to_appointment_page(appointmentType)
        go_to_conditions_page()
        go_to_info_page(passport, name, country, birthyear)
        require_appointment()
        try:
            go_to_office_page()
            add_info_compl(tel, email)
            if not driver.getPageSource().contains("No hay citas"):
                wait(1000)
                break
            else:
                click_button("btnSubmit")
        except:
            no_appointment()
except KeyboardInterrupt:
    wait(100)

#error page URL https://sede.administracionespublicas.gob.es/icpplustieb/acOfertarCita

#office selection page URL is https://sede.administracionespublicas.gob.es/icpplustieb/acCitar

#for the info_compl page URL is https://sede.administracionespublicas.gob.es/icpplustieb/acVerFormulario

#could get generic back page: https://sede.administracionespublicas.gob.es/icpplustieb/infogenerica
#use click_button("btnSubmit") if so
