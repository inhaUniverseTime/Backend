import base64
from PIL import Image
from io import BytesIO

# base64로 인코딩된 이미지 문자열. 예시를 위해 짧게 처리함.
encoded_image = ""

# base64 문자열을 바이트로 디코딩
image_bytes = base64.b64decode(encoded_image)

# BytesIO를 사용해 디코딩된 바이트를 이미지로 변환
image = Image.open(BytesIO(image_bytes))

# 이미지를 파일로 저장
image.save("decoded_image.png")

print("이미지가 성공적으로 저장되었습니다.")
