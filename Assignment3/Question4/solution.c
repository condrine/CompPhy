#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Define Random number generator
float rng() {
    return (float)rand()/(float)RAND_MAX;
}

// Gaussian (Box-Muller)
float* Gaussian(float sigma, float mu, int N) {

    // initialise sample array
    float *smpl;
    smpl = calloc(N, sizeof(float));

    // fill sampke
    for (int i=0; i < N/2 + 1; i++) {

        // Get random numbers
        float r1 = rng();
        float r2 = rng();

        // Get gaussian samples
        float u1 = sqrt(-2*log(r1))*cos(2*M_PI*r2);
        float u2 = sqrt(-2*log(r2))*sin(2*M_PI*r1);
        if (2*i < N) *(smpl + 2*i) = u1;
        if (2*i + 1 < N)*(smpl + 2*i + 1) = u2;
    }

    return smpl;
}

int main() {

    // Get Samples  
    int N = 1000;  
    float* Samples = Gaussian(0., 1., N);

    // Write to file
    FILE *fptr;
    fptr = fopen("Results/gauss.dat","w");
    for (int i = 0; i < N; i++ )
   	  fprintf(fptr, "%f\n", *(Samples+i) );
}

