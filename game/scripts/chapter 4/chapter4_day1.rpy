label chapter4_day1:
    scene black
    with fade
    centered "Day 15 - Monday 15th January."
    pause 1.0

    scene bg bedroom day
    with fade
    "I awaken, yawning and stretching out."
    "My body feels so tense for some reason..."
    "I stand up, make the bed, and straighten myself up, before heading into the kitchen to grab breakfast."

    scene bg kitchen day
    with fade
    "I enter the kitchen, grabbing a couple of slices of bread from the cupboard, butter from the butter tray, and a knife."
    "I put the bread into the toaster, letting it go soft but not burnt."
    "Then I apply the butter, being careful not to rip the bread."
    "After I am done, I place the toast on a plate and head to pretend to put the knife in the dishwasher."
    "3..."
    "2..."
    "1..."
    play music revenge_theme
    my "AAAAAAAAAAHHHHHHH!!!!!!!!!!!!!!!!!"
    "I scream and charge at the person lurking in the shadows."
    "I throw my knife but they manage to duck away just in time."
    "???" "Jeez, you're good."
    my "Show yourself, you coward!"
    "The truth is, I know exactly who it is."
    "She steps forward."
    show interface arbiter smile
    interface "So, we meet again!"
    my "Indeed we do."
    "I pick up my knife and point the blade in her direction as a warning signal."
    "She doesn't even flinch."
    my "Where is Hareka?!"
    "I know where she is."
    "She'll say..."
    show interface arbiter eyes_closed smile
    interface "I cannot relay that information to you."
    "Knew it."
    "Next she'll order..."
    show interface arbiter eyes_closed normal
    interface "You must come with me."
    "I oblige with her requests."
    "This is all working out perfectly..."

    scene bg office day
    show interface arbiter normal
    with flash
    "We teleport to the office."
    interface "Wait there. I shall fetch Kana."
    hide interface with moveoutleft
    "She leaves, locking the door behind her."
    "I smile to myself. This is all going completely how Hareka predicted it would... It's almost eery how perfect it's been so far..."
    "I'll always stay on high alert, just in case."
    "A few minutes later, she returns, with Kana in tow."
    show interface arbiter normal at left
    show kana arbiter normal at right
    with moveinleft
    "I turn to face them."
    my "Hello, Kana."
    kana "Hello, Alex."
    my "Can you tell me where Hareka is? Or are you not allowed to tell me either?"
    show kana arbiter eyes_closed normal
    kana "Sigh..."
    kana "You know the answer to that."
    my "Well, I'm sure I can guess, at least..."
    "I don't have to guess. I know {i}exactly{/i} where she is right now."
    my "Can you at least tell me why?"
    "I put on a pleading face."
    show kana arbiter normal
    kana "We have reason to believe she hacked into our systems last night. That is a criminal offence."
    my "Oh..."
    my "Well then, what will happen to me?"
    "Please... Don't let me down now..."
    kana "We will find a new Arbiter to look after you."
    kana "In the meantime, you shall stay with us."
    my "Okay..."
    "Perfect."
    scene bg office evening
    show interface arbiter eyes_closed normal at left
    show kana arbiter eyes_closed normal at right
    with fade
    "Evening rolls around."
    "We've mostly been doing our own thing. They aren't half as chatty as Hareka."
    "Oh well. That's fine. I'm only buying time, anyways."
    "Just then..."
    scene bg office evening
    show interface arbiter normal at left
    show kana arbiter normal at right
    with flash
    with hpunch
    "There it goes."
    "The explosion echoes throughout the entire building."
    kana "What the fuck was that?!"
    "She glares at me."
    my "Hey, how could I do anything? I've only ever been in this room!"
    "She sighs, shaking her head, and turning back to The Interface."
    kana "Interface, can you pinpoint the location of the explosion?"
    "No response."
    "The Interface has gone completely still and silent."
    kana "Shit!"
    my "What?"
    "I genuinely didn't anticipate this part."
    show kana arbiter eyes_closed normal
    "Kana sighs, heading to The Interface and dragging her to the sofa, laying her down."
    kana "Sleep well."
    my "What happened??"
    "Kana turns back to me."
    show kana arbiter normal
    kana "The explosion must have happened from inside the Control Unit Server Room."
    kana "She'll be fine, but for now, we must evacuate. Please follow me."
    my "Are you gonna leave her??"
    kana "Teleportation."
    my "Ah..."
    "Wait. No! I can't leave!"
    "This'll ruin everything!!!"

    scene black
    with hpunch
    "I get knocked to the floor violently."
    "I roll, trying to protect my head, and end up landing on my back funny."
    "I groan in pain."
    my "What the fuck... Ow..."
    kana "What the-"
    kana "Who are you??"
    "???" "I am your worst nightmare, dear Kana."
    "..."
    "That voice..."
    "I recognise it..."
    "Could it really be...?"
    kana "No way..."
    kana "How did you get past the Script Barriers?"
    kana "This shouldn't be possible..."
    "The mystery girl laughs."
    "???" "You're so adorably clueless."
    kana "..."
    kana "I assume you caused the explosion, then."
    kana "To wipe out your main threat."
    "I assume she means The Interface by that."
    "???" "Oh, dear, that was just a diversion! The main event is only just beginning~!"
    "???" "Buckle your seatbelts, ladies and gentlemen! We're going on an {i}explosive{/i} ride~!"
    scene white
    with flash
    "A bright flash of light."
    "Warmth surrounds me."
    kana "No!"
    "Kana cries."
    kana "Why?!"
    kana "Why would you do this?!"
    "???" "A simple reason, dear."
    "The person steps forward."
    show hareka arbiter ringdev blur
    with dissolve
    "???" "I want to give you a taste of your own medicine."
    "???" "I want you to feel how I felt, being walked all over..."
    "???" "I want revenge, Kana."
    "???" "And now... I finally have what I want."
    window hide
    $ chapter4_day2_avail = True
    scene black
    with fade
    centered "End of day."
    menu chapter4_day1_end:
        "Day 15 (Chapter 4 - Day 1) complete!"
        "Would you like to return to the chapter selection screen, or carry onto the next day?"
        "Chapter selection.":
            jump chapter_select
        "Carry on.":
            jump chapter4_day2