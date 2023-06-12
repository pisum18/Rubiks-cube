#!"C:\Users\Iemand\Documents\PythonVenv\RubiksCube\Scripts\python.exe"

from re import L
import numpy as np
import cython

# https://cython.readthedocs.io/en/latest/src/userguide/language_basics.html


class Cube:

    def __init__(self, size):
        self.TopLayer = self.Layer(size, 'w')
        self.BottomLayer = self.Layer(size, 'y')
        self.LeftLayer = self.Layer(size, 'o')
        self.RightLayer = self.Layer(size, 'r')
        self.BackLayer = self.Layer(size, 'b')
        self.FrontLayer = self.Layer(size, 'g')

    def AffectUpper(self, mode):
        #case you want to turn upper layer clockwise
        MoveClockwise = False
        MoveCounterClockwise = False
        MoveTwice = False

        if (mode == 0): MoveClockwise = True
        elif (mode == 1): MoveCounterClockwise = True
        elif (mode == 2): MoveTwice = True

        if (MoveClockwise):
            NewLeftColumn = self.TopLayer.Layer[0][:].transpose()
            NewMiddleColumn = self.TopLayer.Layer[1][:].transpose()
            NewRightColumn = self.TopLayer.Layer[2][:].transpose()

            self.TopLayer.Layer[:][0] = NewLeftColumn
            self.TopLayer.Layer[:][1] = NewMiddleColumn
            self.TopLayer.Layer[:][2] = NewRightColumn


    def VisualizeCube(self):
        outputstring = ""
        outputstring += "Top Layer \r\n"
        outputstring += self.VisualizeLayer(self.TopLayer.Layer)
        outputstring += "Bottom Layer \r\n"
        outputstring += self.VisualizeLayer(self.BottomLayer.Layer)
        outputstring += "Left Layer \r\n"
        outputstring += self.VisualizeLayer(self.LeftLayer.Layer)
        outputstring += "Right Layer \r\n"
        outputstring += self.VisualizeLayer(self.RightLayer.Layer)
        outputstring += "Back Layer \r\n"
        outputstring += self.VisualizeLayer(self.BackLayer.Layer)
        outputstring += "Front Layer \r\n"
        outputstring += self.VisualizeLayer(self.FrontLayer.Layer)
        print(outputstring)

    def VisualizeLayer(self, Layer):
        outputstring = Layer[0][0].decode() + Layer[0][1].decode() + Layer[0][2].decode() + "\r\n"
        outputstring += Layer[1][0].decode() + Layer[1][1].decode() + Layer[1][2].decode() + "\r\n"
        outputstring += Layer[2][0].decode() + Layer[2][1].decode() + Layer[2][2].decode() + "\r\n"
        return outputstring

        # subclasses
    class Layer:
        def __init__(self, size, fill):
            self.Layer = np.chararray((size, size))
            self.Layer.fill(fill)

        def FillLayer(self):
            for i in range(size):
                for j in range(size):
                    self.Layer[i][j] = (i + 1) * (j + 1)

        #def Move(self, Layer):




if __name__ == "__main__":
    size = 3
    NewCube = Cube(size)

    NewCube.TopLayer.FillLayer()
    NewCube.AffectUpper(0)

    NewCube.VisualizeCube()

