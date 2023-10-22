from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.FIREFOX)


#driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
# Find <.... name="q" ...> ...</...>
elem = driver.find_element_by_name("q")
print(elem)
# elem is an input, so clear is to clear the input
elem.clear()
# Write "pycon"
elem.send_keys("pycon")
# Press ENTER
elem.send_keys(Keys.RETURN)
# Assert if string in the page
assert "No results found." not in driver.page_source
# Close Selenium driver
results = driver.find_element_by_xpath('//[@id="content"]/div/section/form/ul/li[1]/h3')
print(results)
driver.close()
