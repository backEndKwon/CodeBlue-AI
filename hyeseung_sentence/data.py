# 증상 데이터와 응급 정도 레이블
# 1 : "생명이 위험한 상태. 30-2시간이내로 응급조치 필요", 
# 2 :  "2-10시간 이내로 조치 필요", 
# 3 : "생명에는 지장이 없으나, 빠른 조치 필요", 
# 4 : "의사의 소견이 필요함", 
# 5 : "휴식을 취하면 괜찮아짐" 
data = [
    ("사백신 맞은 후 발열이 있고 경련이 있다.", 5),
    ("발열이 있고 경련이 있다.", 2),
    ("눈에 통증이 있어서 얼음찜질을 장시간 함. 두통이 오고 머리 왼쪽 윗부분에 마비증상이 오기 시작하였고 음식을 씹지못할 정도로 안면신경마비가 왔음", 1),
    ("대상포진. 피부에 통증과 발진만 있는 상태", 4),
    ("대상포진. 피부 발진이 수포를 형성하고, 통증이 심각한 경우. 열, 오한 발생", 2),
    ("편도수술 후 기침을 많이 함. 감기 걸린 것 같다. 어제 밤에 소변이 붉은 색으로 나옴.  예전에 감기걸리거나 운동을 했을 때 혈뇨가 나온적은 없음.", 4),
    ("중이염과 항생제 복용, 설사가 10번/일.",3),
    ("3일전부터 발열 금일부터 발진. 몸통 주위부터 시작. 입안에 백태. 해열제를 복용하고 있는 중. 비대칭적. 예전에는 열꽃 같은 증상은 없었다", 3),
    ("오른쪽 귀 뒷부분에 몽우리 손가락 한마디 정도가 만져지고 점점 커짐. 만지면 아픔. 볼부위가 많이 부었다. 발열 기침 가래 피부병변. 최근에 감기 걸린 증상이 없었다.", 3),
    ("계란 알레르기가 있는데 인플루엔자 예방접종을 맞음.",4),
    ("알레르기. 경미한 피부 발진, 가려움", 5),
    ("알레르기. 중등도 피부 발진, 구역질, 복통.", 4),
    ("알레르기. 심한 호흡곤란, 구역질, 구취, 혈압저하",3),
    ("알레르기. 심한 호흡곤란, 발진, 구역질, 혈압저하, 의식 잃음", 2),
    ("알레르기. 심한 호흡곤란, 발진, 구역질, 혈압저하, 의식 상실, 부종, 급성 충수염", 1),
    ("경미한 발진과 경도의 발열", 5),
    ("중등도 발진과 발열, 구토 또는 설사",4),
    ("심한 발진과 고열, 음식 섭취 불가능, 호흡곤란.", 3),
    ("심한 발진과 고열, 음식 섭취 불가능, 호흡곤란, 의식 잃음.",2),
    ("심한 발진과 고열, 음식 섭취 불가능, 호흡곤란, 의식 상실, 부종", 1),
    ("독감예방주사 후 발열,오한.", 5),
    ("독감예방주사 후 오심,구토",4),
    ("간이식받고 면역억제제 복용 중 수두 걸린 사람과 접촉", 3),
    ("갑상선기능저하증약과 철분제제를 함께 복용. 운동 시 호흡곤란, 심계항진 있음",4),
    ("운동 시 호흡곤란, 심계항진 있음", 1),
    ("반복적인 저혈당 증상",4),
    ("입안 점막 감염, 통증, 부움", 4),
]