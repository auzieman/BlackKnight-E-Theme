#include <Elementary.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static char *previous;
static Eina_Bool restore(void *data) {
 (void)data;
 elm_theme_set(NULL, previous);
 elm_config_all_flush();
 printf("RESTORED %s\n", previous); fflush(stdout);
 elm_exit(); return ECORE_CALLBACK_CANCEL;
}
EAPI_MAIN int elm_main(int argc, char **argv) {
 const char *current=elm_theme_get(NULL);
 if (argc==1) { printf("PROFILE %s\nTHEME %s\n", elm_config_profile_get(), current); return 0; }
 if (argc==3 && !strcmp(argv[1],"--restore")) {
  elm_theme_set(NULL,argv[2]); elm_config_all_flush();
  printf("RESTORED %s\n",argv[2]); return 0;
 }
 if (argc!=2 && !(argc==4 && !strcmp(argv[2],"--previous"))) { fprintf(stderr,"Usage: %s [THEME_EDJ]\n",argv[0]); return 2; }
 if (!edje_file_group_exists(argv[1], "e/widgets/border/default/border")) { fprintf(stderr,"Missing desktop border group\n"); return 1; }
 previous=strdup(argc==4 ? argv[3] : current);
 if (!previous) return 1;
 // Arm the rollback before broadcasting the trial theme.
 if (!ecore_timer_add(20.0,restore,NULL)) { free(previous); return 1; }
 size_t length=strlen(argv[1])+strlen(previous)+2;
 char *trial=malloc(length);
 if (!trial) { free(previous); return 1; }
 snprintf(trial,length,"%s:%s",argv[1],previous);
 printf("PREVIOUS %s\nTRIAL %s\nROLLBACK 20 seconds\n",previous,trial);fflush(stdout);
 elm_theme_set(NULL, trial);
 free(trial);
 elm_config_all_flush();
 elm_run();
 free(previous); return 0;
}
ELM_MAIN()
