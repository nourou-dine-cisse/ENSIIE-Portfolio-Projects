#ifndef _PIXELS_H_
#define _PIXELS_H_

typedef enum
{
    RED = 0,
    GREEN = 1,
    BLUE = 2
} color;

/*@requires *p and *r valid pictures
  @assigns *r
  @ensures puts the data of *p into *r
*/
void write_pixels(picture *p, picture *r);

#endif