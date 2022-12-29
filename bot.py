# Selenium documentation
# https://selenium-python.readthedocs.io/
# https://www.geeksforgeeks.org/selenium-python-tutorial/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from topics import topics_list
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from playsound import playsound

# To stop chrome from automatically closing
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#2-driver-management-software

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

link = 'https://www.omegle.com/'

# Maximize browser window
driver.maximize_window()
driver.get(link)
sleep(2)

# Adding topics to talk about from topics.py
def topics():
  newtopicinput = driver.find_element(By.CLASS_NAME, "newtopicinput")
  for topics in topics_list:
    newtopicinput.send_keys(topics)
    newtopicinput.send_keys(Keys.ENTER) 
    sleep(1)

# Click on text button after entering topics
def textbtn():
  textbtn = driver.find_element(By.ID, "textbtn")
  textbtn.click()
  sleep(1)

# Click on pop up checkboxes and confirm button after clicking the textbtn
def checkbox():
  # Tick on checkbox 1
  checkbox = driver.find_element(By.XPATH, "/html/body/div[7]/div/p[1]/label/input")
  checkbox.click()
  sleep(1)
  # Tick on checkbox 2
  checkbox = driver.find_element(By.XPATH, "/html/body/div[7]/div/p[2]/label/input")
  checkbox.click()
  sleep(1)
  # Click on Confirm and Continue button
  confirmbtn = driver.find_element(By.XPATH, "/html/body/div[7]/div/p[3]/input")
  confirmbtn.click()

# Completing recaptcha
# """no code is written. If recaptcha occurs, clear it manually"""

# Checking whether textbox is enabled or not
def checktextbox():
  textbox_path = driver.find_element(By.CSS_SELECTOR, 'textarea.chatmsg')
  if textbox_path.is_enabled(): 
    # is_enabled is used to check whether the element is enabled or not
    print("Textbox path is enabled")
    print("Redirected to sendmsg() from checktextbox()")
    send_message()
  else:
    print("Textbox path is disabled")
    try:
      textbox_disabled = WebDriverWait(driver, 500).until(
          EC.invisibility_of_element_located((By.CSS_SELECTOR, 'textarea.disabled')) 
          # invisibility_of_element_located is used to waite until the element is removed (invisibility_of_element_located returns a boolean value)
        )
      if textbox_disabled is True:
        print(textbox_disabled)
        print("Redirected to sndmsg() from checktextbox()")
        send_message()
      else:
        print("Something went wrong with the textbox_disabled")
    except StaleElementReferenceException:
      print("Textbox is not showing StaleElementReferenceException is executed")
      checktextbox()

# Function to send message
def send_message():
  textbox_path = driver.find_element(By.CSS_SELECTOR, 'textarea.chatmsg')
  textbox_path.send_keys("M ♂️ or F ♀️")
  # message send button
  msgsend_btn = driver.find_element(By.CSS_SELECTOR, "button.sendbtn")
  msgsend_btn.click()
  print("Asked stranger M of F")
  print("Redirected to checktext() from sendmsg()")
  checktext()

# Check text
def checktext():
  # global strangertext_path
  print("Entered to checktext fun()")
  try:
    strangertext_path = WebDriverWait(driver, 10).until(
      # stranger message path
      EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[1]/div[1]/div/div[4]/p/span"))
      # /html/body/div[6]/div/div/div[1]/div[1]/div/div[5]/p/span
    )
  except TimeoutException:
    print("Stranger not replied for 10 sec")
    print("Redirected to strangerdisconnect() from checktext()")
    strangerdisconnect()
  strangermsg = strangertext_path.text
  print("Stranger says : " + strangermsg)
  if (strangermsg == 'F' or strangermsg == 'f' or strangermsg == 'Hai F' or strangermsg == 'hai F' or strangermsg == 'Hai f' or strangermsg == 'hai f' or strangermsg == '.F' or strangermsg == '.f' or strangermsg == 'F.' or strangermsg == 'f.' or strangermsg == 'Hi F' or strangermsg == 'hi F' or strangermsg == 'Hi f' or strangermsg == 'hi f' or strangermsg == 'Hai F' or strangermsg == 'Hai f' or strangermsg == 'hai F' or strangermsg == 'hai f' or strangermsg == 'F Here' or strangermsg == 'F here' or strangermsg == 'f Here' or strangermsg == 'f here'):
    playsound('beep_beep.mp3')
    print("An F found")
    sleep(300)
  elif (strangermsg == 'M' or strangermsg == 'm' or strangermsg == '.M' or strangermsg == '.m' or strangermsg == 'M.' or strangermsg == 'm.' or strangermsg == 'Hai m' or strangermsg == 'Hai M' or strangermsg == 'hai M' or strangermsg == 'hai m' or strangermsg == 'Hi M' or strangermsg == 'Hi m' or strangermsg == 'hi M' or strangermsg == 'hi m' or strangermsg == 'Helo M' or strangermsg == 'Helo m' or strangermsg == 'helo M' or strangermsg == 'helo m' or strangermsg == 'Hello M' or strangermsg == 'Hello m' or strangermsg == 'hello M' or strangermsg == 'hello m' or strangermsg == 'M Here' or strangermsg == 'M here' or strangermsg == 'm Here' or strangermsg == 'm here'):
    disconnect_btn = driver.find_element(By.CSS_SELECTOR, 'button.disconnectbtn')
    action = ActionChains(driver)
    for i in range(3):
      action.move_to_element(disconnect_btn).click()
      action.perform()
    print("Disconnected M found")
    print("Redirected to checktextbox()")
    checktextbox()
  else:
    print("Redirected to whoami() from checktext()")
    whoami()

# Reply to stranger if the 2nd Message is not expected message 
def whoami():
  print("Entered to who am i function()")
  textbox_path = driver.find_element(By.CSS_SELECTOR, 'textarea.chatmsg')
  textbox_path.send_keys("M")
  print("You says M")
  # message send button
  msgsend_btn = driver.find_element(By.CSS_SELECTOR, "button.sendbtn")
  msgsend_btn.click()
  sleep(5)
  print("Redirected to stranger disconnect()")
  strangerdisconnect()

# Function Call
topics()
textbtn()
checkbox()
checktextbox()
