### VARIABLE DEFINITIONS ###
default zena_affection = 0
default amari_affection = 0
default angela_affection = 0
default mora_affection = 0
default hareka_affection = 0
default chapter1_day2_avail = False
default chapter1_day3_avail = False
default chapter1_day4_avail = False
default chapter1_day5_avail = False
default chapter2_day2_avail = False
default chapter2_day3_avail = False
default chapter3_day2_avail = False
default chapter3_day3_avail = False
default chapter3_day4_avail = False
default chapter3_day5_avail = False
default chapter3_day6_avail = False
default chapter3_day7_avail = False
default chapter3_day8_avail = False
default chapter3_day9_avail = False
default chapter3_day10_avail = False
default chapter3_day11_avail = False
default chapter3_day12_avail = False
default chapter3_day13_avail = False
default chapter3_day14_avail = False
default chapter4_day2_avail = False
default chapter4_day3_avail = False
default chapter4_day4_avail = False
default chapter4_day5_route1_avail = False
default chapter4_day5_route2_avail = False
default chapter4_day6_route1_avail = False
default chapter4_day6_route2_avail = False
default chapter4_day7_route1_avail = False
default chapter4_day7_route2_avail = False
default chapter2_avail = False
default chapter3_avail = False
default chapter4_avail = False
default mora_death = False
default mora_almost_kill = False
default mora_push = False
default chapter1_day3_moraumbrella = False
define flash = Fade(.25, 0.0, .75, color="#fff")
transform t_xpos(x):
  xpos x
default mora_hobbies_unlock = False
default mora_job_unlock = False
default mora_workenjoy_failed_unlock = False
image white = Solid("#ffffff")
image blue = Solid("#0000FF")
define config.allow_underfull_grids = True
default chapter4_day4_menu1_answer1 = False
default chapter4_day4_menu1_answer2 = False
default chapter4_day5_route1_menu3_answer1 = False
default chapter4_day5_route1_menu3_answer2 = False

### CHARACTER DEFINITIONS ###
define my = Character("Myself", image="mc", voice_tag="mc")
image side mc = "images/mc_side_normal.png"
### ZENA ###
define zena = Character("Zena", image="zena", voice_tag="zena")
image side zena idol = "images/zena/idol/side_normal.png"
image side zena = "images/zena/newstudent/side_normal.png"
image side zena arbiter = "images/zena/arbiter/side_normal.png"
# IDOL #
image zena idol:
    "images/zena/idol/idol.png"
    zoom 1.75
image zena idol normal:
    "images/zena/idol/normal.png"
    zoom 1.75
image zena idol talk:
    "images/zena/idol/talk.png"
    zoom 1.75
image zena idol eyes_closed normal:
    "images/zena/idol/eyes_closed_normal.png"
    zoom 1.75
image zena idol eyes_closed talk:
    "images/zena/idol/eyes_closed_talk.png"
    zoom 1.75
# NEW STUDENT #
image zena newstudent normal:
    "images/zena/newstudent/normal.png"
    zoom 1.75
image zena newstudent talk:
    "images/zena/newstudent/talk.png"
    zoom 1.75
image zena newstudent eyes_closed normal:
    "images/zena/newstudent/eyes_closed_normal.png"
    zoom 1.75
image zena newstudent eyes_closed talk:
    "images/zena/newstudent/eyes_closed_talk.png"
    zoom 1.75
# STUDENT #
image zena student normal:
    "images/zena/student/normal.png"
    zoom 1.75
image zena student talk:
    "images/zena/student/talk.png"
    zoom 1.75
image zena student eyes_closed normal:
    "images/zena/student/eyes_closed_normal.png"
    zoom 1.75
image zena student eyes_closed talk:
    "images/zena/student/eyes_closed_talk.png"
    zoom 1.75
# ARBITER #
image zena arbiter normal:
    "images/zena/arbiter/normal.png"
    zoom 1.75
image zena arbiter talk:
    "images/zena/arbiter/talk.png"
    zoom 1.75
image zena arbiter eyes_closed normal:
    "images/zena/arbiter/eyes_closed_normal.png"
    zoom 1.75
image zena arbiter eyes_closed talk:
    "images/zena/arbiter/eyes_closed_normal.png"
    zoom 1.75

