#!"C:\Users\Iemand\Documents\PythonVenv\RubiksCube\Scripts\python.exe"

import numpy as np
import cython

# https://cython.readthedocs.io/en/latest/src/userguide/language_basics.html


class Cube:

    # subclasses
    class Layer:
        def __init__(self, size, fill):
            Layer = np.chararray((size, size))
            Layer.fill(fill)

    def __init__(self):
        self.TopLayer = self.Layer(3, 'w')
        self.BottomLayer = self.Layer(3, 'y')
        self.LeftLayer = self.Layer(3, 'o')
        self.RightLayer = self.Layer(3, 'r')
        self.BackLayer = self.Layer(3, 'b')
        self.FrontLayer = self.Layer(3, 'g')

    def VisualizeCube():

        #implement this code
        # make it print out the cube layer by layer

        # don't like this code, would be best if input was a generic layer type
        # maybe make other object for layers
    def VisualizeLayer(Layer):
        print(Layer[0][0].decode() + Layer[0][1].decode() + Layer[0][2].decode())
        print(Layer[1][0].decode() + Layer[1][1].decode() + Layer[1][2].decode())
        print(Layer[2][0].decode() + Layer[2][1].decode() + Layer[2][2].decode())



if __name__ == "__main__":

    NewCube = Cube()

    NewCube.VisualizeCube()

