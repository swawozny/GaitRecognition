# GaitRecognition

## How to run

```
python app.py <gait3d_dataset_dir>
```

## Output
The script generates a json file that looks like this:
```json
{
{"p1s1": {
"camera_0": [
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]] , "32": [[93.75951290130615, 116.30941540002823]]},
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]] , "32": [[93.75951290130615, 116.30941540002823]]},


{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]}],
"camera_1": [
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]},
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]},

{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]}],

"camera_3": [
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]},
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]},

{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]}]
},
{"p1s2": {
"camera_0": [
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]},
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]},

{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]}],
"camera_1": [
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]},
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]},

{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]}],

"camera_3": [
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]},
{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]},

{"0": [[96.33454084396362, 122.18288987874985]], "1": [[94.20570373535156, 116.45960569381714]], "32": [[93.75951290130615, 116.30941540002823]]}]
}}

```

For each sequence in the gait 3d dataset we divide the video from each camera (there are 4 in total) into 135 frames and for each of these frames we determine the landmarks (mediapipe has 33)