### ALESSA ###
define alessa = Character("Alessa")
# STUDENT #
image alessa student normal:
    "images/alessa/student/normal.png"
    zoom 1.75
image alessa student talk:
    "images/alessa/student/talk.png"
    zoom 1.75
image alessa student sad:
    "images/alessa/student/sad.png"
    zoom 1.75

### ANGELA ###
define angela = Character("Angela", image="angela", voice_tag="angela")
image side angela idol = "images/angela/idol/side_normal.png"
image side angela = "images/angela/casual/side_normal.png"
# IDOL #
image angela idol normal:
    "images/angela/idol/normal.png"
    zoom 1.75
image angela idol talk:
    "images/angela/idol/talk.png"
    zoom 1.75
image angela idol eyes_closed normal:
    "images/angela/idol/eyes_closed_normal.png"
    zoom 1.75
image angela idol eyes_closed talk:
    "images/angela/idol/eyes_closed_talk.png"
    zoom 1.75
# CASUAL #
image angela casual normal:
    "images/angela/casual/normal.png"
    zoom 1.75
image angela casual talk:
    "images/angela/casual/talk.png"
    zoom 1.75
image angela casual eyes_closed normal:
    "images/angela/casual/eyes_closed_normal.png"
    zoom 1.75
image angela casual eyes_closed talk:
    "images/angela/casual/eyes_closed_talk.png"
    zoom 1.75

### AMARI ###
define amari = Character("Amari", image="amari", voice_tag="amari")
image side amari idol = "images/amari/idol/side_normal.png"
image side amari = "images/amari/casual/side_normal.png"
# IDOL #
image amari idol normal:
    "images/amari/idol/normal.png"
    zoom 1.75
image amari idol talk:
    "images/amari/idol/talk.png"
    zoom 1.75
image amari idol eyes_closed normal:
    "images/amari/idol/eyes_closed_normal.png"
    zoom 1.75
image amari idol eyes_closed talk:
    "images/amari/idol/eyes_closed_talk.png"
    zoom 1.75
# CASUAL #
image amari casual normal:
    "images/amari/casual/normal.png"
    zoom 1.75
image amari casual talk:
    "images/amari/casual/talk.png"
    zoom 1.75
image amari casual eyes_closed normal:
    "images/amari/casual/eyes_closed_normal.png"
    zoom 1.75
image amari casual eyes_closed talk:
    "images/amari/casual/eyes_closed_talk.png"
    zoom 1.75

### ELI ###
define eli = Character("Eli", image="eli", voice_tag="eli")
image side eli = "images/employees/eli/side_normal.png"
# WORK #
image eli work normal:
    "images/employees/eli/normal.png"
    zoom 1.75
image eli work eyes_closed normal:
    "images/employees/eli/eyes_closed_normal.png"
    zoom 1.75

### CARA ###
define cara = Character("Cara", image="cara")
image side cara = "images/employees/cara/side_normal.png"
# WORK #
image cara work normal:
    "images/employees/cara/normal.png"
    zoom 1.75
image cara work eyes_closed normal:
    "images/employees/cara/eyes_closed_normal.png"
    zoom 1.75

### MORA ###
define mora = Character("Mora", image="mora", voice_tag="mora")
image side mora = "images/mora/arbiter/side_normal.png"
# ARBITER #
image mora arbiter normal:
    "images/mora/arbiter/normal.png"
    zoom 1.75
image mora arbiter eyes_closed normal:
    "images/mora/arbiter/eyes_closed_normal.png"
    zoom 1.75
image mora arbiter no_coat normal:
    "images/mora/arbiter/no_coat/normal.png"
    zoom 1.75
image mora arbiter no_coat eyes_closed normal:
    "images/mora/arbiter/no_coat/eyes_closed_normal.png"
    zoom 1.75
image mora arbiter no_coat blush:
    "images/mora/arbiter/no_coat/blush.png"
    zoom 1.75
image mora arbiter no_coat eyes_closed blush:
    "images/mora/arbiter/no_coat/eyes_closed_blush.png"
    zoom 1.75
# UNDERWEAR #
image mora underwear coat normal:
    "images/mora/underwear/coat/normal.png"
    zoom 1.75
image mora underwear coat eyes_closed normal:
    "images/mora/underwear/coat/eyes_closed_normal.png"
    zoom 1.75
