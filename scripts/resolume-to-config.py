import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/marten/Dropbox/Resolume Arena 5/compositions/2017-05-13 hypno soft open.avc')
root = tree.getroot() # 'composition'
# print root

def coord_to_key(layer, track):
    layers = [
        [
          36, 37, 38, 39,
          44, 45, 46, 47,
          52, 53, 54, 55,
          60, 61, 62, 63
        ],
        [
          40, 41, 42, 43,
          48, 49, 50, 51,
          56, 57, 58, 59,
          64, 65, 66, 67
        ],
        [
          68, 69, 70, 71,
          76, 77, 78, 79,
          84, 85, 86, 87,
          92, 93, 94, 95
        ],
        [
          72, 73, 74, 75,
          80, 81, 82, 83,
          88, 89, 90, 91,
          96, 97, 98, 99
        ]
    ]

    try:
        return layers[layer][track]
    except IndexError:
        return -1

clips = root.findall("./decks/deck[@name='Effect Clip']/clip")
for clip in clips:
    # settings for effect clips only
    settings = clip.find("settings/name[@value]..")
    if settings is not None:
        clip_name = settings.find('nameGiven').get('value')
        layer_idx = int(clip.get('layerIndex'))
        track_idx = int(clip.get('trackIndex'))
        key = coord_to_key(layer_idx, track_idx)

        param_names = list()
        params = settings.findall('parameters/parameter')
        for param in params:
            param_names.append(param.find('nameGiven').get('value'))
        print [key, clip_name, param_names], ","
    settings = clip.find("settings/name[@value='Gradients']..")


# All 'neighbor' grand-children of 'country' children of the top-level
# elements
# root.findall("./country/neighbor")
#
# # Nodes with name='Singapore' that have a 'year' child
# root.findall(".//year/..[@name='Singapore']")
#
# # 'year' nodes that are children of nodes with name='Singapore'
# root.findall(".//*[@name='Singapore']/year")
#
# # All 'neighbor' nodes that are the second child of their parent
# root.findall(".//neighbor[2]")
