import arcade
#arcade in
populationstxt = open("project4.txt")
populationstxt.readlines()
#open file
#opening window
arcade.open_window(1000,1000)
arcade.start_render()
#start for loop to make rectangles
for line in populationstxt:
    line.split(",")
    state = populationstxt[0]
    pop_curr = populationstxt[1]
    change_pop = populationstxt[2]
    pop_curr-change_pop == per_change_pop
    per_change_pop/pop_curr == percent

    print(pop_curr)
    #trying to figure out change in populaiton by percent


#I got really stuck here and couldnt figure out how to get this working. As I write this its
# 10:45pm and will be sending an email saying the same thing. I have my PAl session tomorrow before we
# meet and am going to ask Matt on what I'm doing wrong. Have a nice day. ~Aidan



arcade.finish_render()
arcade.run()