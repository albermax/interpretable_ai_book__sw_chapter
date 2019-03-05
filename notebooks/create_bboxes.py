"""
Takes as argument the path to the ImageNet 2012 bounding boxes directory.
It will read all files and output a json-file containing
all the bounding box information.
"""

import json
import os
import sys

if __name__ == "__main__":
    dir_name = sys.argv[1]

    def between(l):
        l = l.strip()
        begin = l.find(">")
        end = begin+l[begin:].find("<")
        return l[begin+1:end]

    output = {}
    print("Files in directory:", len(os.listdir(dir_name)))
    for f_name in os.listdir(dir_name):
        d = {}
        with open(os.path.join(dir_name, f_name)) as f:
            for l in f.readlines():
                if "filename" in l:
                    d["filename"] = between(l)
                if "name" in l:
                    d["name"] = between(l)
                if "width" in l:
                    d["width"] = int(between(l))
                if "height" in l:
                    d["height"] = int(between(l))
                if "xmin" in l:
                    d["xmin"] = int(between(l))
                if "xmax" in l:
                    d["xmax"] = int(between(l))
                if "ymin" in l:
                    d["ymin"] = int(between(l))
                if "ymax" in l:
                    d["ymax"] = int(between(l))
        d["num"] = str(int(d["filename"][d["filename"].find("val_")+4:]))
        d["id"] = d["name"]+"_"+d["num"]
        output[d["filename"]] = d

    print("Read entries:", len(output))
    with open('imagenet2012_val_bboxes.json', 'w') as fp:
        json.dump(output, fp, sort_keys=True,
                  indent=4, separators=(',', ': '))
