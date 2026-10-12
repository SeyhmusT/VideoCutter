# Source - https://stackoverflow.com/a/37323543
# Posted by Zulko, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-12, License - CC BY-SA 4.0

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

full_video = "sad_dev.mp4"
cutted_video = "cutted_video.mp4"

cutter = ffmpeg_extract_subclip
cutter(full_video,"00:00","00:30",cutted_video)