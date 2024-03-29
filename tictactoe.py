import random
def checkWin(board):
    for a in range(3):
        if board[3*a+0]==board[3*a+1] and board[3*a+1]==board[3*a+2]:
            if board[3*a+0] in ['x','o']:
                return board[3*a+0]
    for a in range(3):
        if board[a]==board[3+a] and board[3+a]==board[6+a]:
            if board[a] in ['x','o']:
                return board[a]
    if board[0]==board[4] and board[4]==board[8]:
            if board[0] in ['x','o']:
                return board[0]
    if board[2]==board[4] and board[4]==board[6]:
            if board[2] in ['x','o']:
                return board[2]
    return 'n'
def displayBoard(board):
    print "%s|%s|%s\n%s|%s|%s\n%s|%s|%s\n"%(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8])
def condenseList(toCondense):
    output=''
    for thing in toCondense:
        output+=str(thing)
    return output
def playAIGame(list1,list2,showtext=True):
    if showtext: print "Starting game between AI#%s and AI#%s"%(condenseList(list1),condenseList(list2))
    board=[' ']*9
    for i in range(5):
        for x in list1:
            if board[x] not in ['x','o']:
                board[x]='x'
                break
        if showtext: displayBoard(board)
        if checkWin(board)=='x':
            if showtext: print "AI#%s wins!"%(condenseList(list1))
            return 'x'
        for o in list2:
            if board[o] not in ['x','o']:
                board[o]='o'
                break
        if showtext: displayBoard(board)
        cWin=checkWin(board)
        if checkWin(board)=='o':
            if showtext: print "AI#%s wins!"%(condenseList(list2))
            return 'o'
    return 'e'
def simGames(length):
    king=random.sample([0,1,2,3,4,5,6,7,8],9)
    letter='x'
    reign=0
    winsdraws=[0,0]
    a=1
    while a<=length:
        print "Generation %i"%a
        challenger=random.sample([0,1,2,3,4,5,6,7,8],9)
        if letter=='x':
            result=playAIGame(king,challenger)
            if result=='x' or result=='e':
                if result=='x':
                    winsdraws[0]+=1
                elif result=='e':
                    winsdraws[1]+=1
                reign+=1
                print "The king, AI#%s's reign extends to %i!"%(condenseList(king),reign)
            elif result=='o':
                reign=0
                winsdraws=[0,0]
                letter='o'
                print "The challenger AI#%s has defeated the king!"%(condenseList(challenger))
                for i in range(9):
                    king[i]=challenger[i]
        elif letter=='o':
            result=playAIGame(challenger,king)
            if result=='o' or result=='e':
                if result=='o':
                    winsdraws[0]+=1
                elif result=='e':
                    winsdraws[1]+=1
                reign+=1
                print "The king, AI#%s's reign extends to %i!"%(condenseList(king),reign)
            elif result=='x':
                reign=0
                winsdraws=[0,0]
                letter='x'
                print "The challenger AI#%s has defeated the king!"%(condenseList(challenger))
                for i in range(9):
                    king[i]=challenger[i]
        print "The king has won %i games as king and drawn %i"%(winsdraws[0],winsdraws[1])
        a+=1
def testStrategy(strategy,games,letter,showtext=True,returnwdl=False):
    a=1
    wdl=[0,0,0]
    condensedStrategy=condenseList(strategy)
    print "Testing strategy %s"%condensedStrategy
    while a<=games:
        if showtext:
            print "Game %i"%a
        challenger=random.sample([0,1,2,3,4,5,6,7,8],9)
        if letter=='x':
            result=playAIGame(strategy,challenger,False)
        elif letter=='o':
            result=playAIGame(challenger,strategy,False)
        if result==letter:
            wdl[0]+=1
        elif result=='e':
            wdl[1]+=1
        else:
            wdl[2]+=1
        if showtext: print "Strategy %s has won %i times, drawn %i times, and lost %i times!"%(condensedStrategy,wdl[0],wdl[1],wdl[2])
        a+=1
    #if not showtext: print "Strategy %s has won %i times, drawn %i times, and lost %i times!"%(condensedStrategy,wdl[0],wdl[1],wdl[2])
    if returnwdl: return [condensedStrategy]+wdl
def testRandomStrategies(strategies):
    b=1
    results=[]
    while b<=strategies:
        strategy=random.sample([0,1,2,3,4,5,6,7,8],9)
        results.append(testStrategy(strategy,10000,'x',False,True))
        b+=1
    #file=open("results.txt","a")
    print "Strategy\tWins\tDraws\tLosses"
    for result in results:
        toprint=''
        for thing in result:
            toprint+=str(thing)
            toprint+='\t'
        #toprint+='\n'
        print toprint
        #file.write(toprint)
    #file.close()
def trs(strategies):
    testRandomStrategies(strategies)
def testInfiniteStrategies():
    b=0
    while True:
        #print b
        trs(100)
        b+=1
        a=''
        a=raw_input("Press enter to continue: ")
def tis():
    testInfiniteStrategies()
