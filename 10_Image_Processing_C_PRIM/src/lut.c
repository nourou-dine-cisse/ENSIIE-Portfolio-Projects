#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "picture.h"
#include "pixels.h"
#include "lut.h"
#include <math.h>

lut create_lut(byte n)
{
    // creation et remplissage du lut
    lut l;
    l.n = n;
    l.data = malloc(256 * sizeof(byte));
    for (int i = 0; i < 256; i++)
    {
        l.data[i] = i * n / 256;
    }
    return l;
}

void clean_lut(lut *l)
{
    // liberation des ressources
    free(l->data);
    l->n = 0;
}

void apply_lut(picture *p, lut *l)
{
    // remplissage des donnees de l'image resultante
    for (int i = 0; i < p->width; i++)
    {
        for (int j = 0; j < p->height; j++)
        {
            for (int k = 0; k < p->channels; k++)
            {
                p->data[(i * p->width + j) * p->channels + k] = l->data[p->data[(i * p->width + j) * p->channels + k]];
            }
        }
    }
}

picture inverse_picture(picture p)
{
    // creation et remplissage des donnees de l'image resultante
    picture r = create_picture(p.width, p.height, p.channels, p.max);
    // creation et remplissage du lut
    lut lut = create_lut(1);
    for (int i = 0; i < 256; i++)
    {
        lut.data[i] = 255 - i;
    }

    for (int i = 0; i < p.width; i++)
    {
        for (int j = 0; j < p.height; j++)
        {
            for (int k = 0; k < p.channels; k++)
            {
                // recuperation de la valeur du pixel
                int v = p.data[(i * p.width + j) * p.channels + k];
                // application du lut
                r.data[(i * p.width + j) * p.channels + k] = lut.data[v];
            }
        }
    }
    return r;
}

picture normalize_dynamic_picture(picture p)
{
    int max = 0;
    int min = 255;
    // recherche du min et du max
    for (int i = 0; i < p.width; i++)
    {
        for (int j = 0; j < p.height; j++)
        {
            for (int k = 0; k < p.channels; k++)
            {
                int v = p.data[(i * p.width + j) * p.channels + k];
                if (v > max)
                {
                    max = v;
                }
                if (v < min)
                {
                    min = v;
                }
            }
        }
    }
    // creation et remplissage des donnees de l'image resultante
    picture r = create_picture(p.width, p.height, p.channels, p.max);
    // creation et remplissage du lut
    lut lut = create_lut(255 / (max - min));
    for (int i = 0; i < 256; i++)
    {
        lut.data[i] = (i - min) * 255 / (max - min);
    }
    for (int i = 0; i < p.width; i++)
    {
        for (int j = 0; j < p.height; j++)
        {
            for (int k = 0; k < p.channels; k++)
            {
                // recuperation de la valeur du pixel
                int v = p.data[(i * p.width + j) * p.channels + k];
                // application du lut
                r.data[(i * p.width + j) * r.channels + k] = lut.data[v];
            }
        }
    }
    return r;
}

picture set_levels_picture(picture p, byte nb_levels)
{
    // creation et remplissage du lut
    lut lut = create_lut(nb_levels);
    for (int i = 0; i < nb_levels; i++)
    {
        lut.data[i] = i + 1;
    }
    // creation et remplissage des donnees de l'image resultante
    picture r = create_picture(p.width, p.height, p.channels, p.max);
    // application du lut
    for (int i = 0; i < p.width; i++)
    {
        for (int j = 0; j < p.height; j++)
        {
            for (int k = 0; k < p.channels; k++)
            {
                // recuperation de la valeur du pixel
                int v = p.data[(i * p.width + j) * p.channels + k];
                // discretisation de la valeur
                int v_discret = v * (nb_levels - 1) / 255;
                // valeur transformer
                int v_transformed = lut.data[v_discret];
                // valeur finale et application du lut
                r.data[(i * p.width + j) * p.channels + k] = v_transformed * 255 / nb_levels;
            }
        }
    }
    return r;
}

picture sub_picture(picture p1, picture p2)
{
    // creation et remplissage des donnees de l'image resultante
    picture r = create_picture(p1.width, p1.height, p1.channels, p1.max);
    for (int i = 0; i < p1.width; i++)
    {
        for (int j = 0; j < p1.height; j++)
        {
            for (int k = 0; k < p1.channels; k++)
            {
                // recuperation des valeurs des pixels
                int v1 = p1.data[(i * p1.width + j) * p1.channels + k];
                int v2 = p2.data[(i * p2.width + j) * p2.channels + k];
                // soustraction des valeurs
                int v = abs(v1 - v2);
                // application de la valeur
                r.data[(i * p1.width + j) * p1.channels + k] = v;
            }
        }
    }
    return r;
}

