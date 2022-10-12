from fuctions import *
import numpy as np


def main():
    print("Ingrese los valores de las ecuaciones")
    print("Ecuacion 1")
    Ecuation1 = getEcuationsValues(1)
    print("Ecuacion 2")
    Ecuation2 = getEcuationsValues(2)
    print("Ecuacion 3")
    Ecuation3 = getEcuationsValues(3)

    Matrices = getMatrices(Ecuation1, Ecuation2, Ecuation3)

    Principal_Matriz = Matrices[0]
    Matriz_Intensiad_1 = Matrices[1]
    Matriz_Intensiad_2 = Matrices[2]
    Matriz_Intensiad_3 = Matrices[3]

    Determinant_Principal_Matriz = np.linalg.det(Principal_Matriz)
    Determinant_Matriz_Intensiad_1 = np.linalg.det(Matriz_Intensiad_1)
    Determinant_Matriz_Intensiad_2 = np.linalg.det(Matriz_Intensiad_2)
    Determinant_Matriz_Intensiad_3 = np.linalg.det(Matriz_Intensiad_3)

    Intensity_1 = Determinant_Matriz_Intensiad_1 / Determinant_Principal_Matriz
    Intensity_2 = Determinant_Matriz_Intensiad_2 / Determinant_Principal_Matriz
    Intensity_3 = Determinant_Matriz_Intensiad_3 / Determinant_Principal_Matriz
    print("La intensidad 1 compleja es: ", Intensity_1)
    print("La intensidad 2 compleja es: ", Intensity_2)
    print("La intensidad 3 compleja es: ", Intensity_3)
    Intenssity_polar_1 = (convertToPolar(Intensity_1))
    Intenssity_polar_2 = (convertToPolar(Intensity_2))
    Intenssity_polar_3 = (convertToPolar(Intensity_3))
    print("La intensidad 1 polar es: ", Intenssity_polar_1[0], "el angulo es: ", Intenssity_polar_1[1])
    print("La intensidad 2 polar es: ", Intenssity_polar_2[0], "el angulo es: ", Intenssity_polar_2[1])
    print("La intensidad 3 polar es: ", Intenssity_polar_3[0], "el angulo es: ", Intenssity_polar_3[1])


if __name__ == "__main__":
    main()
