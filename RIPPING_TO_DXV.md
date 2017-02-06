#!/usr/bin/env bash

# output, videoUrl, startTime, endTime
source $(dirname $0)/bashArgumentParser.sh

if [ ! -f "downloads/$VIDEOURL.mp4" ]; then
  youtube-dl $VIDEOURL -o "downloads/$VIDEOURL.%(ext)s" --recode-video mp4 --no-check-certificate --prefer-insecure
else
  echo "Skipping downloading $VIDEOURL because it already exists!"
fi

if [ ! -f "videos/$FILE_NAME.mp4" ]; then
  if [ -n "$ENDTIME" ]; then
    echo "Applying start/end times..."
    python editVideo.py --input="$VIDEOURL" --output="$FILE_NAME" --startTime="$STARTTIME" --endTime="$ENDTIME"
  else
    echo "Copying downloaded video..."
    cp downloads/$VIDEOURL.mp4 videos/$FILE_NAME.mp4
  fi
else
  echo "Skipping creating $FILE_NAME because it already exists!"
fi

# trying dis. just give urls to stdin
youtube-dl --output "videos/%(id)s - %(title)s.%(ext)s" -a -

# trying to get pulse working
youtube-dl https://vimeo.com/197854878 --list-formats

# do I have qt-export?

youtube-dl https://vimeo.com/197854878 --output "videos/%(id)s - %(title)s.%(ext)s" --recode-video mp4
youtube-dl https://vimeo.com/197854878 --output "videos/%(id)s - %(title)s.%(ext)s" --recode-video flv
youtube-dl https://vimeo.com/197854878 --output "videos/%(id)s - %(title)s.%(ext)s" --recode-video ogg
youtube-dl https://vimeo.com/197854878 --output "videos/%(id)s - %(title)s.%(ext)s" --recode-video webm
youtube-dl https://vimeo.com/197854878 --output "videos/%(id)s - %(title)s.%(ext)s" --recode-video mkv
youtube-dl https://vimeo.com/197854878 --output "videos/%(id)s - %(title)s.%(ext)s" --recode-video avi

youtube-dl https://vimeo.com/90747156  --output "%(id)s - %(title)s.%(ext)s"

youtube-dl https://vimeo.com/173654333 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/133342821 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/90747156  --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/57066384  --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/194347061 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/113442782 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/77499515  --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/17335122  --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/9463248   --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/9462893   --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/168422600 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/135815327 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/188568661 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/197854878 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl https://vimeo.com/189611593 --output "videos/%(id)s - %(title)s.%(ext)s"
# youtube-dl mizfWiGSdTg --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl BtgIPJT2s20 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl Uk_8yojgSbQ --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl Vp3FJkkXHLs --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl Uj4II6m79VY --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl UMUtbB_60bA --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl Z9qGWIENgA4 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl h-qGj9nX7y4 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl 8PGLC-Em0mk --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl m6GkVyHmCw8 --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl jX_PlfxE1wI --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl OZCqz-BPhyE --output "videos/%(id)s - %(title)s.%(ext)s"
youtube-dl BgP9tzt9_Z8 --output "videos/%(id)s - %(title)s.%(ext)s"