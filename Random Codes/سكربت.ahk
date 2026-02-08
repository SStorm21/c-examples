 
; Main Script
 
 
global DELAY := -100 ;ms
 
\::
    While GetKeyState("\", "P"){
        Send,{UP} {control down}a{control up} {Backspace} {Enter 4}
        Sleep, DELAY
    }
    return