image mora underwear normal:
    "images/mora/underwear/normal.png"
    zoom 1.75
image mora underwear eyes_closed normal:
    "images/mora/underwear/eyes_closed_normal.png"
    zoom 1.75
# CASUAL #
image mora casual normal:
    "images/mora/casual/normal.png"
    zoom 1.75
image mora casual eyes_closed normal:
    "images/mora/casual/eyes_closed_normal.png"
    zoom 1.75
image mora casual ponytail normal:
    "images/mora/casual/ponytail/normal.png"
    zoom 1.75
image mora casual ponytail eyes_closed normal:
    "images/mora/casual/ponytail/eyes_closed_normal.png"
    zoom 1.75
image mora casual coat normal:
    "images/mora/casual/coat/normal.png"
    zoom 1.75
image mora casual coat eyes_closed normal:
    "images/mora/casual/coat/eyes_closed_normal.png"
    zoom 1.75
image mora casual coat ponytail normal:
    "images/mora/casual/coat/ponytail/normal.png"
    zoom 1.75
image mora casual coat ponytail eyes_closed normal:
    "images/mora/casual/coat/ponytail/eyes_closed_normal.png"
    zoom 1.75
# DATE #
image mora date normal:
    "images/mora/date/normal.png"
    zoom 1.75
image mora date eyes_closed normal:
    "images/mora/date/eyes_closed_normal.png"
    zoom 1.75
image mora date smile:
    "images/mora/date/smile.png"
    zoom 1.75
image mora date eyes_closed smile:
    "images/mora/date/eyes_closed_smile.png"
    zoom 1.75

### HAREKA ###
define hareka = Character("Hareka", image="hareka", voice_tag="hareka")
image side hareka = "images/hareka/arbiter/side_normal.png"
define harekai = Character("Hareka - Interface", image="hareka" and "harekai", voice_tag="hareka")
image side harekai = "images/hareka/arbiter/alt/side_normal.png"
# ARBITER #
image hareka arbiter normal:
    "images/hareka/arbiter/normal.png"
    zoom 1.75
image hareka arbiter eyes_closed normal:
    "images/hareka/arbiter/eyes_closed_normal.png"
    zoom 1.75
image hareka arbiter smile:
    "images/hareka/arbiter/smile.png"
    zoom 1.75
image hareka arbiter eyes_closed smile:
    "images/hareka/arbiter/eyes_closed_smile.png"
    zoom 1.75
image hareka arbiter corrupted:
    "images/hareka/arbiter/corrupted.png"
    zoom 1.75
image hareka arbiter hair_down normal:
    "images/hareka/arbiter/hair_down/normal.png"
    zoom 1.75
image hareka arbiter hair_down eyes_closed normal:
    "images/hareka/arbiter/hair_down/eyes_closed_normal.png"
    zoom 1.75
image hareka arbiter hair_down smile:
    "images/hareka/arbiter/hair_down/smile.png"
    zoom 1.75
image hareka arbiter hair_down eyes_closed smile:
    "images/hareka/arbiter/hair_down/eyes_closed_smile.png"
    zoom 1.75
image hareka arbiter no_coat normal:
    "images/hareka/arbiter/no_coat/normal.png"
    zoom 1.75
image hareka arbiter no_coat eyes_closed normal:
    "images/hareka/arbiter/no_coat/eyes_closed_normal.png"
    zoom 1.75
image hareka arbiter no_coat smile:
    "images/hareka/arbiter/no_coat/smile.png"
    zoom 1.75
image hareka arbiter no_coat eyes_closed smile:
    "images/hareka/arbiter/no_coat/eyes_closed_smile.png"
    zoom 1.75
image hareka arbiter no_coat hair_down normal:
    "images/hareka/arbiter/no_coat/hair_down/normal.png"
    zoom 1.75
image hareka arbiter no_coat hair_down eyes_closed normal:
    "images/hareka/arbiter/no_coat/hair_down/eyes_closed_normal.png"
    zoom 1.75
image hareka arbiter no_coat hair_down smile:
    "images/hareka/arbiter/no_coat/hair_down/smile.png"
    zoom 1.75
image hareka arbiter no_coat hair_down eyes_closed smile:
    "images/hareka/arbiter/no_coat/hair_down/eyes_closed_smile.png"
    zoom 1.75
