import time
from selenium import webdriver
from UserInfo import *

driver = webdriver.Firefox(executable_path='Driver/geckodriver.exe')
driver.get("https://ent.netocentre.fr/cas/login?service=https:%2F%2F0370884K.index-education.net%2Fpronote%2Feleve.html")

button_connexion_page1 = driver.find_element_by_class_name("parentEleveEN-IdP")
button_connexion_page1.click()
button_connexion_page2 = driver.find_element_by_id("bouton_eleve")
button_connexion_page2.click()

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
connexion = driver.find_element_by_id("bouton_valider")
username.send_keys(UserName)
password.send_keys(PassWord)
connexion.click()

time.sleep(5)

down = driver.find_element_by_class_name("footer-toggler")
down.click()
cahier = driver.find_element_by_id("GInterface.Instances[0].Instances[1]_Combo1")
cahier.click()

time.sleep(5)

hebdo = driver.find_element_by_name("id_143")
hebdo.click()