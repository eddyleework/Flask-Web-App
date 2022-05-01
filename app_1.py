from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import numpy as np

app = Flask(__name__)

@app.route('/')
def render_file():
   return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      #image display====================
      imagefile = f.filename
      src_img_array = np.array(imagefile)
      test(src_img_array)
      #==================================
      return render_template('index.html', prediction = pred_str, probability = probability_str)
   test(src_img)

def test(image):
   print(image.shape)
   plt.imshow(image)
   plt.show()

   # src_img = cv2.resize(src_img, dsize=(224, 224))
   # src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
   # src_img = src_img / 255.0
   #
   # src_img_list.append(src_img)
   # src_img_array = np.array(src_img_list)
   # pred = new_model.predict(src_img_array)
   # class_names = ['chihuahua', 'jindo_dog', 'shepherd', 'yorkshire_terrier']
   # print(src_img_array.shape)
  #  pred = pred[0]
  #
  #  pred_str = class_names[np.argmax(pred)]
  #  print(pred_str)
  #  prob_str = (max(pred)) * 100
  #  print(prob_str)
  #  plt.title('label:' + pred_str + '\nprobability:' + str(int(prob_str)))
  #
  #  plt.imshow(src_img)
  #  plt.show()
  #
  #  print("test called and respond")


if __name__ == '__main__':
    #서버 실행
   app.run(debug = True)