image hareka arbiter no_coat hair_down corrupted:
    "images/hareka/arbiter/no_coat/hair_down/corrupted.png"
    zoom 1.75
image hareka arbiter alt normal:
    "images/hareka/arbiter/alt/normal.png"
    zoom 1.75
image hareka arbiter alt eyes_closed normal:
    "images/hareka/arbiter/alt/eyes_closed_normal.png"
    zoom 1.75
image hareka arbiter alt smile:
    "images/hareka/arbiter/alt/smile.png"
    zoom 1.75
image hareka arbiter alt eyes_closed smile:
    "images/hareka/arbiter/alt/eyes_closed_smile.png"
    zoom 1.75
image hareka arbiter alt blush:
    "images/hareka/arbiter/alt/blush.png"
    zoom 1.75
image hareka arbiter alt eyes_closed blush:
    "images/hareka/arbiter/alt/eyes_closed_blush.png"
    zoom 1.75
image hareka arbiter alt blush smile:
    "images/hareka/arbiter/alt/blush_smile.png"
    zoom 1.75
image hareka arbiter alt eyes_closed blush smile:
    "images/hareka/arbiter/alt/eyes_closed_blush_smile.png"
    zoom 1.75
image hareka arbiter alt hair_down normal:
    "images/hareka/arbiter/alt/hair_down/normal.png"
    zoom 1.75
image hareka arbiter alt hair_down eyes_closed normal:
    "images/hareka/arbiter/alt/hair_down/eyes_closed_normal.png"
    zoom 1.75
image hareka arbiter alt hair_down smile:
    "images/hareka/arbiter/alt/hair_down/smile.png"
    zoom 1.75
image hareka arbiter alt hair_down eyes_closed smile:
    "images/hareka/arbiter/alt/hair_down/eyes_closed_smile.png"
    zoom 1.75
image hareka arbiter alt messy normal:
    "images/hareka/arbiter/alt/messy/normal.png"
    zoom 1.75
image hareka arbiter alt messy eyes_closed normal:
    "images/hareka/arbiter/alt/messy/eyes_closed_normal.png"
    zoom 1.75
image hareka arbiter alt messy smile:
    "images/hareka/arbiter/alt/messy/smile.png"
    zoom 1.75
image hareka arbiter alt messy eyes_closed smile:
    "images/hareka/arbiter/alt/messy/eyes_closed_smile.png"
    zoom 1.75
image hareka arbiter ringdev normal:
    "images/hareka/arbiter/ringdev/normal.png"
    zoom 1.75
image hareka arbiter ringdev eyes_closed normal:
    "images/hareka/arbiter/ringdev/eyes_closed_normal.png"
    zoom 1.75
image hareka arbiter ringdev smile:
    "images/hareka/arbiter/ringdev/smile.png"
    zoom 1.75
image hareka arbiter ringdev eyes_closed smile:
    "images/hareka/arbiter/ringdev/eyes_closed_smile.png"
    zoom 1.75
image hareka arbiter ringdev blur:
    "images/hareka/arbiter/ringdev/blur.png"
    zoom 1.75
# CASUAL #
image hareka casual normal:
    "images/hareka/casual/normal.png"
    zoom 1.75
image hareka casual eyes_closed normal:
    "images/hareka/casual/eyes_closed_normal.png"
    zoom 1.75
image hareka casual hair_up normal:
    "images/hareka/casual/hair_up/normal.png"
    zoom 1.75
image hareka casual hair_up eyes_closed normal:
    "images/hareka/casual/hair_up/eyes_closed_normal.png"
    zoom 1.75
# CASUAL 2 #
image hareka casual_2 normal:
    "images/hareka/casual_2/normal.png"
    zoom 1.75
image hareka casual_2 eyes_closed normal:
    "images/hareka/casual_2/eyes_closed_normal.png"
    zoom 1.75
image hareka casual_2 smile:
    "images/hareka/casual_2/smile.png"
    zoom 1.75
image hareka casual_2 eyes_closed smile:
    "images/hareka/casual_2/eyes_closed_smile.png"
    zoom 1.75
image hareka casual_2 hair_down normal:
    "images/hareka/casual_2/hair_down/normal.png"
    zoom 1.75
