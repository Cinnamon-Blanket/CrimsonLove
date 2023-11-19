label chapter1_day1:
    scene black
    with fade
    centered "Day 1 - Monday 1st January."
    pause 1.0

    scene bg train day rain
    with fade
    play music chapter1_theme fadein 0.5 loop fadeout 0.5
    "I step onto the train, yawning, and take a seat."
    "Time to begin the journey..."
    "It's early morning. I didn't really {i}have to{/i} leave this early, but I wanted to anyways."
    "Better to be safe than sorry, right?"
    "The weather outside is miserable..."
    "As would be expected..."
    "It's finally the New Year."
    "I made some pretty tough resolutions, but I plan to stick to them the best I can."
    "One of them was rather stupid."
    "\"Make a friend.\""
    "How silly is that?"
    "I chuckle to myself."
    "Oh well. I'll still try."
    "It's not easy making friends, when you're a loner like me."
    "I didn't really choose to be this way. I just keep to myself and people don't bother to notice me."
    "It's a blessing, really, I don't like attention all too much..."
    "{b}{u}Half an hour later...{/u}{/b}"
    "The train is gathering more people as the journey goes on."
    "It's getting pretty packed now. I'm glad I got a seat earlier."
    # voice "audio/voice_acting/chapter1_2/001.mp3"
    "???" "Excuse me?"
    # voice "audio/voice_acting/chapter1_2/002.mp3"
    my "Huh-"
    "I look up, to see{nw}{done} a girl standing in front of me."
    show zena newstudent normal
    "I look up, to see{fast} a girl standing in front of me."
    # voice "audio/voice_acting/chapter1_2/003.mp3"
    my "Can I help you?"
    # voice "audio/voice_acting/chapter1_2/004.mp3"
    "???" "Can I sit next to you? There's no other free seats."
    # voice "audio/voice_acting/chapter1_2/005.mp3"
    my "Ah..."
    "I have no reason to not let her."
    # voice "audio/voice_acting/chapter1_2/006.mp3"
    my "Yeah, sure!"
    show zena newstudent eyes_closed normal
    "She lets out a sigh of relief."
    show zena newstudent normal
    # voice "audio/voice_acting/chapter1_2/007.mp3"
    "???" "Thank you."
    "She takes a seat next to me."
    "The journey continues in silence."
    hide zena
    "{b}{u}Ten minutes later...{/u}{/b}"
    show zena newstudent eyes_closed normal
    "The girl has fallen asleep."
    "I wanted to talk to her... It's boring on this ride."
    "It shouldn't be too much longer, anyways."
    hide zena
    "{b}{u}Another ten minutes later...{/u}{/b}"
    show zena newstudent eyes_closed normal
    "Train Announcer" "We will now be arriving in: Chisick."
    "Ah. My stop."
    "I stand up, gathering my things."
    "The girl begins to wake up."
    show zena newstudent normal
    # voice "audio/voice_acting/chapter1_2/008.mp3"
    "???" "What stop is this..."
    # voice "audio/voice_acting/chapter1_2/009.mp3"
    my "Chisick."
    # voice "audio/voice_acting/chapter1_2/010.mp3"
    "???" "Ah..."
    "She stands up too."
    "Huh, she's getting off here too?"
    "The train slows to a halt."
    "We exit."

    scene bg city raining
    with wipeleft
    show zena newstudent normal
    "The rain is heavy."
    "I grab my umbrella."
    "She stands there for a moment, contemplating."
    # voice "audio/voice_acting/chapter1_2/011.mp3"
    my "Don't you have a coat or umbrella?"
    "I ask, curious and a bit concerned."
    "She shrugs."
    show zena newstudent eyes_closed normal
    # voice "audio/voice_acting/chapter1_2/012.mp3"
    "???" "I'll be fine."
    # voice "audio/voice_acting/chapter1_2/013.mp3"
    my "Okay..."
    hide zena
    with moveoutright
    "She quickly runs off."
    "I sigh, beginning to walk to my destination."

    scene bg stage
    with fade
    play music stage_theme fadein 0.5 loop fadeout 0.5
    "Phew... I made it..."
    # voice "audio/voice_acting/chapter1_2/014.mp3"
    "Employee" "Hey, you're late!"
    # voice "audio/voice_acting/chapter1_2/015.mp3"
    my "Sorry! The weather is terrible!"
    # voice "audio/voice_acting/chapter1_2/016.mp3"
    "Employee" "It's fine, don't worry!"
    "I set down my umbrella and take off my coat."
    "Time to get to work."
    "The first day of the New Year in my job..."
    "As a stage manager..."
    "Some idol group is performing here today, for a New Years concert."
    "I clap my hands, getting everyone's attention."
    # voice "audio/voice_acting/chapter1_2/017.mp3"
    my "Okay, everyone, let's begin setting the stage!"
    scene bg stage
    with flash
    "{b}{u}A few hours later...{/u}{/b}"
    "Finally, after hours of work, it's done."
    "The idol group has arrived already, and are waiting backstage."
    "I decide to pay them a visit with my free time."

    scene bg backstage
    with wipeleft
    "I enter the backstage area."
    # voice "audio/voice_acting/chapter1_2/018.mp3"
    my "Hello~?"
    "I call out."
    "Three girls turn their heads."
    show amari idol normal at left
    show angela idol normal at center
    show zena idol normal at right
    "I immediately recognise one of them."
    # voice "audio/voice_acting/chapter1_2/019.mp3"
    "???" "!!!"
    show zena idol eyes_closed normal
    "She looks away."
    show angela idol talk
    # voice "audio/voice_acting/chapter1_2/020.mp3"
    "???" "How can we help you?"
    "One of them asks."
    "I smile."
    # voice "audio/voice_acting/chapter1_2/021.mp3"
    my "I'm the stage manager here, thought I'd come meet you!"
    # voice "audio/voice_acting/chapter1_2/022.mp3"
    "???" "How sweet!"
    "She steps forward."
    # voice "audio/voice_acting/chapter1_2/023.mp3"
    angela "My name is Angela, nice to meet you! I'm the leader of our idol group!"
    # voice "audio/voice_acting/chapter1_2/024.mp3"
    angela "The one to the left of me is Amari!"
    show amari idol talk
    # voice "audio/voice_acting/chapter1_2/025.mp3"
    amari "Nice to meet you."
    # voice "audio/voice_acting/chapter1_2/026.mp3"
    angela "And-"
    show angela idol eyes_closed normal
    # voice "audio/voice_acting/chapter1_2/027.mp3"
    angela "Zena doesn't talk much."
    # voice "audio/voice_acting/chapter1_2/028.mp3"
    zena "..."
    # voice "audio/voice_acting/chapter1_2/029.mp3"
    my "Ah..."
    # voice "audio/voice_acting/chapter1_2/030.mp3"
    my "That's okay."
    # voice "audio/voice_acting/chapter1_2/031.mp3"
    my "Nice to meet you all!"
    # voice "audio/voice_acting/chapter1_2/032.mp3"
    my "Good luck with your show today! I'll be cheering you on!"
    show angela idol talk
    # voice "audio/voice_acting/chapter1_2/033.mp3"
    angela "Thank you~!"
    show amari idol eyes_closed normal
    # voice "audio/voice_acting/chapter1_2/034.mp3"
    amari "We'll do our best!"
    show zena idol normal
    # voice "audio/voice_acting/chapter1_2/035.mp3"
    zena "I'll perform the best I can..."
    "I smile."
    # voice "audio/voice_acting/chapter1_2/036.mp3"
    my "I'm sure you'll all do great!"

    scene black
    with fade
    stop music fadeout 0.5
    "I leave even happier than before."
    "Those girls seem really positive."
    "No wonder they're popular idols..."
    "I'm surprised to have met the girl from the train earlier."
    "I can't believe she's part of their group..."
    "Oh, it's a small world."
    "We finish preparations for the show, and the crowd files in."
    "And so, it begins."

    scene bg stage
    with flash
    play music artificial_interspace_theme fadein 0.5 loop fadeout 0.5
    show amari idol talk at left
    show angela idol talk at center
    show zena idol talk at right
    # voice "audio/voice_acting/chapter1_2/037.mp3"
    angela "Helloooo~!"
    # voice "audio/voice_acting/chapter1_2/038.mp3"
    angela "I'm Angela!"
    # voice "audio/voice_acting/chapter1_2/039.mp3"
    amari "I'm Amari!"
    # voice "audio/voice_acting/chapter1_2/040.mp3"
    zena "I'm Zena!"
    # voice "audio/voice_acting/chapter1_2/041.mp3"
    angela "We are The Artificial Interspace!"
    "The crowd cheers."
    # voice "audio/voice_acting/chapter1_2/042.mp3"
    angela "I hope you enjoy our performance for you today!"
    show amari idol eyes_closed talk
    # voice "audio/voice_acting/chapter1_2/043.mp3"
    amari "Happy New Years, everyone!!"
    "With a click of a button, the music begins."
    show amari idol eyes_closed normal
    show angela idol eyes_closed normal
    show zena idol eyes_closed normal
    "The girls all dance pretty well, and their singing is beautiful."
    "Their voices mix together perfectly."
    "Furthermore, the audience is completely immersed, having the time of their lives."
    "I even find myself enjoying it!"
    "I never really was a fan of idols before but these girls..."
    "Something changed inside me tonight."
    "Something..."
    scene bg stage
    with fade
    "{b}{u}A few hours later...{/u}{/b}"
    show amari idol normal at left
    show angela idol normal at center
    show zena idol normal at right
    "Before I know it, the show is coming to a close."
    # voice "audio/voice_acting/chapter1_2/044.mp3"
    amari "Did you enjoy that, everyone?"
    "The crowd roars."
    show amari idol eyes_closed normal
    # voice "audio/voice_acting/chapter1_2/045.mp3"
    amari "I'm glad~!"
    show angela idol talk
    # voice "audio/voice_acting/chapter1_2/046.mp3"
    angela "Thank you so much for coming, everyone! It's been so much fun!"
    # voice "audio/voice_acting/chapter1_2/047.mp3"
    angela "Hopefully we'll meet again soon!"
    # voice "audio/voice_acting/chapter1_2/048.mp3"
    angela "Goodbye~!"
    hide amari
    hide angela
    hide zena
    with moveoutleft
    "They exit the stage."
    "The crowd cheers, adrenaline high."
    "I'm left with a buzz I've never felt before."
    "It's... nice..."
    "However, we must now get everyone out and shut down the systems."
    "It's late now."
    "I get to work, using this dopamine kick to motivate me."

    scene bg backstage
    with fade
    play music stage_theme fadein 0.5 loop fadeout 0.5
    "I head backstage to check if the girls are still there."
    "They're gathering their things."
    show amari casual eyes_closed normal at left
    show angela casual eyes_closed normal at center
    show zena newstudent eyes_closed normal at right
    angela "We're finally done..."
    show amari casual eyes_closed talk
    amari "I hope you enjoyed the show~!"
    my "I did!!"
    amari "Yay!!"
    show angela casual talk
    angela "Thank you for helping us through the show! We couldn't have made it successful without you!"
    my "Aw, thanks."
    my "I didn't do that much..."
    my "Just working behind the scenes..."
    show zena newstudent talk
    zena "It's time to go."
    zena "Goodbye."
    hide zena
    with moveoutright
    "Zena rushes off."
    show angela casual eyes_closed normal
    "Angela lets out a chuckle."
    angela "She's so shy..."
    show amari casual normal
    amari "I hope we'll meet again!"
    my "Yeah, definitely!"
    my "Bye!"
    show angela casual talk
    angela "Bye!"
    amari "Byeee!"
    hide angela
    hide amari
    with moveoutright
    "They leave."
    "The sweet feeling remains."

    scene bg train night
    with fade
    play music chapter1_theme fadein 0.5 loop fadeout 0.5
    "I'm finally heading home."
    "It's very late, and I'm exhausted."
    "I struggle to stay awake through the long train ride."
    "Hopefully soon I'll be able to move into my new shared home..."
    
    scene black
    with fade
    "Today was a great start to the New Year."
    "I hope I can get to know those girls more. They seem really nice!"
    "I go to bed, buzzing with excitement."
    window hide
    centered "End of day."
    $ chapter1_day2_avail = True
    menu chapter1_day1_end:
        "Day 1 complete!"
        "Would you like to return to the chapter selection screen, or carry onto the next day?"
        "Chapter selection.":
            jump chapter_select
        "Carry on.":
            jump chapter1_day2