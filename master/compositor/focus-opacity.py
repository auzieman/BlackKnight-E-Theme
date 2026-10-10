#!/usr/bin/env python3
"""Temporary X11 focus opacity preview; restores original properties on exit."""
import ctypes as C, ctypes.util, signal, time
x=C.CDLL(ctypes.util.find_library('X11'))
x.XOpenDisplay.argtypes=[C.c_char_p];x.XOpenDisplay.restype=C.c_void_p
x.XDefaultRootWindow.argtypes=[C.c_void_p];x.XDefaultRootWindow.restype=C.c_ulong
x.XInternAtom.argtypes=[C.c_void_p,C.c_char_p,C.c_int];x.XInternAtom.restype=C.c_ulong
x.XGetWindowProperty.argtypes=[C.c_void_p,C.c_ulong,C.c_ulong,C.c_long,C.c_long,C.c_int,C.c_ulong,C.POINTER(C.c_ulong),C.POINTER(C.c_int),C.POINTER(C.c_ulong),C.POINTER(C.c_ulong),C.POINTER(C.POINTER(C.c_ubyte))]
x.XChangeProperty.argtypes=[C.c_void_p,C.c_ulong,C.c_ulong,C.c_ulong,C.c_int,C.c_int,C.POINTER(C.c_ubyte),C.c_int]
x.XDeleteProperty.argtypes=[C.c_void_p,C.c_ulong,C.c_ulong]
x.XFree.argtypes=[C.c_void_p];x.XFlush.argtypes=[C.c_void_p];x.XCloseDisplay.argtypes=[C.c_void_p]
# Windows may close during the trial; stale XIDs must not prevent restoration.
ERR=C.CFUNCTYPE(C.c_int,C.c_void_p,C.c_void_p)
handler=ERR(lambda *_:0);x.XSetErrorHandler.argtypes=[ERR];x.XSetErrorHandler(handler)
d=x.XOpenDisplay(None)
if not d:raise SystemExit('No X display')
root=x.XDefaultRootWindow(d)
def atom(name):return x.XInternAtom(d,name.encode(),0)
def get(win,name):
 typ=C.c_ulong();fmt=C.c_int();n=C.c_ulong();remaining=C.c_ulong();data=C.POINTER(C.c_ubyte)()
 result=x.XGetWindowProperty(d,win,atom(name),0,4096,0,0,C.byref(typ),C.byref(fmt),C.byref(n),C.byref(remaining),C.byref(data))
 values=[]
 if result==0 and fmt.value==32 and data:values=list(C.cast(data,C.POINTER(C.c_ulong))[:n.value])
 if data:x.XFree(data)
 return values
opacity=atom('_NET_WM_WINDOW_OPACITY');cardinal=atom('CARDINAL')
def put(win,value):
 if value is None:x.XDeleteProperty(d,win,opacity)
 else:
  v=C.c_ulong(value);x.XChangeProperty(d,win,opacity,cardinal,32,0,C.cast(C.byref(v),C.POINTER(C.c_ubyte)),1)
original={};last={};stop=False
normal=atom('_NET_WM_WINDOW_TYPE_NORMAL');fullscreen=atom('_NET_WM_STATE_FULLSCREEN')
def finish(*_):
 global stop
 stop=True
signal.signal(signal.SIGTERM,finish);signal.signal(signal.SIGINT,finish)
print('TRIAL inactive ordinary windows 92%; originals restored after 20 seconds',flush=True)
try:
 end=time.monotonic()+20
 while not stop and time.monotonic()<end:
  active=get(root,'_NET_ACTIVE_WINDOW');active=active[0] if active else 0
  for win in get(root,'_NET_CLIENT_LIST'):
   types=get(win,'_NET_WM_WINDOW_TYPE')
   if types and normal not in types:continue
   if win not in original:
    old=get(win,'_NET_WM_WINDOW_OPACITY');original[win]=old[0] if old else None
   base=original[win];value=base
   transient=get(active,'WM_TRANSIENT_FOR') if active else []
   if win!=active and win not in transient and fullscreen not in get(win,'_NET_WM_STATE'):
    value=min(base if base is not None else 0xffffffff,round(0xffffffff*.92))
   if win not in last or last[win]!=value:put(win,value);last[win]=value
  x.XFlush(d);time.sleep(.2)
finally:
 for win,value in original.items():put(win,value)
 x.XFlush(d);x.XCloseDisplay(d)
 print('RESTORED original opacity properties for',len(original),'windows',flush=True)
