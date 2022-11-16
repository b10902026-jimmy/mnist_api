import numpy as np
import model1
import base64
import cv2
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
@cross_origin()
def index():
    return 'hello!!'

@app.route('/predict', methods=['POST'])
@cross_origin()
def postInput():
    # 取得前端傳過來的數值
    insertImage = request.get_json()
    img_b64decode = base64.b64decode(insertImage['picture'])
    img_nparray = np.frombuffer(img_b64decode,np.uint8)
    input_img = cv2.imdecode(img_nparray,cv2.IMREAD_COLOR)
    
    result = model1.predict(input_img)


    return jsonify({'Prediction': str(result)})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)


