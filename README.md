# K-Fashion-Project

K-Fashion image를 학습한 모델을 구현하고 모델을 통하여 사용자가 원하는 옷의 스타일을 분류해주고
그 스타일과 비슷한 옷을 추천 및 옷의 정보를 제공해주는 서비스


## Team

* [김영서](https://github.com/dudtjakdl)
* [송우진](https://github.com/woojinsong)
* [안성재](https://github.com/sammy0329)
* [정효준](https://github.com/Junepp)

## 아키텍쳐

![image](https://user-images.githubusercontent.com/38833676/178092665-c8d58d26-1801-446e-8ab8-2421dc42f4a9.png)

## 데이터셋

1. [K-Fashion 이미지 원본 데이터](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=51)

2. [쇼핑몰관련 옷 이미지 원본 데이터](https://drive.google.com/drive/folders/1YfTl0YbWvXDz7OtltbwKVovpd2m-UJhH?usp=sharing)

3. [쇼핑몰관련 옷 정보 데이터](https://drive.google.com/file/d/1HdHsg7P88ZZjLC1v2z-7wJoKs3_JeMXL/view?usp=sharing)

4. [K-Fashion 학습 이미지 데이터](https://drive.google.com/drive/folders/1X1dPSJg3IeWAIZk1D6AsWhuuH7pXs8pE?usp=sharing)


## 사용 기술

### 데이터 수집 & 전처리

1. 웹 크롤링
  - 17개의 쇼핑몰의 옷 데이터와 옷 정보를 크롤링 하여 이미지와 CSV 데이터 수집
  - Selenium, BeautifulSoup 라이브러리 사용

2. Human Segmentation
  - https://github.com/ternaus/people_segmentation
  - 사전 학습된 오픈소스 모델을 적용하여 훈련 이미지 데이터에서 인물 이외의 픽셀 제거
  
### 모델링
1. Data Augmentation
  - Xception model layer가 시작되기 전에 augmentation layer를 추가시켜 데이터 증강 및 모델 성능 확보
  
2. Image Classification
  - Xception 모델을 활용하여 9개의 라벨로 구성된 이미지 데이터셋을 모델에 학습
 
3. Recommandation Algorithm
  - VGG16 모델을 사용하여 마지막 FC1 dense layer에서 Feature Vector를 추출 후 인풋 데이터와 쇼핑몰 데이터의 Feature Vector의 유사도를 코사인유사도로 비교하여서 유사한 것을 추천


![image](https://user-images.githubusercontent.com/38833676/178094136-acfaaddc-de52-4ce2-a6b3-1fc2d5ce965d.png)

### 웹

1. 프론트엔드
  - HTML, CSS , JavaScript, BootStrap

  - 모델 및 데이터 처리를 웹에 동적으로 연동시키기 위해 파이썬 웹 프레임워크인 Flask 사용

2. 백엔드
  - 1. 클라이언트가 이미지 업로드
  - 2. 이미지를 받아와 segmentation 적용 후 서버에 업로드 시간을 제목으로 이미지 저장
  - 3. 분류 모델과 유사도 모델 적용
  - 4. 크롤링 데이터 csv에서 유사도 모델 결과로 나온 파일 이름을 조회 후 정보 추출
  - 5. Flask의 jinja2 템플릿을 이용하여 View 페이지인 result.html의 분석 결과를 동적으로 변환

## 사용법

1. 개발환경
  - Python 3.8.10
  - Colab
  - Tesorflow
  - HTML, CSS , JavaScript, BootStrap, Flask
  
2. 라이브러리

[requirements.txt](https://github.com/dudtjakdl/K-Fashion-Recommendation-Project/files/9075997/requirements.txt)


3. 실행 방법
  - 깃허브 파일 다운로드
  - [Install](https://drive.google.com/drive/folders/1-B7ECPEj1fe9wcHTtQVeTPn0tCv34LMN?usp=sharing)
  - best_model_final.h5, image simillarity_1.h5 -> model 폴더에 추가
  - class_array.zip 압축 해제 후 폴더 채로 상위(Root)폴더에 추가
  - shop_img.zip 압축 해제 후 이미지 전체를 static/shop_img 경로에 추가
  - run.py를 파이썬으로 실행
  - http://127.0.0.1:5001/upload 접속
  
## 시연 영상


https://user-images.githubusercontent.com/38833676/178096021-959d819d-2206-4bb3-bfb3-23ba7f714789.mp4
