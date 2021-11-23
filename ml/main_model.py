import numpy as np
from tensorflow import keras
import tensorflow as tf
from keras.applications.imagenet_utils import preprocess_input
from keras.applications.xception import Xception
from keras.models import Model, load_model, Sequential



def img_load(img_path):#이미지 로드 및 어레이 변경
  image = keras.preprocessing.image.load_img(img_path, target_size=(256,128))
  image_array = keras.preprocessing.image.img_to_array(image)
  return image_array,image

def run_model(input_segimg):
    model = keras.models.load_model('./model/best_model_final.h5', custom_objects=None, compile=True)#모델로드
    img_path = './static/segmentation_img/'+str(input_segimg)#사용자 사진
    image_array,img= img_load(img_path) #사용자 사진 넣은 결과
    image_input_type = np.array([image_array])
    result = model.predict(image_input_type)#최종결과
    result_class = np.argmax(result)
    print(img_path, ", Class_Predict : " + str(result_class))

    simillarity_model = tf.keras.models.load_model("./model/image simillarity_1.h5",custom_objects=None, compile=True)#유사도 모델

    class FeatureExtractor: # 추출 
        def __init__(self):
            self.model = simillarity_model
        def extract(self, img):
            # Resize the image
            img = img.resize((299, 299))
            # Convert the image color space
            img = img.convert('RGB')
            # Reformat the image
            x = keras.preprocessing.image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            # Extract Features
            feature = self.model.predict(x)[0]
            return feature / np.linalg.norm(feature)

    fe=FeatureExtractor()


    if(result_class):
        features=np.load("class_array/"+str(result_class)+"/all_p.npy")
        paths=np.load("class_array/2/all_f.npy")
    else:
        print("error")
  
    query = fe.extract(img)

    dists = np.linalg.norm(features - query, axis=1)
    ids = np.argsort(dists)[:6]
    scores = [(dists[id], paths[id], id) for id in ids]

    global sim
    sim=[]
    for i in range(len(scores)):
        sim.append(scores[i][1])

    
    trans=result.round(2)*100
    class_name=['바캉스','보헤미안','섹시','스포티','오피스룩','캐주얼','트레디셔널','페미닌','힙합']
    global result_json
    result_json=dict(zip(class_name,trans[0]))