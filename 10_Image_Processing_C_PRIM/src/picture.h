#ifndef _PICTURE_H_
#define _PICTURE_H_

#define MAX_BYTE 255
typedef unsigned char byte;
struct picture
{
   int height;
   int width;
   int channels;
   byte max;
   byte *data;
};
typedef struct picture picture;
/* @requires filename a valid file
   @assigns nothing
   @ensures reads the filename data into a picture and returns the picture
*/
picture read_picture(char *filename);
/* @requires filename a valid file
   @assigns nothing
   @ensures write the picture data into filename
*/
int write_picture(picture p, char *filename);

/* @requires height and width positive integers channels = 1 or 3 ans max between 0 and 255
   @assigns nothing
   @ensures returns an initialised image with the input data
*/
picture create_picture(unsigned int width, unsigned int height, unsigned int channels, byte max);

/* @requires *p a valid adress
   @assigns *p
   @ensures free *p and reinitialize height, width to 0 and data to NULL
*/
void clean_picture(picture *p);

/* @requires p a picture
   @assigns nothing
   @ensures returns a copy of p
*/
picture copy_picture(picture p);

/* @requires p a picture
   @assigns nothing
   @ensures returns 0 if p is  NULL and 1 otherwise
*/
int is_empty_picture(picture p);

/* @requires p a picture
   @assigns nothing
   @ensures returns 0 if p is not a gray picture with one channel and 1 otherwise
*/
int is_gray_picture(picture p);

/* @requires p a picture
   @assigns nothing
   @ensures returns 0 if p is not a colored picture with 3 channels and 1 otherwise
*/
int is_color_picture(picture p);

/* @requires p a picture
   @assigns nothing
   @ensures returns the width, height and channels of p
*/
void info_picture(picture p);

/* @requires p a picture
   @assigns nothing
   @ensures returns p trasformed into a colored picture
*/
picture convert_to_color_picture(picture p);

/* @requires p a colored picture
   @assigns nothing
   @ensures returns p trasformed into a gray picture
*/
picture convert_to_gray_picture(picture p);

/* @requires p a colored picture
   @assigns nothing
   @ensures returns 3 images for every color
*/
picture *split_picture(picture p);

/* @requires p a colored picture
   @assigns nothing
   @ensures returns an image by merging red, gree and blue
*/
picture merge_picture(picture red, picture green, picture blue);

/* @requires p a colored picture
   @assigns nothing
   @ensures returns p brighthened
*/
picture brighten_picture(picture p, double factor);

/* @requires p a colored picture
   @assigns nothing
   @ensures returns p with a melted effect
*/
picture melt_picture(picture p, int number);

/*@ requires max <= RAND_MAX
  assigns nothing
  ensures returns a pseudo-random value between 0 and max included
  if rand() is assumed to be uniform, so is this function */
int rand_up_to(int max);

#endif