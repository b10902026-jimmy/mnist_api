import numpy as np
import model
import base64
import cv2
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_cors import cross_origin
from flasgger import Swagger 

app = Flask(__name__)
app.config['SWAGGER'] = {
    "title": "My API",
    "description": "My API",
    "version": "1.0.2",
    "termsOfService": "",
    "hide_top_bar": True
}

CORS(app)
Swagger(app)

@app.route('/')
@cross_origin()
def index():
    return 'hello!!'

@app.route('/predict', methods=['POST'])
@cross_origin()
def postInput():
    # 取得前端傳過來的數值
    """
    mnist number prediction
    ---
    
    consumes:
        - application/json
    produces: 
        - application/json
    
    parameters:
        -   name: base 64 code
            in: body
            required: true
            schema : # <--- What?
            example:
                "picture" : "base64 Code"
    responses:
      200:
        description: A prediction(number) of uploaded picture
        example:
            "prediction" : "4"
    """
    insertImage = request.get_json()
    img_b64decode = base64.b64decode(insertImage['picture'])
    img_nparray = np.frombuffer(img_b64decode,np.uint8)
    input_img = cv2.imdecode(img_nparray,cv2.IMREAD_COLOR)
    
    result = model.predict(input_img)


    return jsonify({'Prediction': str(result)})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)


