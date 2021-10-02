from selenium import webdriver

driver=webdriver.Chrome(executable path=r"")
driver.get("")
driver.maximize_window()
driver.title
print(driver.title)
driver.close()
