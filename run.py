from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from ml import main_model as md
from ml import Human_Segmentation as hs

caption = {'바캉스' : '휴일이나 여행지에서 입을 것 같은 느슨하고 편안한 개방적인 스타일 입니다.', 
            '보헤미안' : '자유분방한 생활을 즐기는 유랑인 보헤미안의 스타일을 뜻하며 헐렁한 레이어드와 패치, 자수가 특징인 스타일 입니다.', 
            '섹시' : '신체의 노출이 많거나 몸에 꼭 맞는 의상이 특징인 여성스러운 스타일 입니다.', 
            '스포티' : '자연스럽고 건강해 보이며 입기에 편한 기능성을 중요시하는 활동적인 스타일 입니다.', 
            '오피스룩' : '직장인들이 선호하는 깔끔하고 편안하면서 세련된 스타일입니다.', 
            '캐주얼' : '격식에 메이지 않고 가볍고 부담 없이 입을 수 있는 자연스러운 스타일 입니다.', 
            '트레디셔널' : '세련되고 도회적이며 여유로운 편안함을 조화롭게 추구하는 신사복 스타일 입니다.', 
            '페미닌' : '각 시대에 맞는 여성스러움을 표현한 우아하고 러블리한 분위기의 스타일 입니다.', 
            '힙합' : '스트릿 문화에 기반한 자신의 개성을 살린 자유로운 분위기의 스타일 입니다.'}

app = Flask(__name__)

#업로드 HTML 렌더링
@app.route('/')
def render_file():
   return render_template('index.html')

#파일 업로드 처리
@app.route('/result', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #저장할 경로 + 파일명
      f.save('static/image/'+str(secure_filename(f.filename)))
      hs.segmentation_model('static/image/'+str(secure_filename(f.filename)))
      md.run_model(str(str(hs.timestr)+'.png'))
      return render_template(
                'result.html',
                caption=caption,
                img_src=md.img_src,                   
                shop_name=md.shop_name,
                price=md.price,
                item_name=md.item_name,
                item_link=md.item_link,
                category=md.category,
                jso=md.result_json,   
                image_file="segmentation_img/"+str(str(hs.timestr)+'.png'),
                my_img='image/'+str(secure_filename(f.filename))
            )

if __name__ == '__main__':
   app.run(host="146.56.143.57", port="80")
