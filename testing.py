# 需要的包
import base64
import requests

# 读取需要人别的图片
with open('./img/7KIDaUHuPceOx8m.jpg', 'rb') as f:
    img_data = f.read() 

# img_str的类型是字符串，decode()对字节类型变量进行解码，bytes->str
img_str = str(base64.b64encode(img_data), encoding="utf-8")

# 设置POST请求的数据
Data = {
    "ImageBase64": img_str,
    "IsCorrection": 1,
    "SecretId": "xxx",
    "SecretKey": "xxx"
}
# 向OCR API端点访问服务
result = requests.post('http://www.7-an.com:5000/api/paddle', data=Data)
print(result.text)
