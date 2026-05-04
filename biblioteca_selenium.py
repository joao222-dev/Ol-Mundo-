# from selenium import webdriver
# import time

# navegador = webdriver.Edge()

# navegador.get("https://mail.google.com/mail/u/0/?hl=pt-BR#inbox")

# navegador.maximize_window()

# navegador.find_element("xpath", '//*[@id="identifierId"]').send_keys("

# time.sleep(10)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/")
driver.maximize_window()

input("Faça login e aperte ENTER...")

# garante que está na página de vagas
driver.get("https://www.linkedin.com/jobs/")
wait = WebDriverWait(driver, 10)

# espera o campo aparecer
busca = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label*='Search']"))
)

busca.send_keys("python")
busca.send_keys(Keys.ENTER)

time.sleep(5)

vagas = driver.find_elements(By.CSS_SELECTOR, "ul.jobs-search__results-list li")

for vaga in vagas[:5]:
    try:
        titulo = vaga.find_element(By.CSS_SELECTOR, "h3").text
        empresa = vaga.find_element(By.CSS_SELECTOR, "h4").text

        print("\nVaga:", titulo)
        print("Empresa:", empresa)
    except:
        continue

driver.quit()