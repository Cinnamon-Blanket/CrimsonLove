label start:
    camera:
        perspective True
    jump chapter_select

label chapter_select:
    menu chapter_page_select:
        "Please choose a page."
        "Page 1 (Chapters 1-4)":
            jump page1_select
    menu page1_select:
        "Please choose a chapter."
        "Chapter 1 (Part 1, Mora)":
            jump chapter1_select
        "Chapter 2 (Part 2, Mora)" if chapter2_avail:
            jump chapter2_select
        "Chapter 3 (Part 1, Hareka)" if chapter3_avail:
            jump chapter3_select
        "Chapter 4 (Part 2, Hareka)" if chapter4_avail:
            jump chapter4_select
    menu chapter1_select (screen="gridchoice", cols=1, rows=5):
        "Chapter 1\nPlease choose a day."
        "Day 1.":
            jump chapter1_day1
        "Day 2." if chapter1_day2_avail:
            jump chapter1_day2
        "Day 3." if chapter1_day3_avail:
            jump chapter1_day3
        "Day 4." if chapter1_day4_avail:
            jump chapter1_day4
        "Day 5." if chapter1_day5_avail:
            jump chapter1_day5
    menu chapter2_select (screen="gridchoice", cols=1, rows=3):
        "Chapter 2\nPlease choose a day."
        "Day 1.":
            jump chapter2_day1
        "Day 2." if chapter2_day2_avail:
            jump chapter2_day2
        "Day 3." if chapter2_day3_avail:
            jump chapter2_day3
    menu chapter3_select (screen="gridchoice", cols=3, rows=6):
        "Chapter 3\nPlease choose a day."
        "Day 1.":
            jump chapter3_day1
        "Day 2." if chapter3_day2_avail:
            jump chapter3_day2
        "Day 3." if chapter3_day3_avail:
            jump chapter3_day3
        "Day 4." if chapter3_day4_avail:
            jump chapter3_day4
        "Day 5." if chapter3_day5_avail:
            jump chapter3_day5
        "Day 6." if chapter3_day6_avail:
            jump chapter3_day6
        "Day 7." if chapter3_day7_avail:
            jump chapter3_day7
        "Day 8." if chapter3_day8_avail:
            jump chapter3_day8
        "Day 9." if chapter3_day9_avail:
            jump chapter3_day9
        "Day 10." if chapter3_day10_avail:
            jump chapter3_day10
        "Day 11." if chapter3_day11_avail:
            jump chapter3_day11
        "Day 12." if chapter3_day12_avail:
            jump chapter3_day12
        "Day 13." if chapter3_day13_avail:
            jump chapter3_day13
        "Day 14." if chapter3_day14_avail:
            jump chapter3_day14
    menu chapter4_select (screen="gridchoice", cols=2, rows=6):
        "Chapter 4\nPlease choose a day."
        "Day 1.":
            jump chapter4_day1
        "Day 2." if chapter4_day2_avail:
            jump chapter4_day2
        "Day 3." if chapter4_day3_avail:
            jump chapter4_day3
        "Day 4." if chapter4_day4_avail:
            jump chapter4_day4
        "Day 5." if chapter4_day5_route1_avail:
            jump chapter4_day5_route1
        "Day 5." if chapter4_day5_route2_avail:
            jump chapter4_day5_route2
        "Day 6." if chapter4_day6_route1_avail:
            jump chapter4_day6_route1
        #"Day 6." if chapter4_day6_route2_avail:
            #jump chapter4_day6_route2
        "Day 7." if chapter4_day7_route1_avail:
            jump chapter4_day7_route1
        #"Day 7." if chapter4_day7_route2_avail:
            #jump chapter4_day7_route2