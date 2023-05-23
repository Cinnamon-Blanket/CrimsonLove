screen timed_choice(items):
    style_prefix "choice"
    default timeout = 0
    default tCounter = 0
    default defAction = 0

    vbox:
        for i in items:
            $ defAction = i.action.value if i.kwargs.get("auto", False) else defAction
            $ timeout = i.kwargs.get("time", timeout)
            textbutton i.caption action i.action:
                selected i.kwargs.get("auto",False)  #this line is optional if you want player to know what will happen
    
    timer 0.1 repeat True action SetScreenVariable('tCounter', tCounter+0.1 )
    
    if timeout > 0:
        bar xcenter 0.5 yalign 0.0 xsize 768 ysize 32 yoffset 16:
            value timeout - tCounter
            range timeout
        timer timeout action Return(defAction)