picture mult_picture(picture p1, picture p2)
{
    // creation et remplissage des donnees de l'image resultante
    picture r = create_picture(p1.width, p1.height, p1.channels, p1.max);
    for (int i = 0; i < p1.width; i++)
    {
        for (int j = 0; j < p1.height; j++)
        {
            for (int k = 0; k < p1.channels; k++)
            {
                // recuperation des valeurs des pixels
                int v1 = p1.data[(i * p1.width + j) * p1.channels + k];
                int v2 = p2.data[(i * p2.width + j) * p2.channels + k];
                // multiplication des valeurs
                int v = v1 * v2 / 255;
                // application de la valeur
                r.data[(i * p1.width + j) * p1.channels + k] = v;
            }
        }
    }
    return r;
}

picture mix_picture(picture p1, picture p2, picture p3)
{
    // creation et remplissage des donnees de l'image resultante
    picture r = create_picture(p1.width, p1.height, p1.channels, p1.max);
    for (int i = 0; i < p1.width; i++)
    {
        for (int j = 0; j < p1.height; j++)
        {
            for (int k = 0; k < p1.channels; k++)
            {
                // recuperation des valeurs des pixels
                int v1 = p1.data[(i * p1.width + j) * p1.channels + k];
                int v2 = p2.data[(i * p2.width + j) * p2.channels + k];
                int v3 = p3.data[(i * p3.width + j) * p3.channels + k];
                int alpha = v3 / 255;
                r.data[(i * p1.width + j) * p1.channels + k] = (1 - alpha) * v1 + alpha * v2;
            }
        }
    }
    return r;
}

picture nearest_scale(picture p, double factor)
{
    // Création et remplissage des données de l'image résultante
    picture r = create_picture((int)(p.width * factor), (int)(p.height * factor), p.channels, p.max);

    // Parcours de l'image redimensionnée
    for (int i = 0; i < r.width; i++)
    {
        for (int j = 0; j < r.height; j++)
        {
            for (int k = 0; k < p.channels; k++)
            {
                // Calcul des coordonnées dans l'image d'origine
                int x_src = i / factor;
                int y_src = j / factor;

                // pour ne pas dépasser les dimensions de l'image
                if (x_src >= p.width)
                    x_src = p.width - 1;
                if (y_src >= p.height)
                    y_src = p.height - 1;
                // Application du redimensionnement
                r.data[(i * r.width + j) * r.channels + k] = p.data[(x_src * p.width + y_src) * p.channels + k];
            }
        }
    }
    return r;
}

picture bilineaire_scale(picture p, double factor)
{
    // Création et remplissage des données de l'image résultante
    picture r = create_picture((int)(p.width * factor), (int)(p.height * factor), p.channels, p.max);

    // Parcours de l'image redimensionnée (inversion de i et j)
    for (int i = 0; i < r.height; i++)
    {
        for (int j = 0; j < r.width; j++)
        {
            for (int k = 0; k < p.channels; k++)
            {
                // Calcul des coordonnées dans l'image d'origine
                double x_src = j / factor;
                double y_src = i / factor;

                // Coordonnées des pixels entourant le pixel source
                int x1 = (int)x_src;
                int y1 = (int)y_src;
                int x2 = (x1 + 1 < p.width) ? x1 + 1 : x1;
                int y2 = (y1 + 1 < p.height) ? y1 + 1 : y1;

                // Récupération des valeurs entourant le pixel
                int p1 = p.data[(y1 * p.width + x1) * p.channels + k];
                int p2 = p.data[(y2 * p.width + x1) * p.channels + k];
                int p3 = p.data[(y1 * p.width + x2) * p.channels + k];
                int p4 = p.data[(y2 * p.width + x2) * p.channels + k];

                // Coefficients alpha et beta
                double alpha = x_src - x1;
                double beta = y_src - y1;

                // Application du redimensionnement
                r.data[(i * r.width + j) * p.channels + k] = (1 - alpha) * (1 - beta) * p1 + alpha * (1 - beta) * p3 + (1 - alpha) * beta * p2 + alpha * beta * p4;
            }
        }
    }

    return r;
}
