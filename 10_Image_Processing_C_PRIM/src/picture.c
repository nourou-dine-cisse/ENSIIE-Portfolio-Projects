#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "picture.h"
#include "pixels.h"
#include "filename.h"
#include <time.h>
#include "lut.h"

picture read_picture(char *filename)
{
    // ouverture du fichier
    FILE *file = fopen(filename, "rb");
    if (!file)
    {
        perror("erreur d'ouverture du fichier");
        exit(1);
    }

    // declaration d'une image et buffer
    picture img = {0};
    char buffer[126];

    // lecture de l'entete
    if (fgets(buffer, 126, file) == NULL)
    {
        perror("erreur de lecture de l'entete");
        fclose(file);
        exit(2);
    }

    if (strcmp(buffer, "P5\n") != 0 && strcmp(buffer, "P6\n") != 0)
    {
        perror("not binary PPM/PGM file");
        fclose(file);
        exit(3);
    }

    // determination du nombre de canal
    img.channels = (strcmp(buffer, "P5\n") == 0) ? 1 : 3;

    // ignorer les lignes commencant par '#'
    do
    {
        if (fgets(buffer, 126, file) == NULL)
        {
            perror("erreur de lecture de l'entete");
            fclose(file);
            exit(4);
        }
    } while (buffer[0] == '#');

    // lecture des dimensions
    if (sscanf(buffer, "%d %d", &img.width, &img.height) < 0)
    {
        perror("Erreur de lecture des dimensions");
        fclose(file);
        exit(5);
    }
    // lire le byte max
    if (fgets(buffer, 126, file) == NULL)
    {
        perror("erreur de lecture du byte max");
        fclose(file);
        exit(6);
    }
    sscanf(buffer, "%s", &img.max);

    // lire les donnees
    img.data = malloc(img.height * img.width * img.channels * sizeof(byte));
    if (!img.data)
    {
        fclose(file);
        perror("Allocation mémoire échouée");
        exit(7);
    }
    fread(img.data, sizeof(byte), img.height * img.width * img.channels, file);

    // fermer
    fclose(file);

    return img;
}

int write_picture(picture p, char *filename)
{
    // ouverture du fichier
    FILE *file = fopen(filename, "wb");
    if (!file)
    {
        perror("erreur d'ouverture du fichier");
        return 1;
    }
    // recuperation de l'extention
    char *ext = ext_from_path(filename);

    // ecriture en cas de fichier pgm
    if (strcmp(ext, "pgm") == 0)
    {
        fprintf(file, "P5\n%d %d\n%d\n", p.width, p.height, MAX_BYTE);
        fwrite(p.data, sizeof(byte), p.height * p.width, file);
        fclose(file);
        return 0;
    }

    // ecriture en cas de fichier ppm
    fprintf(file, "P6\n%d %d\n%d\n", p.width, p.height, MAX_BYTE);
    fwrite(p.data, sizeof(byte), p.height * p.width * p.channels, file);
    fclose(file);
    return 0;
}

picture create_picture(unsigned int width, unsigned int height, unsigned int channels, byte max)
{
    // declaration de l'image et remplissage des donnees
    picture img;
    img.width = width;
    img.height = height;
    img.channels = channels;
    img.max = max;
    // allocation de memoire pour les donnees de img
    img.data = malloc(height * width * channels * sizeof(byte));
    if (!img.data)
    {
        perror("Allocation mémoire échouée");
        exit(1);
    }
    return img;
}

void clean_picture(picture *p)
{
    // liberation de la memoire
    free(p);
    // reitialisation des valeurs
    p->data = NULL;
    p->height = 0;
    p->width = 0;
}

picture copy_picture(picture p)
{
    // creation de l'image resultante
    picture r = create_picture(p.width, p.height, p.channels, p.max);
    // remplissage des donnees de r
    write_pixels(&p, &r);
    return r;
}

int is_empty_picture(picture p)
{
    // verification de la nulite des donnees
    if (p.data == NULL)
    {
        return 1;
    }
    return 0;
}

int is_gray_picture(picture p)
{
    // comparaison du channel
    return p.channels == 1;
}

int is_color_picture(picture p)
{
    // comparaison du channel
    return p.channels == 3;
}

void info_picture(picture p)
{
    // affichage des infos dans stdout
    printf("(%d x %d x %d)", p.width, p.height, p.channels);
}

