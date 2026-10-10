/* Replace only existing image payloads in a copy of a working EDJ. */
#define EDJE_EDIT_IS_UNSTABLE_AND_I_KNOW_ABOUT_IT
#include <Ecore_Evas.h>
#include <Edje.h>
#include <Edje_Edit.h>
#include <Eet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static const char *slots[]={"default_top_left_corner","default_top_titlebar","default_top_right_corner","default_left_border_mid","default_left_border_top","default_right_border","default_bottom_right_corner","default_bottom_right","default_bottom_mid","default_bottom_left","default_bottom_left_corner","e17_mini_button","e17_shelf_bg2_h","e17_shelf_bg2_v","e17_shelf_bg3_v","shelf_bar","shelf_bottom","shelf_top","shelf_bottom_left","shelf_bottom_right","shelf_top_left","shelf_top_right","shelf_mid_left","shelf_mid_right","shelf_ibar_bg"};
#define SLOT_COUNT (sizeof(slots)/sizeof(slots[0]))
int main(int argc,char **argv) {
 if(argc!=4){fprintf(stderr,"Usage: %s ORIGINAL_EDJ COPIED_EDJ ASSET_DIR\n",argv[0]);return 2;}
 if(!strcmp(argv[1],argv[2]))return 2;
 ecore_evas_init();edje_init();eet_init();
 Ecore_Evas *ee=ecore_evas_buffer_new(1,1);if(!ee)return 1;
 Evas *canvas=ecore_evas_get(ee);
 Evas_Object *obj=edje_edit_object_add(canvas);
 if(!edje_object_file_set(obj,argv[2],"e/widgets/border/default/border"))return 1;
 int ids[SLOT_COUNT];char name[256];
 for(int i=0;i<(int)SLOT_COUNT;i++){
  snprintf(name,sizeof name,"wrk/%s.png",slots[i]);ids[i]=edje_edit_image_id_get(obj,name);
  if(ids[i]<0){fprintf(stderr,"Missing donor image %s\n",name);return 1;}
 }
 evas_object_del(obj);
 Eet_File *out=eet_open(argv[2],EET_FILE_MODE_READ_WRITE);if(!out)return 1;
 for(int i=0;i<(int)SLOT_COUNT;i++){
  char path[4096],key[128];snprintf(path,sizeof path,"%s/%s.png",argv[3],slots[i]);snprintf(key,sizeof key,"edje/images/%d",ids[i]);
  Evas_Object *im=evas_object_image_add(canvas);evas_object_image_file_set(im,path,NULL);
  if(evas_object_image_load_error_get(im)!=EVAS_LOAD_ERROR_NONE)return 1;
  int w,h;evas_object_image_size_get(im,&w,&h);
  unsigned int ow,oh;int a,c,q;Eet_Image_Encoding l;
  if(!eet_data_image_header_read(out,key,&ow,&oh,&a,&c,&q,&l)||(ow!=(unsigned)w && strcmp(slots[i],"default_top_titlebar"))||oh!=(unsigned)h){fprintf(stderr,"Dimension mismatch %s\n",key);return 1;}
  void *pixels=evas_object_image_data_get(im,EINA_FALSE);
  if(!pixels||!eet_data_image_write(out,key,pixels,w,h,evas_object_image_alpha_get(im),1,100,EET_IMAGE_LOSSLESS))return 1;
  printf("REMAPPED %s %s %dx%d\n",slots[i],key,w,h);evas_object_del(im);
 }
 if(eet_close(out)!=EET_ERROR_NONE)return 1;
 Eet_File *original=eet_open(argv[1],EET_FILE_MODE_READ),*changed=eet_open(argv[2],EET_FILE_MODE_READ);if(!original||!changed)return 1;
 int count=0,newcount=0,verified=0,replaced=0;char **keys=eet_list(original,"*",&count),**newkeys=eet_list(changed,"*",&newcount);
 if(count!=newcount)return 1;
 for(int i=0;i<count;i++){
  int selected=0;for(int j=0;j<(int)SLOT_COUNT;j++){char key[128];snprintf(key,sizeof key,"edje/images/%d",ids[j]);if(!strcmp(key,keys[i]))selected=1;}
  int n=0,m=0;void *x=eet_read(original,keys[i],&n),*y=eet_read(changed,keys[i],&m);
  if(!x||!y)return 1;
  if(selected){if(n==m&&!memcmp(x,y,n)){fprintf(stderr,"Image unchanged %s\n",keys[i]);return 1;}replaced++;}
  else {if(n!=m||memcmp(x,y,n)){fprintf(stderr,"Unexpected change %s\n",keys[i]);return 1;}verified++;}
  free(x);free(y);
 }
 printf("VERIFIED %d unchanged entries; %d image-only replacements\n",verified,replaced);
 free(keys);free(newkeys);eet_close(original);eet_close(changed);ecore_evas_free(ee);edje_shutdown();eet_shutdown();ecore_evas_shutdown();return replaced==(int)SLOT_COUNT?0:1;
}
