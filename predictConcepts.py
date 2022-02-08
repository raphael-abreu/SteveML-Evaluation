from clarifai.errors import ApiError
from clarifai.rest import ClarifaiApp
import json 

import os
directory = 'data/Action'
outDir = 'data/recognition/'

app = ClarifaiApp(api_key='___')

m = app.public_models.general_model

alreadyListedFiles = [os.path.splitext(f)[0] for f in os.listdir(outDir) if os.path.isfile(os.path.join(outDir, f))]

for filename in os.listdir(directory):
    nameToSave = os.path.splitext(filename)[0]
    item = os.path.join(directory, filename)
    if os.path.isfile(item) and nameToSave not in alreadyListedFiles:

        try:
            print('curr file: %s' % filename)
            # There are also methods m.predict_by_base64 and m.predict_by_bytes
            response = m.predict_by_filename(os.path.join(directory, filename),is_video=True,sample_ms=1000)
        except ApiError as e:
            print('Error status code: %d' % e.error_code)
            print('Error description: %s' % e.error_desc)
            if e.error_details:
                print('Error details: %s' % e.error_details)
            exit(1)


        frames = response['outputs'][0]['data']['frames']
        with open(outDir+nameToSave+'.json', 'w') as f:
            json.dump(frames, f)

        for frame in frames:
            print('###%d###' % frame['frame_info']['time'])
            #print('#\n')
            #f.write('###%d###\n' % frame['frame_info']['time'])
            for concept in frame['data']['concepts']:
                print('%s %f' % (concept['name'], concept['value']))
                #f.write('%s %f\n' % (concept['name'], concept['value']))
       
