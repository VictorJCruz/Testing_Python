from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
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

btn_addlapicero = driver.find_element_by_id("btn_agregarCarrito-123321");
btn_addlapicero.click();
time.sleep(1); 

cantidad_lapicero = driver.find_element_by_id("txt_123321");
cantidad_lapicero.send_keys("2");
time.sleep(1);

btn_addlapicero.click();
time.sleep(1); 

alert = driver.switch_to.alert
alert.accept()
time.sleep(1);

btn_addborrador = driver.find_element_by_id("btn_agregarCarrito-5871256");
btn_addborrador.click();
time.sleep(1); 

cantidad_borrador = driver.find_element_by_id("txt_5871256");
cantidad_borrador.send_keys("6");
time.sleep(1);

btn_solicitar = driver.find_element_by_name("Solicitar");
btn_solicitar.click();
time.sleep(1); 

alert.accept()
time.sleep(1);

cantidad_borrador.send_keys(Keys.BACKSPACE);
cantidad_borrador.send_keys("2");
time.sleep(1);

btn_solicitar.click();
time.sleep(1); 

alert.accept()
time.sleep(30);

driver.quit();