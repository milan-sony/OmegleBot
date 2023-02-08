# Selenium documentation
# https://selenium-python.readthedocs.io/
# https://www.geeksforgeeks.org/selenium-python-tutorial/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from topics import topics_list
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

# Getting topics from topics.py
def topics():
  newtopicinput = driver.find_element(By.CLASS_NAME, "newtopicinput")
  for topics in topics_list:
    newtopicinput.send_keys(topics)
    newtopicinput.send_keys(Keys.ENTER) 
    sleep(1)

# Click text button
def textbtn():
  textbtn = driver.find_element(By.ID, "textbtn")
  textbtn.click()
  sleep(1)

# Click on pop up checkboxes and confirm button
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
# """no code is written"""

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

# Function to click disconnect button
def disconnet_btn():
  disconnect_btn = driver.find_element(By.CSS_SELECTOR, 'button.disconnectbtn')
  action = ActionChains(driver)
  for i in range(3):
    action.move_to_element(disconnect_btn).click()
    action.perform()
    print("Redirected to checktextbox() from disconnect()")
  checktextbox()

# Check text
def checktext():
  # global strangertext_path
  print("Entered to checktext fun()")
  try:
    strangertext_path = WebDriverWait(driver, 10).until(
      # stranger message path
      EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[1]/div[1]/div/div[4]/p/span"))
    )
  except TimeoutException:
    print("Stranger not replied for 10 sec")
    print("Redirected to strangerdisconnect() from checktext()")
    strangerdisconnect()
  strangermsg = strangertext_path.text
  strangermsglower = strangermsg.lower()
  print("Stranger says : " + strangermsglower)
  if (strangermsglower == 'f' or strangermsglower == 'hai f' or strangermsglower == 'f hai' or strangermsglower == 'f here' or strangermsglower == 'hello f' or strangermsglower == 'helo f' or strangermsglower == '.f' or strangermsglower == 'f.' or strangermsglower == 'hi f' or strangermsglower == 'f hi' or strangermsglower == 'f,hai' or strangermsglower == 'f, hai' or strangermsglower == 'f,hi' or strangermsglower == 'f, hi' or strangermsglower == 'f here' or strangermsglower == '♀️' or strangermsglower == 'f ♀️' or strangermsglower == '♀️ f'):
    playsound('beep_beep.mp3')
    print("An F found")
    exit()
  elif(strangermsglower == 'hai' or strangermsglower == 'hi' or strangermsglower == 'hello' == strangermsglower == 'hey'):
    whoami()
  elif (strangermsglower == 'm' or strangermsglower == '.m' or strangermsglower == 'm.' or strangermsglower == 'hai m' or strangermsglower == 'hi m' or strangermsglower == 'm hai' or strangermsglower == 'm hi' or strangermsglower == 'helo m' or strangermsglower == 'hello m' or strangermsglower == 'm here' or strangermsglower == '♂️' or strangermsglower == 'm ♂️' or strangermsglower == 'm♂️' or strangermsglower == '♂️m'):
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

def whoami():
  print("Entered to who am i function()")
  textbox_path = driver.find_element(By.CSS_SELECTOR, 'textarea.chatmsg')
  textbox_path.send_keys("M")
  print("You says M")
  # message send button
  msgsend_btn = driver.find_element(By.CSS_SELECTOR, "button.sendbtn")
  msgsend_btn.click()
  # sleep(5)
  # print("Redirected to stranger disconnect()")
  print("Redirected to checktext2()")
  checktext2()
  # strangerdisconnect()

def checktext2():
  print("Entered to checktext2 fun()")
  try:
    strangertext2_path = WebDriverWait(driver, 10).until(
      # stranger message path
      EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[1]/div[1]/div/div[6]/p/span"))
    )
  except TimeoutException:
    print("Stranger not replied for 10 sec")
    print("Redirected to strangerdisconnect() from checktext()")
    strangerdisconnect()
  strangermsg2 = strangertext2_path.text
  strangermsg2lower = strangermsg2.lower()
  print("Stranger says : " + strangermsg2lower)
  if (strangermsg2lower == 'f' or strangermsg2lower == 'hai f' or strangermsg2lower == 'f hai' or strangermsg2lower == 'f here' or strangermsg2lower == 'hello f' or strangermsg2lower == 'helo f' or strangermsg2lower == '.f' or strangermsg2lower == 'f.' or strangermsg2lower == 'hi f' or strangermsg2lower == 'f hi' or strangermsg2lower == 'f,hai' or strangermsg2lower == 'f, hai' or strangermsg2lower == 'f,hi' or strangermsg2lower == 'f, hi' or strangermsg2lower == 'f here' or strangermsg2lower == '♀️' or strangermsg2lower == 'f ♀️' or strangermsg2lower == '♀️ f'):
    playsound('beep_beep.mp3')
    print("An F found")
    exit()
  elif (strangermsg2lower == 'm' or strangermsg2lower == '.m' or strangermsg2lower == 'm.' or strangermsg2lower == 'hai m' or strangermsg2lower == 'hi m' or strangermsg2lower == 'm hai' or strangermsg2lower == 'm hi' or strangermsg2lower == 'helo m' or strangermsg2lower == 'hello m' or strangermsg2lower == 'm here' or strangermsg2lower == '♂️' or strangermsg2lower == 'm ♂️' or strangermsg2lower == 'm♂️' or strangermsg2lower == '♂️m'):
    disconnect_btn = driver.find_element(By.CSS_SELECTOR, 'button.disconnectbtn')
    action = ActionChains(driver)
    for i in range(3):
      action.move_to_element(disconnect_btn).click()
      action.perform()
    print("Disconnected M found")
    print("Redirected to checktextbox()")
    checktextbox()

# Check whether a stranger disconnected or not
def strangerdisconnect():
  try:
    WebDriverWait(driver, 10).until(
      EC.visibility_of_all_elements_located((By.CLASS_NAME, 'newchatbtnwrapper'))
    )
    print("strangerdisconnected redirected to disconnect_btn()")
    disconnet_btn()
  
  except TimeoutException:
    print(TimeoutException)
    print("Strangerdisconnect path not found timeout redirected to disconnect_btn()")
    disconnet_btn()

topics()
textbtn()
checkbox()
checktextbox()
# strangerdisconnect()