picture convert_to_color_picture(picture p)
{
    // si image deja en couleur la copier
    if (p.channels == 3)
    {
        return copy_picture(p);
    }
    // mettre le channel a 3
    int r_channels = 3;
    // creation  de l'image resultante
    picture r = create_picture(p.width, p.height, r_channels, p.max);
    r.channels = r_channels;
    // remplissage des donnees
    write_pixels(&p, &r);
    return r;
}

picture convert_to_gray_picture(picture p)
{
    // si image deja en gray la copier
    if (p.channels == 1)
    {
        return copy_picture(p);
    }
    // creation et remplissage des donnees de l'image resultante
    int r_channels = 1;
    picture r = create_picture(p.width, p.height, r_channels, p.max);
    r.channels = r_channels;
    for (int i = 0; i < p.width; i++)
    {
        for (int j = 0; j < p.height; j++)
        {
            // application de la formule de conversion
            r.data[i * p.width + j] = 0.299 * p.data[(i * p.width + j) * p.channels] +
                                      0.587 * p.data[(i * p.width + j) * p.channels + 1] +
                                      0.114 * p.data[(i * p.width + j) * p.channels + 2];
        }
    }
    return r;
}

picture *split_picture(picture p)
{
    // allocation de memoire pour le tableau d'image resultante
    picture *r = malloc(3 * sizeof(picture));
    int r_channels = 1;
    for (int i = 0; i < 3; i++)
    {
        r[i] = create_picture(p.width, p.height, r_channels, p.max);
        r[i].channels = r_channels;
    }
    // remplissage des donnees
    for (int i = 0; i < p.width; i++)
    {
        for (int j = 0; j < p.height; j++)
        {
            r[RED].data[(i * p.width + j)] = p.data[(i * p.width + j) * p.channels];
            r[BLUE].data[(i * p.width + j)] = p.data[(i * p.width + j) * p.channels + 1];
            r[GREEN].data[(i * p.width + j)] = p.data[(i * p.width + j) * p.channels + 2];
        }
    }
    return r;
}

picture merge_picture(picture red, picture green, picture blue)
{
    // ccreation de l'image resultante
    int r_channels = 3;
    picture r = create_picture(red.width, red.height, r_channels, red.max);
    r.channels = r_channels;
    // remplissage des donnees
    for (int i = 0; i < red.width; i++)
    {
        for (int j = 0; j < red.height; j++)
        {
            for (int k = 0; k < r_channels; k++)
            {
                r.data[(i * r.width + j) * r_channels] = red.data[(i * red.width + j)];
                r.data[(i * r.width + j) * r_channels + 1] = green.data[(i * green.width + j)];
                r.data[(i * r.width + j) * r_channels + 2] = blue.data[(i * blue.width + j)];
            }
        }
    }
    return r;
}

picture brighten_picture(picture p, double factor)
{
    // ccreation de l'image resultante
    picture r = create_picture(p.width, p.height, p.channels, p.max);
    // remplissage des donnees
    for (int i = 0; i < p.width; i++)
    {
        for (int j = 0; j < p.height; j++)
        {
            for (int k = 0; k < r.channels; k++)
            {
                int v = p.data[(i * p.width + j) * r.channels + k] * factor;
                if (v > 255)
                {
                    v = 255;
                }
                r.data[(i * p.width + j) * r.channels + k] = v;
            }
        }
    }
    return r;
}

// retourne une valeur random entre 0 et max
int random_between(int min, int max)
{
    return rand() % (max - min + 1) + min;
}

picture melt_picture(picture p, int number)
{
    // Copie de l'image originale
    picture r = copy_picture(p);

    // Initialisation de la graine pour rand()
    srand((unsigned int)time(NULL));

    for (int i = 0; i < number; i++)
    {
        // Génération d'une coordonnée aléatoire
        int random_height = random_between(0, p.height - 1);
        int random_width = random_between(0, p.width - 1);

        for (int k = 0; k < p.channels; k++)
        {
            int curr_pixel = (random_height * p.width + random_width) * p.channels + k;

            // Vérification pour éviter un accès hors limites
            if (random_height > 0)
            {
                int above_pixel = ((random_height - 1) * p.width + random_width) * p.channels + k;
                if (r.data[curr_pixel] > r.data[above_pixel])
                {
                    r.data[curr_pixel] = r.data[above_pixel];
                }
            }
        }
    }

    return r;
}
