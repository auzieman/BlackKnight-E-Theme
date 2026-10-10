#include <Elementary.h>
#include <stdio.h>
#include <string.h>
static Evas_Object *layout;
static Eina_Bool paused;
static void phase(void *data,Evas_Object *obj,const char *signal,const char *source){
 (void)data;(void)obj;printf("PHASE %.3f %s %s\n",ecore_time_get(),signal,source);fflush(stdout);
}
static void quit(void *data,Evas_Object *obj,void *event){(void)data;(void)obj;(void)event;elm_exit();}
static Eina_Bool end(void *data){(void)data;puts("PREVIEW_COMPLETE");fflush(stdout);elm_exit();return ECORE_CALLBACK_CANCEL;}
static void key(void *data,Evas *canvas,Evas_Object *obj,void *event){
 (void)data;(void)canvas;(void)obj;const char *name=((Evas_Event_Key_Down*)event)->keyname;
 if(!strcmp(name,"Escape"))elm_exit();
 else if(!strcmp(name,"space")){paused=!paused;edje_object_signal_emit(elm_layout_edje_get(layout),paused?"bk,pause":"bk,resume","host");printf("PAUSED %d\n",paused);fflush(stdout);}
}
EAPI_MAIN int elm_main(int argc,char **argv){
 if(argc!=2){fprintf(stderr,"Usage: %s WALLPAPER_EDJ\n",argv[0]);return 2;}
 Evas_Object *win=elm_win_util_standard_add("blackknight-storm-preview","BlackKnight animated wallpaper proof");
 elm_win_autodel_set(win,EINA_TRUE);evas_object_smart_callback_add(win,"delete,request",quit,NULL);
 layout=elm_layout_add(win);if(!elm_layout_file_set(layout,argv[1],"e/desktop/background"))return 1;
 evas_object_size_hint_weight_set(layout,EVAS_HINT_EXPAND,EVAS_HINT_EXPAND);evas_object_size_hint_align_set(layout,EVAS_HINT_FILL,EVAS_HINT_FILL);elm_win_resize_object_add(win,layout);
 edje_object_signal_callback_add(elm_layout_edje_get(layout),"bk,phase,*","wallpaper",phase,NULL);
 evas_object_event_callback_add(win,EVAS_CALLBACK_KEY_DOWN,key,NULL);
 evas_object_resize(win,960,540);evas_object_show(layout);evas_object_show(win);
 ecore_timer_add(130,end,NULL);puts("READY Space pauses/resumes; Escape closes; auto-close after 130 seconds");fflush(stdout);elm_run();return 0;
}
ELM_MAIN()
