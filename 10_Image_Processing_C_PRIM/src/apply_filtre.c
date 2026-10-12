#include "apply_filtre.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "picture.h"
#include "pixels.h"
#include "filename.h"
#include <time.h>
#include "lut.h"

void apply_filter(picture (*filter)(picture), picture input, char *dir, char *name, char *specifier, char *ext)
{
    // Appliquer le filtre
    picture result = filter(input);

    // Construire le chemin de sortie
    char *path = concat_parts(dir, name, specifier, ext);

    // Sauvegarder l'image
    write_picture(result, path);

    // Libérer les ressources
    free(path);
}

picture extract_red_channel(picture p)
{
    return split_picture(p)[RED];
}

picture extract_green_channel(picture p)
{
    return split_picture(p)[GREEN];
}

picture extract_blue_channel(picture p)
{
    return split_picture(p)[BLUE];
}

picture wrapper_brighten(picture p)
{
    return brighten_picture(p, 1.5);
}

picture wrapper_melt(picture p)
{
    return melt_picture(p, p.height * p.width * p.channels * 5);
}

picture wrapper_set_levels(picture p)
{
    return set_levels_picture(p, 8);
}

picture wrapper_smaller_nearest(picture p)
{
    return nearest_scale(p, 0.74);
}

picture wrapper_bigger_nearest(picture p)
{
    return nearest_scale(p, 1.36);
}

picture wrapper_smaller_bilineaire(picture p)
{
    return bilineaire_scale(p, 0.74);
}

picture wrapper_bigger_bilineaire(picture p)
{
    return bilineaire_scale(p, 1.36);
}

picture wrapper_diff_g(picture gray)
{
    picture scale_nearest_g = nearest_scale(gray, 1.36);
    picture scale_bilineare_g = bilineaire_scale(gray, 1.36);
    picture diff_g = sub_picture(scale_bilineare_g, scale_nearest_g);
    return normalize_dynamic_picture(diff_g);
}

picture wrapper_diff_c(picture color)
{
    picture scale_nearest_c = nearest_scale(color, 1.36);
    picture scale_bilineare_c = bilineaire_scale(color, 1.36);
    picture diff_c = sub_picture(scale_bilineare_c, scale_nearest_c);
    return normalize_dynamic_picture(diff_c);
}

picture wrapper_mult(picture p)
{
    return mult_picture(p, read_picture("Lenna_BW.ppm"));
}

picture wrapper_mix(picture p)
{
    return mix_picture(read_picture("inv.ppm"), p, read_picture("Lenna_BW.ppm"));
}