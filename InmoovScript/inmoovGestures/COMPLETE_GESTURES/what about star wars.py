def whataboutstarwars():
    global MoveHeadRandom
    MoveHeadRandom=0
    global MoveBodyRandom
    MoveBodyRandom=0
    x = (random.randint(1, 3))
    if x == 1:
            fullspeed()
            i01.moveHead(130,149,87,80,100)
            AudioPlayer.playFile(RuningFolder+'/system/sounds/R2D2.mp3')
            sleep(1)
            i01.moveHead(155,31,87,80,100)
            sleep(1)
            i01.moveHead(130,31,87,80,100)
            sleep(1)
            i01.moveHead(90,90,87,80,100)
            sleep(0.5)
            i01.moveHead(90,90,87,80,70)
            sleep(1)
            relax()
    if x == 2:
            fullspeed()
            AudioPlayer.playFile(RuningFolder+'/system/sounds/Hello sir, I am C3po unicyborg relations.mp3')
            i01.moveHead(138,80)
            i01.moveArm("left",79,42,23,41)
            i01.moveArm("right",71,40,14,39)
            i01.moveHand("left",180,180,180,180,180,47)
            i01.moveHand("right",99,130,152,154,145,180)
            i01.moveTorso(90,90,90)
            sleep(1)
            i01.moveHead(116,80)
            i01.moveArm("left",85,93,42,16)
            i01.moveArm("right",87,93,37,18)
            i01.moveHand("left",124,82,65,81,41,143)
            i01.moveHand("right",59,53,89,61,36,21)
            i01.moveTorso(90,90,90)
            sleep(1)
            relax()
    if x == 3:
            i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
            i01.setHandSpeed("right", 1.0, 0.85, 1.0, 1.0, 1.0, 1.0)
            i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
            i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
            i01.setHeadSpeed(1.0, 0.90)
            i01.setTorsoSpeed(1.0, 1.0, 1.0)
            i01.moveHead(80,86)
            i01.moveArm("left",5,94,30,10)
            i01.moveArm("right",7,74,50,10)
            i01.moveHand("left",180,180,180,180,180,90)
            i01.moveHand("right",180,2,175,160,165,180)
            i01.moveTorso(90,90,90)
            AudioPlayer.playFile(RuningFolder+'/system/sounds/mmmmmmh, from the dark side you are.mp3')
            sleep(4.5)
            relax()      
            

            
