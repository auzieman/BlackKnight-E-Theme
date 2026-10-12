#!/bin/sh
# Deterministic slicing of approved artwork into the existing donor image slots.
set -eu
base=$1
material=$2
output=$3
mkdir -p "$output"
slice() {
 name=$1; image=$2; crop=$3; size=$4; rotate=${5:-null}
 ffmpeg -hide_banner -loglevel error -threads 1 -filter_complex_threads 1 \
  -i "$material/$image.png" -i "$base/wrk/$name.png" \
  -filter_complex "[0:v]crop=$crop,$rotate,scale=$size:flags=lanczos,format=rgba[metal];[1:v]scale=$size:flags=neighbor,format=rgba,alphaextract[mask];[metal][mask]alphamerge[out]" \
  -map '[out]' -frames:v 1 -y "$output/$name.png"
}
slice default_top_left_corner plate 300:520:0:0 30:27
slice default_top_titlebar plate 1550:520:310:0 1024:27
# The 104px slot includes the control backing, not a 104px bevel.
# Match the left cap's 30px ornament scale, continuing center metal beneath controls.
ffmpeg -hide_banner -loglevel error -threads 1 -filter_complex_threads 1 \
 -i "$material/plate.png" -i "$base/wrk/default_top_right_corner.png" \
 -filter_complex "[0:v]split=2[body][edge];[body]crop=1550:520:310:0,scale=1024:27:flags=lanczos,crop=74:27:950:0,format=rgba[rail];[edge]crop=310:520:1860:0,scale=30:27:flags=lanczos,format=rgba[cap];[rail][cap]hstack=inputs=2[metal];[1:v]format=rgba,alphaextract[mask];[metal][mask]alphamerge[out]" \
 -map '[out]' -frames:v 1 -y "$output/default_top_right_corner.png"
slice default_left_border_mid plate 42:370:220:65 19:19
slice default_left_border_top plate 42:370:220:65 19:19
slice default_right_border plate 42:370:1900:65 19:19
slice default_bottom_left_corner plate 310:135:0:385 63:18
slice default_bottom_right_corner plate 310:135:1860:385 63:18
slice default_bottom_left plate 400:75:320:440 31:16
slice default_bottom_right plate 400:75:1420:440 31:16
slice default_bottom_mid plate 1100:75:520:440 78:16
slice e17_mini_button button 1248:1248:0:0 24:24

slice e17_shelf_bg2_h plate 2170:520:0:0 296:101
slice e17_shelf_bg2_v plate 2170:520:0:0 101:296 transpose=1
slice e17_shelf_bg3_v plate 2170:520:0:0 101:296 transpose=1
slice shelf_bar plate 2170:520:0:0 296:101
slice shelf_top plate 1100:50:520:0 4:4
slice shelf_bottom plate 1100:50:520:455 4:4
slice shelf_top_left plate 300:180:0:0 24:21
slice shelf_top_right plate 310:180:1860:0 24:21
slice shelf_bottom_left plate 300:180:0:340 24:21
slice shelf_bottom_right plate 310:180:1860:340 24:21
slice shelf_mid_left plate 42:370:220:65 24:5
slice shelf_mid_right plate 42:370:1900:65 24:5
slice shelf_ibar_bg button 1248:1248:0:0 64:48
