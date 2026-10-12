#ifndef _FILTER_H_
#define _FILTER_H_
#include "picture.h"
#include "lut.h"
#include "pixels.h"
#include "filename.h"
#include <math.h>

/*@requires filename a valid path
   @assigns nothing
   @ensures returns the picture read from filename after applying the filter
*/
void apply_filter(picture (*filter)(picture), picture input, char *dir, char *name, char *specifier, char *ext);

/*@requires
    @assigns nothing
    @ensures returns the red channel of the picture
*/
picture extract_red_channel(picture p);

/*@requires
    @assigns nothing
    @ensures returns the green channel of the picture
*/
picture extract_green_channel(picture p);

/*@requires
    @assigns nothing
    @ensures returns the blue channel of the picture
*/
picture extract_blue_channel(picture p);

/*@requires
    @assigns nothing
    @ensures returns the output of the brighthen_picture function with a specific argument
*/
picture wrapper_brighten(picture p);

/*@requires
    @assigns nothing
    @ensures returns the output of the melted_picture function with a specific argument
*/
picture wrapper_melt(picture p);

/*@requires
    @assigns nothing
    @ensures returns the output of the set_levels_picture function with a specific argument
*/
picture wrapper_set_levels(picture p);

/*@requires
    @assigns nothing
    @ensures returns the output of the nearest_scale function with a specific argument
*/
picture wrapper_smaller_nearest(picture p);

/*@requires
    @assigns nothing
    @ensures returns the output of the nearest_scale function with a specific argument
*/
picture wrapper_bigger_nearest(picture p);

/*@requires
    @assigns nothing
    @ensures returns the output of the bilineaire_scale function with a specific argument
*/
picture wrapper_smaller_bilineaire(picture p);

/*@requires
    @assigns nothing
    @ensures returns the output of the bilineaire_scale function with a specific argument
*/
picture wrapper_bigger_bilineaire(picture p);

/*@requires
    @assigns nothing
    @ensures apply the filter to the picture with a specific argument
*/
picture wrapper_diff_g(picture gray);

/*@requires
    @assigns nothing
    @ensures apply the filter to the picture with a specific argument
*/
picture wrapper_diff_c(picture color);

/*@requires
    @assigns nothing
    @ensures apply the filter to the picture with a specific argument
*/
picture wrapper_mult(picture p);

/*@requires
    @assigns nothing
    @ensures apply the filter to the picture with a specific argument
*/
picture wrapper_mix(picture p);

#endif