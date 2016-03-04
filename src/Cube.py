import numpy as np

class Cube:

    def __init__(self):
        self.faces = np.array([[['w','x','x','w'],
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

    def printCube(self):
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in self.faces[4]]))
        [print('\n'.join([''.join(['{:3}'.format(self.faces[x][y][z]) for x in range(0,4) for z in range(0,4)])])) for y in range(0,4)]
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in self.faces[5]]))

    def quarterTurn():
        print("turn")

    def rotateFace(self,face, direction):
        if direction:
            self.faces[face] = np.rot90(self.faces[face],3)
        else:
            self.faces[face] = np.rot90(self.faces[face])
        print("rot")

    def fitness():
        print("fit")
