from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Establish WebDriver and Chrome interaction
driver = webdriver.Chrome()

#Site to be test automated
driver.get('https://www.python.org')

#Finding HTML element 
search_bar = driver.find_element('name', 'q')

#Clears the searchbar 
search_bar.clear()

#Sends values to be input on the search bar
search_bar.send_keys('Getting started with Selenium')

#Imitates the pressing of Enter or Return key
search_bar.send_keys(Keys.RETURN)

#Prints the current URL the automation is running on
print(driver.current_url)

print(driver.window_handles)



