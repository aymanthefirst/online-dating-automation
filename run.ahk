MsgBox, 4,, Would you like to continue? (press Yes or No)
IfMsgBox Yes
    openAll()
else
    return

openAll(){
    Run, open "C:\Users\aharake\Documents\projects\t\t1.py"
    Run, open "C:\Users\aharake\Documents\projects\t\t2.py"
    Run, open "C:\Users\aharake\Documents\projects\t\t3.py"
    Run, open "C:\Users\aharake\Documents\projects\t\t4.py"
    ; Run, open "C:\Users\aharake\Documents\projects\t\t5.py"
}