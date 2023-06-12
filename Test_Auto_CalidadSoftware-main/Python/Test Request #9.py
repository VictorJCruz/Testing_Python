from selenium import webdriver;
from selenium.webdriver.support.ui import Select
import time;

PATH = "src\chromedriver.exe";
driver = webdriver.Chrome(PATH);
driver.get("http://suministros.facturaelectronicacr.es");
driver.maximize_window();
print(driver.title);

username = driver.find_element_by_name("txt_cedUsuario");
username.send_keys("305320570");
time.sleep(1); 

password = driver.find_element_by_name("txt_conUsuario");
password.send_keys("123");
time.sleep(1); 

btn_iniciar = driver.find_element_by_id("form-submit");
btn_iniciar.click();
time.sleep(1); 

btn_addCajaResmas = driver.find_element_by_id("btn_agregarCarrito-1520");
btn_addCajaResmas.click();
time.sleep(1); 

cantidad_resmas = driver.find_element_by_id("txt_1520");
cantidad_resmas.send_keys("2");
time.sleep(1); 

contador = driver.find_element_by_id("txt_contador");
contador.send_keys("123");
time.sleep(1); 

select_impresora = driver.find_element_by_id('txt_impresora');
d = Select(select_impresora)
d.select_by_value('335');
time.sleep(1); 

input_file = driver.find_element_by_xpath("//input[@type='file']")
input_file.send_keys("D:\Documentos\GitHub\Test_Auto_CalidadSoftware\Python\src\contador.pdf")
time.sleep(1); 

btn_solicitar = driver.find_element_by_name("Solicitar");
btn_solicitar.click();
time.sleep(1); 

alert = driver.switch_to.alert
alert.accept()
time.sleep(60); 

driver.quit();