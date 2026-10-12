#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Fonction distrib : tire 2 cartes distinctes
int* distrib(int deck[], int size) {
    int *res = malloc(2 * sizeof(int));
    if (!res) { perror("malloc"); exit(1); }
    int a = rand() % size;
    int b;
    do { b = rand() % size; } while (b == a);
    res[0] = deck[a];
    res[1] = deck[b];
    return res;
}

// Génère la main de J2 sachant que J1 a reçu (i1,j1)
int* main_J2(int i1, int j1) {
    int counts[4] = {0,2,2,2};
    counts[i1]--; counts[j1]--;
    int deck[4], idx = 0;
    for (int v = 1; v <= 3; v++) {
        for (int k = 0; k < counts[v]; k++) {
            deck[idx++] = v;
        }
    }
    int *c = distrib(deck, 4);
    int *out = malloc(2 * sizeof(int));
    if (!out) { perror("malloc"); exit(1); }
    if (c[0] < c[1]) {
        out[0] = c[0]; out[1] = c[1];
    } else {
        out[0] = c[1]; out[1] = c[0];
    }
    free(c);
    return out;
}

int* manche_1(int i1, int j1, int p1, int q1) {
    int *j2_hand = main_J2(i1, j1); // main de J2
    int i2 = j2_hand[0];
    int j2 = j2_hand[1];

    int c1 = p1 ? j1 : i1;
    int c2 = q1 ? j2 : i2; 

    int* g = malloc(2 * sizeof(int));
    if (!g) { perror("malloc"); exit(1); }

    g[0] = 0;
    g[1] = 0; 

    if ((p1 && c1 > c2) || (!p1 && c1 < c2)) g[0] = 1;
    if ((q1 && c2 > c1) || (!q1 && c2 < c1)) g[1] = 1;

    free(j2_hand);
    return g;
}

int* manche_1_mixte(int i1, int j1, float p1, float q1) {
    // Tirage aléatoire des paris en stratégie mixte
    int pari1 = ((float)rand() / RAND_MAX < p1) ? 1 : 0; // J1 parie V avec proba p1
    int pari2 = ((float)rand() / RAND_MAX < q1) ? 1 : 0; // J2 parie V avec proba q1

    // Utilise la fonction déjà définie
    return manche_1(i1, j1, pari1, pari2); // retourne un int[2]
}

float** P_approx_G1_mixte(int i1, int j1, float p1, float q1, int n) {
    // Allocation du tableau de compteurs [2][2]
    int** counts = malloc(2 * sizeof(int*));
    for (int i = 0; i < 2; i++) {
        counts[i] = calloc(2, sizeof(int));
    }

    for (int t = 0; t < n; t++) {
        int* scores = manche_1_mixte(i1, j1, p1, q1);
        int g1 = scores[0];
        int g2 = scores[1];
        counts[g1][g2]++;
        free(scores);
    }

    // Création du tableau de proportions [2][2]
    float** proportions = malloc(2 * sizeof(float*));
    for (int i = 0; i < 2; i++) {
        proportions[i] = malloc(2 * sizeof(float));
        for (int j = 0; j < 2; j++) {
            proportions[i][j] = (float)counts[i][j] / n;
        }
        free(counts[i]);
    }
    free(counts);

    return proportions;
}

float E_approx_G1_J1_mixte(int i1, int j1, float p1, float q1, int n) {
    float **props = P_approx_G1_mixte(i1, j1, p1, q1, n);
    float e = 0.0;
    for (int g1 = 0; g1 <= 1; g1++) {
        for (int g2 = 0; g2 <= 1; g2++) {
            e += g1 * props[g1][g2];
        }
        free(props[g1]);
    }
    free(props);
    return e;
}

float E_approx_G1_J2_mixte(int i1, int j1, float p1, float q1, int n) {
    float **props = P_approx_G1_mixte(i1, j1, p1, q1, n);
    float e = 0.0;
    for (int g1 = 0; g1 <= 1; g1++) {
        for (int g2 = 0; g2 <= 1; g2++) {
            e += g2 * props[g1][g2];
        }
        free(props[g1]);
    }
    free(props);
    return e;
}

int main() {
    srand(time(NULL));
    int i1 = 1, j1 = 2;
    float p1 = 0.7; // J1 parie Victoire avec proba 0.7
    float q1 = 0.3; // J2 parie Victoire avec proba 0.3
    int n = 100000;

    float EJ1 = E_approx_G1_J1_mixte(i1, j1, p1, q1, n);
    float EJ2 = E_approx_G1_J2_mixte(i1, j1, p1, q1, n);

    printf("Espérance (stratégie mixte) J1 : %.4f\n", EJ1);
    printf("Espérance (stratégie mixte) J2 : %.4f\n", EJ2);

    return 0;
}


