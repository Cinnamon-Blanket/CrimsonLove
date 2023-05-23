label chapter2_day3:
    scene black
    with fade
    centered "Day 45 - Wednesday 14th February"
    pause 1.0
    ###
    scene bg living room day
    stop music fadeout 0.5
    with fade
    "I wake up with a start."
    "I check the time."
    my "Shit!"
    "I get up, rushing to get ready."
    my "I'm so so late..."
    "I look for Mora, but she's nowhere to be found."
    my "Shit..."
    my "I gotta go..."
    my "I'm sorry, Mora."
    "I rush out the door."

    scene bg stage
    play music stage_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show eli work eyes_closed normal
    "I practically fly through the door."
    "Eli is waiting for me."
    eli "Woah, slow down!"
    eli "You're not late yet. Barely."
    eli "Good morning!"
    my "Good... morning..."
    "I take a moment to catch my breath."
    show eli work normal
    eli "Today's the day..."
    my "Yep."
    my "We need to finish preparations."
    eli "Are you sure it'll be okay? Since you cancelled the stage maintenance..."
    my "It'll be fine."
    my "It's only one night."
    eli "Okay!"
    hide eli
    with moveoutright
    "She leaves."
    "I habitually look to the corner, but of course, Mora isn't there."
    "I have a bad feeling..."
    "I must get to work, anyways. The show is tonight."
    "{b}{u}A few hours later...{/u}{/b}"
    eli "The group are here!"
    "Eli calls from across the room."
    "I rush to meet them."

    scene bg backstage
    with fade
    show amari casual eyes_closed normal at left
    show angela casual normal at center
    show zena arbiter eyes_closed normal at right
    "I arrive backstage."
    my "Hi girls!"
    amari "Hello!!"
    show angela casual talk
    angela "Hey!"
    angela "It's nice to be back here..."
    angela "Sorry for rescheduling so suddenly."
    my "Hey, it's fine."
    my "A Valentine's concert..."
    my "I have a date tonight too, you know."
    show angela casual eyes_closed talk
    angela "Ooh~?"
    angela "Who?!"
    my "Ahaha, not sure if she wants it public yet..."
    my "Sorry."
    show zena arbiter eyes_closed talk
    zena "Can I talk to you, Alex?"
    my "Huh-"
    ".{w} .{w} .{w}"
    "It took me this long to notice."
    "She's... Wearing her full Arbiter outfit..."
    "For the first time I've seen..."
    my "Where's Mora?"
    "I turn serious."
    show zena arbiter talk
    stop music fadeout 1.0
    zena "That's what I wanted to talk to you about."
    zena "We have a... policy against personal commitments to our subjects."
    my "She didn't tell me that!"
    my "Why did she..."
    show angela casual normal
    angela "We'll leave you two alone. It's hard to hear."
    angela "Plus, we need to get ready."
    hide angela
    hide amari
    with moveoutleft
    show zena arbiter normal at center
    with move
    "They head to the changing cubicles."
    "Zena sighs."
    zena "This never gets easier to say."
    my "What happened to her?"
    zena "She's being de-assigned from you."
    my "What-"
    my "Why??"
    zena "You full well know why."
    zena "Don't act stupid."
    zena "The government knows everything that happens..."
    zena "Even when you think you're in private."
    my "The... Confession..."
    zena "You may still hold a relationship with her, but she'll have to move out of the apartment, and you'll be assigned a new Arbiter."
    my "Ah..."
    my "So suddenly..."
    "I stumble a bit."
    zena "I told you it's not easy."
    my "Well, where is she now?"
    zena "Probably here. You have a date, remember."
    my "Oh, right..."
    zena "You should go meet her."
    zena "Make her happy."
    my "Okay..."

    scene bg outdoor stairs
    play music love_theme fadein 0.5 fadeout 0.5 loop
    with fade
    "I find her outside."
    my "Mora!"
    show mora date normal
    mora "Oh, hello."
    my "Wow... You look beautiful..."
    mora "Thank you."
    mora "Shall we go inside? It's cold."
    my "Ah right, yeah..."
    my "Before that though..."
    my "I heard what happened. I'm so sorry."
    mora "Huh?"
    mora "What happened?"
    my "...?"
    "What?"
    "There's no way Zena lied."
    "Or maybe... Mora doesn't know herself yet..."
    "Shit..."
    my "Never mind."
    my "Let's go!"
    "I decide to let it go for now."
    "I can tell her later."
    "I don't wanna ruin this night..."

    scene bg stage
    with fade
    show mora date normal
    with moveinleft
    "We enter and take our seats."
    my "See, being stage manager does something, we got front row seats!"
    mora "Yeah... You are useful after all."
    my "Oi!"
    "I playfully push her."
    my "Oop- It's about to start-"
    scene bg stage
    play music artificial_interspace_theme fadein 0.5 fadeout 0.5 loop
    with flash
    show amari idol eyes_closed talk at left
    show angela idol talk at center
    show zena idol talk at right
    angela "Good evening, everyone!"
    angela "I'm Angela!"
    amari "I'm Amari!"
    zena "I'm Zena!"
    angela "We are The Artificial Interspace!"
    amari "I hope you enjoy our show this evening!"
    "The crowd goes wild."
    stop music fadeout 1.0
    zena "Everyone, before we begin, I have an announcent to make."
    show angela idol eyes_closed normal
    show amari idol normal
    angela "Sigh."
    "Huh??"
    mora "What's going on?"
    my "I don't know..."
    zena "Tonight will be my last performance as an idol!"
    "..."
    mora "..."
    "The crowd silences."
    "No way..."
    "What is happening...?"
    "Zena steps forward."
    zena "I'm quitting because-"

    scene black
    with flash
    "Everything goes dark."
    "It's quiet for a moment."
    "Then..."
    scene white
    with hpunch
    scene black
    with hpunch
    "The whole venue shakes."
    "Everyone starts screaming."
    my "WHAT IS HAPPENING?!"
    "I look beside me."
    "Mora is gone."
    my "MORA?!"
    my "MORAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-"
    window hide
    scene black
    with fade
    centered "End of... Actually, no. I'm not going to let that happen. Sorry!"
    $ chapter3_avail = True
    "{b}Error. System failure.{/b}"
    "{b}Error. Scenario failure.{/b}"
    "{b}Error. Aborting all processes...{/b}"
    "{b}Abortion complete.{/b}"
    "{b}Rebooting...{/b}"
    pause 1.0
    "{i}It's all my fault... I should've performed the maintenance... I could've stopped the incident...{/i}"
    "{i}At the end of everything...{/i}"
    "{i}Mora, do you have any regrets?{/i}"
    $ chapter3_avail = True
    menu chapter2_day3_end:
        "Day complete!"
        "{b}Carry on option is not available due to Chapter Completion.{/b}"
        "Chapter selection.":
            jump chapter_select