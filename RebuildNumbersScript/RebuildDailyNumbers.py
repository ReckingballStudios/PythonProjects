# Mason Reck
# 4/13/2022
# mason.reck@und.edu
# reckingballstudios@gmail.com
# This script is a screen scraper that automates a laborious task
# for the company Vertical Endeavors

import pyautogui

def startup():
    print("Hello! \(ᵔᵕᵔ)/")
    print("Please have your chrome tab with the rebuild numbers page ready.")
    print("Failsafe terminate the program by SLAMMING the mouse into a corner!\n")
    m = input("Please enter the month in number format (1-12)\nthat you would like to rebuild the numbers for:\n")

    # Prepare user for activation of program
    print("Please open your Chrome Tab with the rebuild numbers site open")
    pyautogui.sleep(1)
    print("Program starts in: \n3")
    pyautogui.sleep(1)
    print("2")
    pyautogui.sleep(1)
    print("1")
    pyautogui.sleep(2)

    # Make sure the screen is at the proper 100% zoom
    for i in range(20):
        pyautogui.hotkey('ctrl', '-')
    for i in range(7):
        pyautogui.hotkey('ctrl', '+')

    return m

def enter_date():
    pyautogui.click(calendarX, calendarY)
    dateStr = monthStr + str(i+1) + year
    if i < 9:
        dateStr = monthStr + "0" + str(i+1) + year
    pyautogui.write(dateStr)
    pyautogui.sleep(0.1)
    pyautogui.click(rX, rY)
    pyautogui.sleep(0.1)

def take_screenshot(day, scrshotBool):
    if scrshotBool[0] == 'T' or scrshotBool[0] == 't':
        pyautogui.screenshot("data/" + str(day) + ".png")
    
def click_rebuild():
    pyautogui.sleep(sleepTime)
    pyautogui.click(rebuildX, rebuildY)
    pyautogui.sleep(0.1)
    pyautogui.click(rebuildX, rebuildY) 
    pyautogui.sleep(sleepTime/3.0)

def click_ok():
    # The first okay that confirms submission
    pyautogui.click(okX, okY)
    pyautogui.sleep(sleepTime)
    # The second okay that brings you back to the submission page
    pyautogui.click(ok2X, ok2Y)
    pyautogui.sleep(sleepTime)


# Main Setup
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Retrieve the screen width and height
screenWidth, screenHeight = pyautogui.size()
print("Screen Resolution: " + str(screenWidth) + ", " + str(screenHeight) + "\n")

settings = open("settings.txt", "r")
settings.readline()
year = settings.readline()
# Leap Year Check
if int(year) % 4 == 0:
    monthDays[1] = 29
settings.readline()
sleepTime = float(settings.readline())
settings.readline()
screenshotsBool = settings.readline()
settings.close()

# If the buttons move or the web browser changes dimensions
# The first integer will need to be changed to match the button press
calendarX = int((525.0 / 1366.0) * screenWidth)
calendarY = int((260.0 / 768.0) * screenHeight)

rebuildX = int((900.0 / 1366.0) * screenWidth)
rebuildY = int((288.0 / 768.0) * screenHeight)

rX = int((600.0 / 1366.0) * screenWidth)
rY = int((350.0 / 768.0) * screenHeight)

okX = int((777.0 / 1366.0) * screenWidth)
okY = int((165.0 / 768.0) * screenHeight)

ok2X = int((960.0 / 1920.0) * screenWidth)
ok2Y = int((269.0 / 1080.0) * screenHeight)

month = int(startup())
if month < 10:
    monthStr = "0" + str(month)
else:
    monthStr = str(month)

numDays = monthDays[month-1]


###  MAIN OPERATION LOOP ###
for i in range(numDays):
    # We enter the date twice because the website is super buggy and weird
    enter_date()
    enter_date()
    print("Entering: " + str(monthStr) + " " + str(i+1))
    take_screenshot(i+1, screenshotsBool)
    click_rebuild()
    click_ok()
    
print("ヽ(´▽`)/   All Done!   (｡◕‿◕｡)")
input()



