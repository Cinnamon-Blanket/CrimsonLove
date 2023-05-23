screen gridchoice(items, cols, rows):
    style_prefix "choice"

    grid cols rows:
        xalign 0.5
        ypos 500
        yanchor 0.5
        allow_underfull True

        spacing gui.choice_spacing

        for i in items:
            if i is not None:
                textbutton i.caption action i.action xsize 400
            else:
                null