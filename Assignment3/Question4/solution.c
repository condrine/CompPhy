#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Define Random number generator
float rng() {
    return (float)rand()/(float)RAND_MAX;
}

// Exponential sampler (Transform)
float* Expo_Sampler(float lambda, int N) {

    // initialise sample array
    float *smpl;
    smpl = calloc(N, sizeof(float));

    // fill sample
    for (int i=0; i < N ; i++) {

        // Get exponential samples
        float r1 = rng();
        *(smpl + i) = (-1./lambda)*log(1-r1);
    }

    return smpl;
}

// Exact Exponential function
float Exponential(float lambda, float x) {
    return exp(-lambda*x)*lambda;
}

int main() {

    // Get Samples  
    int N = 10000;  
    float* Samples = Expo_Sampler(2., N);

    // Write samples to file
    FILE *fptr;
    fptr = fopen("Results/expo_sample.dat","w");
    for (int i = 0; i < N; i++ ) fprintf(fptr, "%f\n", *(Samples+i));
    fclose(fptr);

    // Free memory
    free(Samples);

    // Write exact func to file
    fptr = fopen("Results/expo_exact.dat","w");
    for (int i = 0; i < 30; i++ ) fprintf(fptr, "%f %f\n", i*4./30., Exponential(2., i*4./30.));
    fclose(fptr);
}


