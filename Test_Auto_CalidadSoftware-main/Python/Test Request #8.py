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

btn_iniciar = driver.find_element_by_id("form-submit-900");
btn_iniciar.click();
time.sleep(30);

driver.quit();