image hareka casual_2 hair_down eyes_closed normal:
    "images/hareka/casual_2/hair_down/eyes_closed_normal.png"
    zoom 1.75
image hareka casual_2 hair_down smile:
    "images/hareka/casual_2/hair_down/smile.png"
    zoom 1.75
image hareka casual_2 hair_down eyes_closed smile:
    "images/hareka/casual_2/hair_down/eyes_closed_smile.png"
    zoom 1.75

### AMITA ###
define amita = Character("Amita", image="amita", voice_tag="amita")
image side amita = "images/amita/star/side_normal.png"
image side amita arbiter = "images/amita/arbiter/side_normal.png"
# STAR #
image amita star normal:
    "images/amita/star/normal.png"
    zoom 1.75
image amita star eyes_closed normal:
    "images/amita/star/eyes_closed_normal.png"
    zoom 1.75
image amita star sad:
    "images/amita/star/sad.png"
    zoom 1.75
image amita star eyes_closed sad:
    "images/amita/star/eyes_closed_sad.png"
    zoom 1.75
# ARBITER #
image amita arbiter normal:
    "images/amita/arbiter/normal.png"
    zoom 1.75
image amita arbiter eyes_closed normal:
    "images/amita/arbiter/eyes_closed_normal.png"
    zoom 1.75
image amita arbiter sad:
    "images/amita/arbiter/sad.png"
    zoom 1.75
image amita arbiter eyes_closed sad:
    "images/amita/arbiter/eyes_closed_sad.png"
    zoom 1.75

### LILY ###
define lily = Character("Lily", image="lily", voice_tag="lily")
image side lily = "images/lily/scientist/side_normal.png"
# SCIENTIST #
image lily scientist normal:
    "images/lily/scientist/normal.png"
    zoom 1.75
image lily scientist eyes_closed normal:
    "images/lily/scientist/eyes_closed_normal.png"
    zoom 1.75

### KANA ###
define kana = Character("Kana", image="kana", voice_tag="kana")
image side kana = "images/kana/arbiter/side_normal.png"
# ARBITER #
image kana arbiter normal:
    "images/kana/arbiter/normal.png"
    zoom 1.75
image kana arbiter eyes_closed normal:
    "images/kana/arbiter/eyes_closed_normal.png"
    zoom 1.75

### INTERFACE ###
define interface = Character("The Interface", image="interface", voice_tag="interface")
image side interface = "images/interface/arbiter/side_normal.png"
# ARBITER #
image interface arbiter normal:
    "images/interface/arbiter/normal.png"
    zoom 1.75
image interface arbiter eyes_closed normal:
    "images/interface/arbiter/eyes_closed_normal.png"
    zoom 1.75
image interface arbiter shocked:
    "images/interface/arbiter/shocked.png"
    zoom 1.75
image interface arbiter smile:
    "images/interface/arbiter/smile.png"
    zoom 1.75
image interface arbiter eyes_closed smile:
    "images/interface/arbiter/eyes_closed_smile.png"
    zoom 1.75
# SCHOOL #
image interface school normal:
    "images/interface/school/normal.png"
    zoom 1.75
image interface school eyes_closed normal:
    "images/interface/school/eyes_closed_normal.png"
    zoom 1.75
# CASUAL #
image interface casual normal:
    "images/interface/casual/normal.png"
    zoom 1.75
image interface casual eyes_closed normal:
    "images/interface/casual/eyes_closed_normal.png"
    zoom 1.75
# CASUAL 2 #
image interface casual_2 normal:
    "images/interface/casual_2/normal.png"
    zoom 1.75
image interface casual_2 eyes_closed normal:
    "images/interface/casual_2/eyes_closed_normal.png"
    zoom 1.75

# MILLY #
define milly = Character("Milly", image="milly", voice_tag="milly")
image side milly = "images/milly/school/side_normal.png"
# SCHOOL #
image milly school normal:
    "images/milly/school/normal.png"
    zoom 1.75
image milly school eyes_closed normal:
    "images/milly/school/eyes_closed_normal.png"
    zoom 1.75
image milly school sad:
    "images/milly/school/sad.png"
    zoom 1.75
image milly school eyes_closed sad:
    "images/milly/school/eyes_closed_sad.png"
    zoom 1.75

