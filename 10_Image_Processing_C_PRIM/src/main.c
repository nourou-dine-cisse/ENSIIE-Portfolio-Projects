#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "picture.h"
#include "pixels.h"
#include "filename.h"
#include <time.h>
#include "lut.h"
#include "apply_filtre.h"

int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        printf("Usage: %s <gray_picture> <color_picture>\n", argv[0]);
        return 1;
    }

    // lecture des images
    picture gray = read_picture(argv[1]);
    picture color = read_picture(argv[2]);

    // variables pour noms de fichiers
    char *dir = dir_from_path(argv[1]);

    char *gray_name = name_from_path(argv[1]);
    char *color_name = name_from_path(argv[2]);

    char *gray_ext = ext_from_path(argv[1]);
    char *color_ext = ext_from_path(argv[2]);

    // conversion en couleur
    apply_filter(convert_to_color_picture, gray, dir, gray_name, "convert_color", color_ext);
    // conversion en gris
    apply_filter(convert_to_gray_picture, color, dir, color_name, "convert_gray", gray_ext);
    // split red
    apply_filter(extract_red_channel, color, dir, color_name, "red", gray_ext);
    // split green
    apply_filter(extract_green_channel, color, dir, color_name, "green", gray_ext);
    // split blue
    apply_filter(extract_blue_channel, color, dir, color_name, "blue", gray_ext);
    // eclaircir l'image en gris
    apply_filter(wrapper_brighten, gray, dir, gray_name, "brighten", gray_ext);
    // eclaircir l'image en couleur
    apply_filter(wrapper_brighten, color, dir, color_name, "brighten", color_ext);
    // fondre l'image en gris
    apply_filter(wrapper_melt, gray, dir, gray_name, "melted", gray_ext);
    // fondre l'image en couleur
    apply_filter(wrapper_melt, color, dir, color_name, "melted", color_ext);
    // inverser l'image en gris
    apply_filter(inverse_picture, gray, dir, gray_name, "inverse", gray_ext);
    // inverser l'image en couleur
    apply_filter(inverse_picture, color, dir, color_name, "inverse", color_ext);
    // normaliser l'image en gris
    apply_filter(normalize_dynamic_picture, gray, dir, gray_name, "dynamic", gray_ext);
    // normaliser l'image en couleur
    apply_filter(normalize_dynamic_picture, color, dir, color_name, "dynamic", color_ext);
    // changer le nombre de niveaux de l'image en gris
    apply_filter(wrapper_set_levels, gray, dir, gray_name, "levels", gray_ext);
    // changer le nombre de niveaux de l'image en couleur
    apply_filter(wrapper_set_levels, color, dir, color_name, "levels", color_ext);
    // redimensionner l'image en gris
    apply_filter(wrapper_smaller_nearest, gray, dir, gray_name, "smaller_nearest", gray_ext);
    // redimensionner l'image en couleur
    apply_filter(wrapper_smaller_nearest, color, dir, color_name, "smaller_nearest", color_ext);
    // redimensionner l'image en gris
    apply_filter(wrapper_bigger_nearest, gray, dir, gray_name, "bigger_nearest", gray_ext);
    // redimensionner l'image en couleur
    apply_filter(wrapper_bigger_nearest, color, dir, color_name, "bigger_nearest", color_ext);
    // redimensionner l'image en gris
    apply_filter(wrapper_smaller_bilineaire, gray, dir, gray_name, "smaller_bilineaire", gray_ext);
    // redimensionner l'image en couleur
    apply_filter(wrapper_smaller_bilineaire, color, dir, color_name, "smaller_bilineaire", color_ext);
    // redimensionner l'image en gris
    apply_filter(wrapper_bigger_bilineaire, gray, dir, gray_name, "bigger_bilineaire", gray_ext);
    // redimensionner l'image en couleur
    apply_filter(wrapper_bigger_bilineaire, color, dir, color_name, "bigger_bilineaire", color_ext);
    // difference d'images en gris
    apply_filter(wrapper_diff_g, gray, dir, gray_name, "difference", gray_ext);
    // difference d'images en couleur
    apply_filter(wrapper_diff_c, color, dir, color_name, "difference", color_ext);
    // produit d'images
    apply_filter(wrapper_mult, color, dir, color_name, "product", color_ext);
    // mixture d'images
    apply_filter(wrapper_mix, color, dir, color_name, "mixture", color_ext);

    // Libérer les ressources
    free(dir);
    free(gray_name);
    free(color_name);
    free(gray_ext);
    free(color_ext);
    return 0;
}
