#include <Elementary.h>
#include <stdio.h>
#include <string.h>
static Evas_Object *bar, *control, *window, *status;
static Eina_Bool disabled, hidden, long_title;
static unsigned int width_index = 1;
static void report(const char *text) {
 elm_object_text_set(status, text); printf("%s\n", text); fflush(stdout);
}
static void active(void *data, Evas_Object *obj, void *event_info) {
 (void)obj; (void)event_info;
 if (!hidden) edje_object_signal_emit(elm_layout_edje_get(bar), (const char *)data, "host");
}
static void action(void *data, Evas_Object *obj, const char *emission, const char *source) {
 (void)data; (void)obj;
 if (disabled || hidden) return;
 char message[256];
 snprintf(message, sizeof(message), "Skin action: %s [%s]", emission, source);
 report(message);
 /* Demonstration logs intent. Desktop/player adapters own actual operations. */
}
static void quit(void *data, Evas_Object *obj, void *event_info) {
 (void)data; (void)obj; (void)event_info; elm_exit();
}
static void key(void *data, Evas *canvas, Evas_Object *obj, void *event_info) {
 Evas_Event_Key_Down *event = event_info;
 const char *name = event->keyname;
 (void)data; (void)canvas; (void)obj;
 if (!strcmp(name, "Escape")) elm_exit();
 else if (!strcmp(name, "F1") && !hidden) { active("bk,state,active", window, NULL); report("Focused: one sweep"); }
 else if (!strcmp(name, "F2") && !hidden) { active("bk,state,inactive", window, NULL); report("Inactive: sweep cancelled"); }
 else if (!strcmp(name, "F3")) {
  const char *names[] = {"close", "maximize", "minimize"};
  disabled = !disabled;
  const char *signal = disabled ? "bk,control,disabled" : "bk,control,enabled";
  for (unsigned int i=0; i<3; ++i) edje_object_signal_emit(elm_layout_edje_get(bar), signal, names[i]);
  edje_object_signal_emit(elm_layout_edje_get(control), signal, "activate");
  report(disabled ? "Controls disabled" : "Controls enabled");
 } else if (!strcmp(name, "F4")) {
  long_title = !long_title;
  edje_object_part_text_set(elm_layout_edje_get(bar), "title", long_title ?
   "BlackKnight — deliberately long title for checking ellipsis and button clearance" : "BlackKnight — live title");
  report("Live title changed");
 } else if (!strcmp(name, "F5")) {
  if (!hidden) {
   active("bk,state,hidden", window, NULL);
   evas_object_hide(bar); evas_object_hide(control); hidden=EINA_TRUE;
  } else {
   hidden=EINA_FALSE; evas_object_show(bar); evas_object_show(control);
   active("bk,state,active", window, NULL);
  }
  report(hidden ? "Skin hidden: glint cancelled" : "Skin shown");
 } else if (!strcmp(name, "F6")) {
  const int widths[] = {480, 800, 1200};
  width_index=(width_index+1)%3; evas_object_resize(window, widths[width_index], 240);
  char message[80]; snprintf(message, sizeof(message), "Requested width: %d", widths[width_index]); report(message);
 }
}
EAPI_MAIN int elm_main(int argc, char **argv) {
 if (argc != 2) { fprintf(stderr, "Usage: %s MATERIAL_EDJ\n", argv[0]); return 2; }
 Evas_Object *win=elm_win_util_standard_add("blackknight-material", "BlackKnight raster skin proof");
 window=win;
 evas_object_smart_callback_add(win, "delete,request", quit, NULL);
 Evas_Object *box=elm_box_add(win);
 evas_object_size_hint_weight_set(box, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
 elm_win_resize_object_add(win, box); evas_object_show(box);
 bar=elm_layout_add(win);
 if (!elm_layout_file_set(bar, argv[1], "bk/material/titlebar")) { fprintf(stderr, "Cannot load titlebar from %s\n", argv[1]); return 1; }
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
 control=elm_layout_add(win);
 if (!elm_layout_file_set(control, argv[1], "bk/material/control")) { fprintf(stderr, "Cannot load control from %s\n", argv[1]); return 1; }
 evas_object_size_hint_min_set(control, 48, 48);
 evas_object_size_hint_max_set(control, 48, 48);
 elm_box_pack_end(box, control); evas_object_show(control);
 edje_object_signal_callback_add(elm_layout_edje_get(control), "bk,action,*", "*", action, NULL);
 Evas_Object *help=elm_label_add(win);
 elm_object_text_set(help, "F1 focus · F2 inactive · F3 enable/disable<br/>F4 title · F5 hide/show · F6 width · Escape quit");
 elm_box_pack_end(box, help); evas_object_show(help);
 status=elm_label_add(win); elm_box_pack_end(box, status); evas_object_show(status);
 report("Hover, press and click raster controls");
 evas_object_event_callback_add(win, EVAS_CALLBACK_KEY_DOWN, key, NULL);
 const char *keys[]={"F1","F2","F3","F4","F5","F6","Escape"};
 for (unsigned int i=0; i<sizeof(keys)/sizeof(keys[0]); ++i)
  if (!evas_object_key_grab(win, keys[i], 0, 0, EINA_TRUE)) fprintf(stderr, "Cannot grab key %s\n", keys[i]);
 evas_object_resize(win, 800, 240); evas_object_show(win);
 active("bk,state,active", win, NULL);
 elm_run(); return 0;
}
ELM_MAIN()