# RILEY #
define riley = Character("Riley", image="riley", voice_tag="riley")
image side riley = "images/riley/arbiter/side_normal.png"
# ARBITER #
image riley arbiter normal:
    "images/riley/arbiter/normal.png"
    zoom 1.75
image riley arbiter eyes_closed normal:
    "images/riley/arbiter/eyes_closed_normal.png"
    zoom 1.75
image riley arbiter no_coat normal:
    "images/riley/arbiter/no_coat/normal.png"
    zoom 1.75
image riley arbiter no_coat eyes_closed normal:
    "images/riley/arbiter/no_coat/eyes_closed_normal.png"
    zoom 1.75
image riley arbiter alt normal:
    "images/riley/arbiter/alt/normal.png"
    zoom 1.75
image riley arbiter alt eyes_closed normal:
    "images/riley/arbiter/alt/eyes_closed_normal.png"
    zoom 1.75
image riley arbiter alt_2 normal:
    "images/riley/arbiter/alt_2/normal.png"
    zoom 1.75
image riley arbiter alt_2 eyes_closed normal:
    "images/riley/arbiter/alt_2/eyes_closed_normal.png"
    zoom 1.75

# LIA #
define lia = Character("Lia", image="lia", voice_tag="lia")
image side lia = "images/lia/casual/side_normal.png"
# CASUAL #
image lia casual normal:
    "images/lia/casual/normal.png"
    zoom 1.75
image lia casual eyes_closed normal:
    "images/lia/casual/eyes_closed_normal.png"
    zoom 1.75

# HEAD #
define head = Character("Head", image="head", voice_tag="head")
image side head = "images/head/head_uni/side_smile.png"
# HEAD UNI #
image head head_uni normal:
    "images/head/head_uni/normal.png"
    zoom 1.75
image head head_uni eyes_closed normal:
    "images/head/head_uni/eyes_closed_normal.png"
    zoom 1.75
image head head_uni smile:
    "images/head/head_uni/smile.png"
    zoom 1.75
image head head_uni eyes_closed smile:
    "images/head/head_uni/eyes_closed_smile.png"
    zoom 1.75
image head head_uni drunk:
    "images/head/head_uni/drunk.png"
    zoom 1.75
image head head_uni eyes_closed drunk:
    "images/head/head_uni/eyes_closed_drunk.png"
    zoom 1.75

# HEAD'S BODYGUARDS #
define bg1 = Character("Bodyguard #1", image="bodyguard 1", voice_tag="bodyguard 1")
image side bodyguard 1 = "images/head/bodyguards/one/side_normal.png"
define bg2 = Character ("Bodyguard #2", image="bodyguard 2", voice_tag="bodyguard 2")
image side bodyguard 2 = "images/head/bodyguards/two/side_normal.png"
# BODYGUARD UNI #
image bodyguard 1 normal:
    "images/head/bodyguards/one/normal.png"
    zoom 1.75
image bodyguard 1 eyes_closed normal:
    "images/head/bodyguards/one/eyes_closed_normal.png"
    zoom 1.75
image bodyguard 2 normal:
    "images/head/bodyguards/two/normal.png"
    zoom 1.75
image bodyguard 2 eyes_closed_normal:
    "images/head/bodyguards/two/eyes_closed_normal.png"
    zoom 1.75

