#ifndef _LUT_H_
#define _LUT_H_
#include "picture.h"

struct lut
{
   int n;
   byte *data;
};
typedef struct lut lut;

/* @requires nothing
   @assigns nothing
   @ensures returns a new allocated lut with n levels
*/
lut create_lut(byte n);

/* @requires nothing
   @assigns nothing
   @ensures free the lut
*/
void clean_lut(lut *l);

/* @requires p a picture and l a lut
   @assigns nothing
   @ensures applies the lut to the picture
*/
void apply_lut(picture *p, lut *l);

/* @requires p a picture
   @assigns nothing
   @ensures returns p by inversing its colors
*/
picture inverse_picture(picture p);

/* @requires p a picture
   @assigns nothing
   @ensures returns p by normalising its pixels
*/
picture normalize_dynamic_picture(picture p);

/* @requires p a picture and nb_levels a valid byte
   @assigns nothing
   @ensures returns p by changing the level of the pixels
*/
picture set_levels_picture(picture p, byte nb_levels);

/* @requires p1 and p2 pictures
   @assigns nothing
   @ensures returns an image by substracting the corresponding pixels of p1 and p2
*/
picture sub_picture(picture p1, picture p2);

/* @requires p1 and p2 pictures
   @assigns nothing
   @ensures returns an image by multiplying the corresponding pixels of p1 and p2
*/
picture mult_picture(picture p1, picture p2);

/* @requires p1, p2 and p3 pictures
   @assigns nothing
   @ensures returns an image by merging the 3 input images
*/
picture mix_picture(picture p1, picture p2, picture p3);

/* @requires p a valid picture and factor > 0
   @assigns nothing
   @ensures returns p scaled by nearest neighbour
*/
picture nearest_scale(picture p, double factor);

/* @requires p a valid picture alpha and beta in [0, 1]
   @assigns nothing
   @ensures returns p scaled by alpha and beta
*/
picture bilineaire_scale(picture p, double factor);

#endif
