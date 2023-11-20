from PIL import Image
import pytesseract
from os import listdir
from os.path import isfile, join
import plotly.graph_objects as go
from config import sims

path = './screenshots'

# loop through all the steps
for step in sims['sb_bn_3bp']['steps']:

    results = []
    # loop through all the screenshots
    for im_file in [f for f in listdir(path) if isfile(join(path, f))]:

        # if has prefix
        if im_file.startswith(step['ss_prefix']):

            # extract text from image
            image = Image.open(join(path, im_file))
            image_to_text = pytesseract.image_to_string(image, lang='eng')
            results.append(image_to_text.strip('\n\x0c').replace('(', '').replace(')', '').replace('%', '').split(' ')[-1])

    print(step['title'], results)
    fig = go.Figure(data=[go.Table(header=dict(values=step['captures']),
                     cells=dict(values=results))
                    ])
    fig.update_layout(title_text=step['title'])
    fig.show()