### BACKGROUND DEFINITIONS ###
image bg apartment exterior = "images/backgrounds/Apartment_Exterior.png"
image bg apartment exterior night = "images/backgrounds/Apartment_Exterior_Night.png"
image bg bathroom = "images/backgrounds/Bathroom.png"
image bg bathroom foggy = "images/backgrounds/Bathroom_Foggy.png"
image bg bedroom day = "images/backgrounds/Bedroom_Day.png"
image bg bedroom evening = "images/backgrounds/Bedroom_Evening.png"
image bg bedroom night = "images/backgrounds/Bedroom_Night.png"
image bg bedroom night dark = "images/backgrounds/Bedroom_Night_Dark.png"
image bg cafeteria day = "images/backgrounds/Cafeteria_Day.png"
image bg city afternoon = "images/backgrounds/City_Afternoon.png"
image bg city morning = "images/backgrounds/City_Morning.png"
image bg city night = "images/backgrounds/City_Night.png"
image bg city raining = "images/backgrounds/City_Raining.png"
image bg classroom day = "images/backgrounds/Classroom_Day.png"
image bg futon room = "images/backgrounds/Futon_Room.png"
image bg futon room night = "images/backgrounds/Futon_Room_Night.png"
image bg kitchen day = "images/backgrounds/Kitchen_Day.png"
image bg kitchen night = "images/backgrounds/Kitchen_Night.png"
image bg laundromat = "images/backgrounds/Laundromat.png"
image bg living room dark = "images/backgrounds/Livingroom_Dark.png"
image bg living room day = "images/backgrounds/Livingroom_Day.png"
image bg living room night = "images/backgrounds/Livingroom_Night.png"
image bg onsen building = "images/backgrounds/Onsen_Building.png"
image bg onsen building night = "images/backgrounds/Onsen_Building_Night.png"
image bg outdoor stairs = "images/backgrounds/Outdoor_Stairs.png"
image bg restaurant a = "images/backgrounds/Restaurant_A.png"
image bg restaurant b = "images/backgrounds/Restaurant_B.png"
image bg school hallway = "images/backgrounds/School_Hallway_Day.png"
image bg sitting room = "images/backgrounds/Sitting_Room.png"
image bg sitting room dark = "images/backgrounds/Sitting_Room_Dark.png"
image bg small apartment kitchen = "images/backgrounds/Small_Apartment_Kitchen.png"
image bg small apartment kitchen night = "images/backgrounds/Small_Apartment_Kitchen_Night.png"
image bg street autumn day = "images/backgrounds/Street_Autumn_Day.png"
image bg street autumn evening = "images/backgrounds/Street_Autumn_Evening.png"
image bg street autumn night = "images/backgrounds/Street_Autumn_Night.png"
image bg street spring day = "images/backgrounds/Street_Spring_Day.png"
image bg street spring evening = "images/backgrounds/Street_Spring_Evening.png"
image bg street spring night = "images/backgrounds/Street_Spring_Night.png"
image bg street spring rain = "images/backgrounds/Street_Spring_Rain.png"
image bg street summer day = "images/backgrounds/Street_Summer_Day.png"
image bg street summer evening = "images/backgrounds/Street_Summer_Evening.png"
image bg street summer night = "images/backgrounds/Street_Summer_Night.png"
image bg street summer rain = "images/backgrounds/Street_Summer_Rain.png"
image bg street summer stars = "images/backgrounds/Street_Summer_Stars.png"
image bg train beach = "images/backgrounds/Train_beach.png"
image bg train day = "images/backgrounds/Train_Day.png"
image bg train day rain = "images/backgrounds/Train_Day_Rain.png"
image bg train evening = "images/backgrounds/Train_Evening.png"
image bg train night = "images/backgrounds/Train_Night.png"
image bg train night rain = "images/backgrounds/Train_Night_Rain.png"
image bg train tunnel = "images/backgrounds/Train_Tunnel.png"
image bg stage = "images/backgrounds/stage.png"
image bg backstage = "images/backgrounds/backstage.png"
image vignette = "images/backgrounds/Vignette.png"
image bg office day:
    "images/backgrounds/office_day.png"
    zoom 2.4
image water:
    "images/backgrounds/water.png"
    zoom 1.6
    ypos 1.2
image bg park:
    "images/backgrounds/park.png"
    zoom 2.4
image bg jail:
    "images/backgrounds/jail.png"
    zoom 2.4
image bg library:
    "images/backgrounds/library_rain.png"
    zoom 2.4
image bg office evening:
    "images/backgrounds/office_evening.png"
    zoom 2.4

### MUSIC ###
define audio.chapter1_theme = "audio/chapter1_theme.mp3"
define audio.stage_theme = "audio/stage_theme.mp3"
define audio.artificial_interspace_theme = "audio/artificial_interspace_theme.mp3"
define audio.mora_theme = "audio/mora_theme.mp3"
define audio.love_theme = "audio/love_theme.mp3"
define audio.arbiter_office_theme = "audio/arbiter_office_theme.mp3"
define audio.hareka_theme = "audio/hareka_theme.mp3"
define audio.interface_theme = "audio/interface_theme.mp3"
define audio.revenge_theme = "audio/revenge_theme.mp3"