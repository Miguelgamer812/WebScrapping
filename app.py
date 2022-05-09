from selenium import webdriver

sitioweb = "https://dimayor.com.co/clubes-liga-betplay-dimayor/"

ruta = "C:\Chrome_webDriver\chromedriver.exe"

driver = webdriver.Chrome(ruta)
driver.get(sitioweb)

clubesBoton = driver.find_element_by_css_selector("#menu-item-1414 > a")
clubesBoton.click()

clubesLiga = driver.find_element_by_css_selector("#menu-item-1427 > a")
clubesLiga.click()

btnElegir = driver.find_element_by_css_selector(".eg-washington-element-10.eg-post-1565")
btnElegir.click()