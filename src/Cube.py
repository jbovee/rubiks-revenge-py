import numpy as np
import random as rand
import operator as op
from collections import Counter

class Cube:

    def __init__(self):
        self.faces = np.array([[['w','w','w','w'],
                                ['w','w','w','w'],
                                ['w','w','w','w'],
                                ['w','w','w','w']],
                                [['r','r','r','r'],
                                ['r','r','r','r'],
                                ['r','r','r','r'],
                                ['r','r','r','r']],
                                [['y','y','y','y'],
                                ['y','y','y','y'],
                                ['y','y','y','y'],
                                ['y','y','y','y']],
                                [['o','o','o','o'],
                                ['o','o','o','o'],
                                ['o','o','o','o'],
                                ['o','o','o','o']],
                                [['b','b','b','b'],
                                ['b','b','b','b'],
                                ['b','b','b','b'],
                                ['b','b','b','b']],
                                [['g','g','g','g'],
                                ['g','g','g','g'],
                                ['g','g','g','g'],
                                ['g','g','g','g']]])

        self.moves = np.array(['U','D','L','R','F','B','u','d','l','r','f','b','Uu','Dd','Ll','Rr','Ff','Bb','U2','D2','L2','R2','F2','B2','u2','d2','l2','r2','f2','b2','Uu2','Dd2','Ll2','Rr2','Ff2','Bb2'])

    def printCube(self):
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in self.faces[4]]))
        for y in range(0,4):
            print('\n'.join([''.join(['{:3}'.format(self.faces[x][y][z]) for x in range(0,4) for z in range(0,4)])]))
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in self.faces[5]]))

    def move(self,moveType,direction):
        if moveType <= 17:
            self.quarterTurn(moveType,direction)
        else:
            self.quarterTurn(moveType%18,direction)
            self.quarterTurn(moveType%18,direction)

    def quarterTurn(self,moveType,direction):
        if moveType == 0: #U
            if direction:
                self.xRegTurn(0)
                self.rotateFace(4,True)
            else:
                self.xAntiTurn(0)
                self.rotateFace(4,False)
        elif moveType == 1: #D
            if direction:
                self.xAntiTurn(3)
                self.rotateFace(5,True)
            else:
                self.xRegTurn(3)
                self.rotateFace(5,False)
        elif moveType == 2: #L
            self.XtoY()
            if direction:
                self.xRegTurn(0)
                self.rotateFace(4,True)
            else:
                self.xAntiTurn(0)
                self.rotateFace(4,False)
            self.YtoX()
        elif moveType == 3: #R
            self.XtoY()
            if direction:
                self.xAntiTurn(3)
                self.rotateFace(5,True)
            else:
                self.xRegTurn(3)
                self.rotateFace(5,False)
            self.YtoX()
        elif moveType == 4: #F
            self.XtoZ()
            if direction:
                self.xRegTurn(0)
                self.rotateFace(4,True)
            else:
                self.xAntiTurn(0)
                self.rotateFace(4,False)
            self.ZtoX()
        elif moveType == 5: #B
            self.XtoZ()
            if direction:
                self.xAntiTurn(3)
                self.rotateFace(5,True)
            else:
                self.xRegTurn(3)
                self.rotateFace(5,False)
            self.ZtoX()
        elif moveType == 6: #u
            if direction:
                self.xRegTurn(1)
            else:
                self.xAntiTurn(1)
        elif moveType == 7: #d
            if direction:
                self.xAntiTurn(2)
            else:
                self.xRegTurn(2)
        elif moveType == 8: #l
            self.XtoY()
            if direction:
                self.xRegTurn(1)
            else:
                self.xAntiTurn(1)
            self.YtoX()
        elif moveType == 9: #r
            self.XtoY()
            if direction:
                self.xAntiTurn(2)
            else:
                self.xRegTurn(2)
            self.YtoX()
        elif moveType == 10: #f
            self.XtoZ()
            if direction:
                self.xRegTurn(1)
            else:
                self.xAntiTurn(1)
            self.ZtoX()
        elif moveType == 11: #b
            self.XtoZ()
            if direction:
                self.xAntiTurn(2)
            else:
                self.xRegTurn(2)
            self.ZtoX()
        elif moveType == 12: #Uu
            if direction:
                self.xRegTurn(0)
                self.xRegTurn(1)
                self.rotateFace(4,True)
            else:
                self.xAntiTurn(0)
                self.xAntiTurn(1)
                self.rotateFace(4,False)
        elif moveType == 13: #Dd
            if direction:
                self.xAntiTurn(2)
                self.xAntiTurn(3)
                self.rotateFace(5,True)
            else:
                self.xRegTurn(2)
                self.xRegTurn(3)
                self.rotateFace(5,False)
        elif moveType == 14: #Ll
            self.XtoY()
            if direction:
                self.xRegTurn(0)
                self.xRegTurn(1)
                self.rotateFace(4,True)
            else:
                self.xAntiTurn(0)
                self.xAntiTurn(1)
                self.rotateFace(4,False)
            self.YtoX()
        elif moveType == 15: #Rr
            self.XtoY()
            if direction:
                self.xAntiTurn(2)
                self.xAntiTurn(3)
                self.rotateFace(5,True)
            else:
                self.xRegTurn(2)
                self.xRegTurn(3)
                self.rotateFace(5,False)
            self.YtoX()
        elif moveType == 16: #Ff
            self.XtoZ()
            if direction:
                self.xRegTurn(0)
                self.xRegTurn(1)
                self.rotateFace(4,True)
            else:
                self.xAntiTurn(0)
                self.xAntiTurn(1)
                self.rotateFace(4,False)
            self.ZtoX()
        elif moveType == 17: #Bb
            self.XtoZ()
            if direction:
                self.xAntiTurn(2)
                self.xAntiTurn(3)
                self.rotateFace(5,True)
            else:
                self.xRegTurn(2)
                self.xRegTurn(3)
                self.rotateFace(5,False)
            self.ZtoX()

    def XtoY(self):
        self.rotateFace(0,True)
        self.rotateFace(2,False)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, self.faces[4])
        np.copyto(self.faces[4], self.faces[3])
        self.rotateFace(4,True)
        np.copyto(self.faces[3], self.faces[5])
        self.rotateFace(3,True)
        np.copyto(self.faces[5], self.faces[1])
        self.rotateFace(5,True)
        np.copyto(self.faces[1], temp)
        self.rotateFace(1,True)

    def XtoZ(self):
        self.rotateFace(1,True)
        self.rotateFace(3,False)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, self.faces[0])
        np.copyto(self.faces[0], self.faces[5])
        np.copyto(self.faces[5], self.faces[2])
        self.rotateFace(5,False)
        self.rotateFace(5,False)
        np.copyto(self.faces[2], self.faces[4])
        self.rotateFace(2,False)
        self.rotateFace(2,False)
        np.copyto(self.faces[4], temp)

    def YtoX(self):
        self.rotateFace(0,False)
        self.rotateFace(2,True)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, self.faces[4])
        np.copyto(self.faces[4], self.faces[1])
        self.rotateFace(4,False)
        np.copyto(self.faces[1], self.faces[5])
        self.rotateFace(1,False)
        np.copyto(self.faces[5], self.faces[3])
        self.rotateFace(5,False)
        np.copyto(self.faces[3], temp)
        self.rotateFace(3,False)

    def ZtoX(self):
        self.rotateFace(1,False)
        self.rotateFace(3,True)
        temp = np.full([4,4], '', dtype=np.str)
        np.copyto(temp, self.faces[0])
        np.copyto(self.faces[0], self.faces[4])
        np.copyto(self.faces[4], self.faces[2])
        self.rotateFace(4,False)
        self.rotateFace(4,False)
        np.copyto(self.faces[2], self.faces[5])
        self.rotateFace(2,False)
        self.rotateFace(2,False)
        np.copyto(self.faces[5], temp)

    def xRegTurn(self,row):
        temp = np.full([6,4,4], '', dtype=np.str)
        tempFace = np.full([4,4], '', dtype=np.str)
        np.copyto(tempFace, self.faces[0][:])
        for x in range(0,3):
            np.copyto(temp[x][row], self.faces[x+1][row])
        np.copyto(temp[3][:], tempFace)
        if row == 0:
            for x in range(0,4):
                np.copyto(temp[x][1:], self.faces[x][1:])
        elif row == 1:
            for x in range(0,4):
                np.copyto(temp[x][0], self.faces[x][0])
                np.copyto(temp[x][2:], self.faces[x][2:])
        elif row == 2:
            for x in range(0,4):
                np.copyto(temp[x][:2], self.faces[x][:2])
                np.copyto(temp[x][3], self.faces[x][3])
        elif row == 3:
            for x in range(0,4):
                np.copyto(temp[x][:3], self.faces[x][:3])
        np.copyto(temp[4:], self.faces[4:])
        np.copyto(self.faces, temp)

    def xAntiTurn(self,row):
        temp = np.full([6,4,4], '', dtype=np.str)
        tempFace = np.full([4,4], '', dtype=np.str)
        np.copyto(tempFace, self.faces[3][:])
        for x in range(3,0,-1):
            np.copyto(temp[x][row], self.faces[x-1][row])
        np.copyto(temp[0][:], tempFace)
        if row == 0:
            for x in range(0,4):
                np.copyto(temp[x][1:], self.faces[x][1:])
        elif row == 1:
            for x in range(0,4):
                np.copyto(temp[x][0], self.faces[x][0])
                np.copyto(temp[x][2:], self.faces[x][2:])
        elif row == 2:
            for x in range(0,4):
                np.copyto(temp[x][:2], self.faces[x][:2])
                np.copyto(temp[x][3], self.faces[x][3])
        elif row == 3:
            for x in range(0,4):
                np.copyto(temp[x][:3], self.faces[x][:3])
        np.copyto(temp[4:], self.faces[4:])
        np.copyto(self.faces, temp)

    def rotateFace(self,face, direction):
        if direction:
            self.faces[face] = np.rot90(self.faces[face],3)
        else:
            self.faces[face] = np.rot90(self.faces[face])

    def scramble(self,n):
        for i in range(0,n):
            tNum = rand.randint(0,35)
            tBool = bool(rand.getrandbits(1))
            self.move(tNum,tBool)

    def faceFitness(self,*args):
        if len(args) == 1 and isinstance(args[0], int):
            flatFace = self.faces[args[0]].flatten().tolist()
            faceCounts = {'w': flatFace.count('w'), 'r': flatFace.count('r'), 'y': flatFace.count('y'), 'o': flatFace.count('o'), 'b': flatFace.count('b'), 'g': flatFace.count('g')}
            sortedCounts = sorted(faceCounts.items(), key=op.itemgetter(1), reverse=True)
            return (sortedCounts[0][0],sortedCounts[0][1])
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], str):
            flatFace = self.faces[args[0]].flatten().tolist()
            return flatFace.count(args[1])

    def fitness1(self):
        faces = self.faces.tolist()
        goalFaces = ['w','r','y','o','b','g']
        faceTotals = [sum([self.faces[x][y].tolist().count(goalFaces[x]) for y in range(0,4)]) for x in range(0,6)]
        return sum(faceTotals)

    def fitness2(self):
        centerOptions = ['w','r','y','o','b','g']
        centers = self.faces[:,1:3,1:3]
        tempCent = np.full([6,4], '', dtype=np.str)
        faceColors = np.full([6], '', dtype=np.str)
        for i in range(0,6):
            np.copyto(tempCent[i], np.hstack((centers[i][0],centers[i][1])))
        tempCentL = tempCent.tolist()
        dicts = [{'w': row.count('w'), 'r': row.count('r'), 'y': row.count('y'), 'o': row.count('o'), 'b': row.count('b'), 'g': row.count('g')} for row in tempCentL]
        sorted_dicts = [sorted(el.items(), key=op.itemgetter(1), reverse=True) for el in dicts]
        has_space = True
        while has_space:
            for i in range(0,6):
                if sorted_dicts[i][0][1] == 3 or sorted_dicts[i][0][1] == 4:
                    faceColors[i] = sorted_dicts[i][0][0]
            for i in range(0,6):
                if sorted_dicts[i][0][1] == 2 and sorted_dicts[i][1][1] == 1:
                    rand_pos = rand.randint(0,3)
                    if sorted_dicts[i][rand_pos%3][0] not in faceColors:
                        faceColors[i] = sorted_dicts[i][rand_pos%3][0]
                elif sorted_dicts[i][0][1] == 2 and sorted_dicts[i][1][1] == 2:
                    rand_pos = rand.randint(0,1)
                    if sorted_dicts[i][rand_pos][0] not in faceColors:
                        faceColors[i] = sorted_dicts[i][rand_pos][0]
                elif sorted_dicts[i][0][1] == 1 and sorted_dicts[i][1][1] == 1:
                    rand_pos = rand.randint(0,3)
                    if sorted_dicts[i][rand_pos][0] not in faceColors:
                        faceColors[i] = sorted_dicts[i][rand_pos][0]
            has_space = '' in faceColors
        faceTotals = [sum([self.faces[x][y].tolist().count(faceColors[x]) for y in range(0,4)]) for x in range(0,6)]
        return sum(faceTotals)
        # return zip(faceColors,faceTotals)
