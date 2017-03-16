/* 3x3 Sobel mask for X Dimension. */
maskX[0][0] = -1;
maskX[0][1] = 0;
maskX[0][2] = 1;
maskX[1][0] = -2;
maskX[1][1] = 0;
maskX[1][2] = 2;
maskX[2][0] = -1;
maskX[2][1] = 0;
maskX[2][2] = 1;
/* 3x3 Sobel mask for Y Dimension. */
maskY[0][0] = 1;
maskY[0][1] = 2;
maskY[0][2] = 1;
maskY[1][0] = 0;
maskY[1][1] = 0;
maskY[1][2] = 0;
maskY[2][0] = -1;
maskY[2][1] = -2;
maskY[2][2] = -1;
for (int x = 0; x < height; ++x) {
    for (int y = 0; y < width; ++y) {
        sumx = 0;
        sumy = 0;
        /* For handling image boundaries */
        if (x == 0 || x == (height - 1) || y == 0 || y == (width - 1))
            sum = 0;
        else {
            /* Gradient calculation in X Dimension */
            for (int i = -1; i <= 1; i++) {
                for (int j = -1; j <= 1; j++) {
                    sumx += (inputImage[x + i][y + j] * maskX[i + 1][j + 1]);
                }
            }
            /* Gradient calculation in Y Dimension */
            for (i = -1; i <= 1; i++) {
                for (j = -1; j <= 1; j++) {
                    sumy += (inputImage[x + i][y + j] * maskY[i + 1][j + 1]);
                }
            }
            /* Gradient magnitude */
            sum = (abs(sumx) + abs(sumy));

			std::cout << "Sum: " << sum << std::endl;

			if (sum < 0) {
				sum = 0;
			}
			else if (sum > 255) {
				sum = 255
			}
			
        }
        outputImage[x][y] = sum;
    }
}
