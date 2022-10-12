from math import sqrt, atan

import numpy as np


def getMatrices(Ecuation1, Ecuation2, Ecuation3):
    Principal_Matriz = np.array([[Ecuation1["Intensity_1_1"], Ecuation1["Intensity_2_1"], Ecuation1["Intensity_3_1"]],
                                 [Ecuation2["Intensity_1_2"], Ecuation2["Intensity_2_2"], Ecuation2["Intensity_3_2"]],
                                 [Ecuation3["Intensity_1_3"], Ecuation3["Intensity_2_3"], Ecuation3["Intensity_3_3"]]])
    Matriz_Intensiad_1 = np.array([[Ecuation1["Voltaje_1"], Ecuation1["Intensity_2_1"], Ecuation1["Intensity_3_1"]],
                                   [Ecuation2["Voltaje_2"], Ecuation2["Intensity_2_2"], Ecuation2["Intensity_3_2"]],
                                   [Ecuation3["Voltaje_3"], Ecuation3["Intensity_2_3"], Ecuation3["Intensity_3_3"]]])
    Matriz_Intensiad_2 = np.array([[Ecuation1["Intensity_1_1"], Ecuation1["Voltaje_1"], Ecuation1["Intensity_3_1"]],
                                   [Ecuation2["Intensity_1_2"], Ecuation2["Voltaje_2"], Ecuation2["Intensity_3_2"]],
                                   [Ecuation3["Intensity_1_3"], Ecuation3["Voltaje_3"], Ecuation3["Intensity_3_3"]]])
    Matriz_Intensiad_3 = np.array([[Ecuation1["Intensity_1_1"], Ecuation1["Intensity_2_1"], Ecuation1["Voltaje_1"]],
                                   [Ecuation2["Intensity_1_2"], Ecuation2["Intensity_2_2"], Ecuation2["Voltaje_2"]],
                                   [Ecuation3["Intensity_1_3"], Ecuation3["Intensity_2_3"], Ecuation3["Voltaje_3"]]])
    return Principal_Matriz, Matriz_Intensiad_1, Matriz_Intensiad_2, Matriz_Intensiad_3


def convertToPolar(complexNumber):
    realPart = complexNumber.real
    imaginaryPart = complexNumber.imag
    module = sqrt(realPart ** 2 + imaginaryPart ** 2)
    angle = (atan((imaginaryPart / realPart)) * 57.2958)
    return module, angle


def getEcuationsValues(ecuation):
    if ecuation == 1:
        Intensity_1_1 = complex(input("Ingrese el componente de la intensidad 1 en la ecuacion 1: "))
        Intensity_2_1 = complex(input("Ingrese el componente de la intensidad 2 en la ecuacion 1: "))
        Intensity_3_1 = complex(input("Ingrese el componente de la intensidad 3 en la ecuacion 1: "))
        Voltaje_1 = complex(input("Ingrese el voltaje en la ecuacion 1: "))
        Ecuation1 = {
            "Intensity_1_1": Intensity_1_1,
            "Intensity_2_1": Intensity_2_1,
            "Intensity_3_1": Intensity_3_1,
            "Voltaje_1": Voltaje_1
        }
        return Ecuation1
    if ecuation == 2:
        Intensity_1_2 = complex(input("Ingrese el componente de la intensidad 1 en la ecuacion 2: "))
        Intensity_2_2 = complex(input("Ingrese el componente de la intensidad 2 en la ecuacion 2: "))
        Intensity_3_2 = complex(input("Ingrese el componente de la intensidad 3 en la ecuacion 2: "))
        Voltaje_2 = complex(input("Ingrese el voltaje en la ecuacion 2: "))
        Ecuation2 = {
            "Intensity_1_2": Intensity_1_2,
            "Intensity_2_2": Intensity_2_2,
            "Intensity_3_2": Intensity_3_2,
            "Voltaje_2": Voltaje_2
        }
        return Ecuation2
    if ecuation == 3:
        Intensity_1_3 = complex(input("Ingrese el componente de la intensidad 1 en la ecuacion 3: "))
        Intensity_2_3 = complex(input("Ingrese el componente de la intensidad 2 en la ecuacion 3: "))
        Intensity_3_3 = complex(input("Ingrese el componente de la intensidad 3 en la ecuacion 3: "))
        Voltaje_3 = complex(input("Ingrese el voltaje en la ecuacion 3: "))
        Ecuation3 = {
            "Intensity_1_3": Intensity_1_3,
            "Intensity_2_3": Intensity_2_3,
            "Intensity_3_3": Intensity_3_3,
            "Voltaje_3": Voltaje_3
        }
        return Ecuation3
