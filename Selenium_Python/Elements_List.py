Selenium (Python Example)
Here's how you can find elements using various locators:

ID
element = driver.find_element_by_id('element_id')

Name
element = driver.find_element_by_name('element_name')

Class Name
element = driver.find_element_by_class_name('element_class')

Tag Name
element = driver.find_element_by_tag_name('input')

CSS Selector
element = driver.find_element_by_css_selector('.class_name')

XPath
element = driver.find_element_by_xpath('//div[@class="class_name"]')

Link Text
element = driver.find_element_by_link_text('Link Text')

Partial Link Text
element = driver.find_element_by_partial_link_text('Partial Link Text')