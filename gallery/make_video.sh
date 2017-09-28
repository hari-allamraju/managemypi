cd ~/FTP/Hall
rm -f *.mp4
cat *.jpg 2>/dev/null| avconv -f image2pipe -c:v mjpeg -i - -r 25 -map 0 out.mp4
cd ~/FTP/HariRoom
rm -f *.mp4
cat *.jpg 2>/dev/null| avconv -f image2pipe -c:v mjpeg -i - -r 25 -map 0 out.mp4