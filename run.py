from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from ml import main_model as md
from ml import Human_Segmentation as hs

app = Flask(__name__);



#업로드 HTML 렌더링
@app.route('/upload')
def render_file():
   return render_template('upload.html')

#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #저장할 경로 + 파일명
      f.save('static/image/'+str(secure_filename(f.filename)))
      hs.segmentation_model('static/image/'+str(secure_filename(f.filename)))
      md.run_model(str(str(hs.timestr)+'.png'))
      return render_template(
                'index.html',                      
                sim=md.sim, 
                jso=md.result_json,     
                my_str="Hello Flask!",             
                my_list=[x + 1 for x in range(30)], 
                image_file="segmentation_img/"+str(str(hs.timestr)+'.png'),
                my_img='image/'+str(secure_filename(f.filename))
            )




# @app.route("/")
# def template_test():
#     return render_template(
#                 'index.html',                      
#                 title="Flask Template Test",      
#                 my_str="Hello Flask!",             
#                 my_list=[x + 1 for x in range(30)], 
#                 image_file="image/"+str(a)
#             )


if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5001, debug=True)
