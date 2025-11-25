# mini_converter   
여러 단위를 간단하게 변환하는 파이썬 패키지

---

##  개요

mini_converter는 일상에서 자주 사용하는 다양한 단위를  
간단한 파이썬 함수로 상호 변환할 수 있도록 만든 미니 프로젝트입니다.

이 패키지는 다음과 같은 단위 변환을 지원합니다:

- 길이 변환 (cm ↔ inch, km ↔ mile)
- 무게 변환 (kg ↔ lb)
- 온도 변환 (°C ↔ °F)
- 부피 변환 (L ↔ gal)

이 프로젝트를 통해 파이썬 패키지 구조, 모듈 분리, 설치 방식, README 작성법 등을 연습할 수 있습니다.

---

##  패키지 구조

```
mini_converter/
│
├── mini_converter
│   ├── __init__.py
│   ├── length.py
│   ├── weight.py
│   ├── temperature.py
│   ├── volume.py
│
├── examples
│   └── demo.py
│
├── tests
│   └── test_converter.py
│
├── README.md
├── setup.py
└── requirements.txt
```

---

##  설치 방법

터미널에서 mini_converter 폴더로 이동 후:

```
pip install -e .
```

---

##  사용 예시

`examples/demo.py` 실행:

```python
from mini_converter import *

print("=== Length ===")
print("10 cm →", cm_to_inch(10), "inch")
print("5 inch →", inch_to_cm(5), "cm")

print("\n=== Weight ===")
print("60 kg →", kg_to_lb(60), "lb")
print("150 lb →", lb_to_kg(150), "kg")

print("\n=== Temperature ===")
print("25°C →", c_to_f(25), "°F")
print("77°F →", f_to_c(77), "°C")

print("\n=== Volume ===")
print("1 L →", liter_to_gallon(1), "gal")
print("2 gal →", gallon_to_liter(2), "L")
```

---

##  실행 결과 

> 아래 이미지는 `examples/demo.py` 실행 화면입니다.




```

```

---

##  테스트 실행

(선택 사항)

```
pytest
```


