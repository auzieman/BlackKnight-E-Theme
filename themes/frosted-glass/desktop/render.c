#include <Ecore.h>
#include <Ecore_Evas.h>
#include <Edje.h>
#include <stdio.h>
#include <stdlib.h>
static Evas_Object *load(Evas *e,const char *file,const char *group,int x,int y,int w,int h) {
 Evas_Object *o=edje_object_add(e);
 if (!edje_object_file_set(o,file,group)) {fprintf(stderr,"Cannot load %s: %s\n",group,edje_load_error_str(edje_object_load_error_get(o)));exit(1);}
 evas_object_move(o,x,y);evas_object_resize(o,w,h);evas_object_show(o);return o;
}
int main(int argc,char **argv) {
 if(argc!=3)return 2;
 ecore_evas_init();edje_init();
 Ecore_Evas *ee=ecore_evas_buffer_new(1000,650);if(!ee)return 1;
 Evas *e=ecore_evas_get(ee);
 Evas_Object *bg=evas_object_rectangle_add(e);evas_object_color_set(bg,65,85,99,255);evas_object_resize(bg,1000,650);evas_object_show(bg);
 for(int i=0;i<2;i++) {
  Evas_Object *o=load(e,argv[1],"e/widgets/border/default/border",35+i*55,30+i*255,820-i*130,220);
  edje_object_part_text_set(o,"e.text.title",i?"Inactive window — compact width":"Frosted workstation — focused window");
  Evas_Object *client=evas_object_rectangle_add(e);evas_object_color_set(client,232,240,242,255);edje_object_part_swallow(o,"e.swallow.client",client);evas_object_show(client);
  if(!edje_object_part_exists(o,"e.event.close")||!edje_object_part_exists(o,"e.swallow.client"))return 1;
  if(!i)edje_object_signal_emit(o,"e,state,focused","e");
  edje_object_message_signal_process(o);edje_object_calc_force(o);
 }
 Evas_Object *s=load(e,argv[1],"e/shelf/default/base",40,565,810,50);
 edje_object_signal_emit(s,"e,state,orientation,bottom","e");edje_object_message_signal_process(s);
 s=load(e,argv[1],"e/shelf/default/base",900,40,50,480);
 edje_object_signal_emit(s,"e,state,orientation,left","e");edje_object_message_signal_process(s);
 for(int i=0;i<40;i++)ecore_main_loop_iterate_may_block(0);
 const void *pixels=ecore_evas_buffer_pixels_get(ee);
 Evas_Object *img=evas_object_image_add(e);evas_object_image_size_set(img,1000,650);evas_object_image_alpha_set(img,0);evas_object_image_data_copy_set(img,(void *)pixels);
 int ok=evas_object_image_save(img,argv[2],NULL,NULL);
 printf("Native groups rendered: %s\n",argv[2]);
 ecore_evas_free(ee);edje_shutdown();ecore_evas_shutdown();return ok?0:1;
}
