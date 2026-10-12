#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "picture.h"
#include "pixels.h"

typedef byte pixels;
void write_pixels(picture *p, picture *r)
{
    // si les images ont le meme nombre de channels
    if (p->channels == r->channels)
    {
        for (int i = 0; i < p->width; i++)
        {
            for (int j = 0; j < p->height; j++)
            {
                for (int k = 0; k < p->channels; k++)
                {
                    r->data[(i * r->width + j) * r->channels + k] = p->data[(i * p->width + j) * p->channels + k];
                }
            }
        }
    }
    // si le resultat est une image couleur
    else if (r->channels == 3)
    {
        for (int i = 0; i < p->width; i++)
        {
            for (int j = 0; j < p->height; j++)
            {
                for (int k = 0; k < r->channels; k++)
                {
                    r->data[(i * r->width + j) * r->channels + k] = p->data[(i * p->width + j) * p->channels];
                }
            }
        }
    }
}
