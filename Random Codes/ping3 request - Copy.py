import pyautogui
import time
time.sleep(2)
x=1
while 1:
    if x<200:
        x+=1
        time.sleep(0.025)
        print('@sent!')
        message = '''#%$S*#%$S*Xz0-#%$#%$S*Xz0-S*Xz0-#%$S*Xz0-#%$S*Xz0-Xz0-#%$S*Xz0-#%$S*Xz0-
        #%$S*Xz0-#%$S*X#%$S*Xz0-#%$S*Xz0-z0-#%$S*Xz0-#%$S*Xz0-#%$S*Xz0-
        '''
        pyautogui.write(message)
        pyautogui.hotkey('enter')
        if x ==200:
            print("Done!")
            break


