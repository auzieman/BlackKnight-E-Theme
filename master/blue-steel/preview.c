#include <Elementary.h>
#include <stdio.h>
static Evas_Object *bar;
static void active(void *data, Evas_Object *obj, void *event_info) {
 (void)obj; (void)event_info;
 edje_object_signal_emit(elm_layout_edje_get(bar), (const char *)data, "host");
}
static void action(void *data, Evas_Object *obj, const char *emission, const char *source) {
 (void)data; (void)obj;
 printf("Skin action: %s [%s]\n", emission, source);
 fflush(stdout);
 /* Demonstration logs intent. Desktop/player adapters own actual operations. */
}
static void quit(void *data, Evas_Object *obj, void *event_info) {
 (void)data; (void)obj; (void)event_info; elm_exit();
}
EAPI_MAIN int elm_main(int argc, char **argv) {
 if (argc != 2) { fprintf(stderr, "Usage: %s MATERIAL_EDJ\n", argv[0]); return 2; }
 Evas_Object *win=elm_win_util_standard_add("blackknight-material", "BlackKnight raster skin proof");
 evas_object_smart_callback_add(win, "delete,request", quit, NULL);
 Evas_Object *box=elm_box_add(win);
 evas_object_size_hint_weight_set(box, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
 elm_win_resize_object_add(win, box); evas_object_show(box);
 bar=elm_layout_add(win);
 if (!elm_layout_file_set(bar, argv[1], "bk/material/titlebar")) return 1;
 evas_object_size_hint_min_set(bar, 480, 72);
 evas_object_size_hint_max_set(bar, -1, 72);
 evas_object_size_hint_weight_set(bar, EVAS_HINT_EXPAND, 0);
 evas_object_size_hint_align_set(bar, EVAS_HINT_FILL, 0);
 elm_box_pack_end(box, bar); evas_object_show(bar);
 edje_object_part_text_set(elm_layout_edje_get(bar), "title", "BlackKnight — live Edje title");
 edje_object_signal_callback_add(elm_layout_edje_get(bar), "bk,action,*", "*", action, NULL);
 evas_object_smart_callback_add(win, "focus,in", active, "bk,state,active");
 evas_object_smart_callback_add(win, "focus,out", active, "bk,state,inactive");
 evas_object_smart_callback_add(win, "iconified", active, "bk,state,hidden");
 Evas_Object *control=elm_layout_add(win);
 if (!elm_layout_file_set(control, argv[1], "bk/material/control")) return 1;
 evas_object_size_hint_min_set(control, 48, 48);
 evas_object_size_hint_max_set(control, 48, 48);
 elm_box_pack_end(box, control); evas_object_show(control);
 edje_object_signal_callback_add(elm_layout_edje_get(control), "bk,action,*", "*", action, NULL);
 evas_object_resize(win, 800, 160); evas_object_show(win);
 active("bk,state,active", win, NULL);
 elm_run(); return 0;
}
ELM_MAIN()
