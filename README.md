# speaker_diarization_for_data.py

수집된 데이터 변환 및 추출을 위한 파일


## 명령어

python3 speaker_diarization_for_data.py --data_in_dir soundDataset/hyeongi --data_out_dir soundDataset/concatData/ --concat_filename test1


config 설정

**data_in_dir** : m4a 확장자를 가진 통화데이터 파일들 디렉토리

**data_out_dir** : 통합 및 추출된 데이터가 저장될 디렉토리

**concat_file_name** : data_out_dir에 저장될 최종 파일의 이름, “(concat_file_name).wav” 로 파일이 저장됨







# speaker_diarization_for_conversation.py

여러명의 대화상황에서 화자분리를 위한 파일


## 명령어 

python3 spearker_diarization_for_conversation.py --data_in /home/hyeongikim/Desktop/음성인식/soundDataset/hyeongi/01045221780_20230330122123.wav


**data_in** : wav 확장자를 가진 회의파일

**data_out_dir** : 화자 분리된 파일들이 저장될 디렉토리




# project flow
**개요**

위에서 제시한 모델을 이용하여 개인화된 화자 분류 모델을 만들 예정입니다.

개인화된, 자신이 원하는 사람들의 목소리를 구분하기 위해서는 그 사람의 목소리가 많이 필요한데 저희는 그 문제를 해결하기 위해 또다시 딥러닝을 이용하였습니다.

**모델 진행상황**

저희는 pytorch 프레임워크를 이용한 pyannote-audio 오픈소스 라이브러리를 사용하여 원하는 사람의 목소리를 추출하여 수집하는 것을 목표로 하였습니다.

그래서 진행된 사항에 대해 말씀드리겠습니다.

저희는 먼저 휴대폰에 있는 통화녹음 5개를 가져와서 각각 wav 확장자로 바꾸어 통일 해주었습니다.

![스크린샷 2023-05-08 오후 1.21.51.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c233e472-7799-4ff3-8c3c-e88eb758aa71/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-08_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.21.51.png)

그 후 모든 wav파일들을 통합하여 하나의 긴 음성파일을 만들었고 여기에는 총 6명의 음성이 들어있습니다.

![스크린샷 2023-05-08 오후 1.33.34.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/63587c30-248b-4a8c-9545-052bc4313b97/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-08_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.33.34.png)

이후 pyannote audio 라이브러리의 사전 학습된 모델을 이용하여 speaker diarization을 실시하였고 총 6명의 음성으로 구분된 결과가 나왔습니다. pyannote 오디오 모델은 lstm 시계열 딥러닝 모델을 기반으로 이루어져 있습니다. pyannote 오디오 모델을 사용하면 통화 녹음에서 목소리의 feature에 따라 음성을 추출할 수 있습니다. 추출된 해당 음성을 비슷한 feature 끼리 묶는 방식으로 발화자들을 구분하여 보여주게 됩니다.  

![스크린샷 2023-05-08 오후 4.40.19.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/25d573a6-f9ae-4b3e-86e8-539aa2b09912/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-08_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.40.19.png)

그래서 하나의 음성파일에서 이렇게 구분되어진 스피커들의 feature 정보를 이용하여 음성파일에서 같은 스피커로 분류된 구간을 그 스피커의 소리만 따로 추출하여 다시 하나의 음성파일들로 만들어 봤습니다.

![스크린샷 2023-05-08 오후 4.43.16.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/79bdf460-e647-4052-ac4f-9b00b0d22678/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-08_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.43.16.png)

그 결과 목표했던 사람의 결합되어 추출된 음성파일은 귀로 들어도 한 사람의 소리가 들렸습니다.

그러나 아직 잡음, 상대방의 짧은 대답이 섞여있어서 완벽하지 않기때문에 추출하는 방식 또는 pyannote audio pipeline 모델을 추가 학습 시키는 방식을 기말때까지 준비하여 성능을 높여야 할 것 같습니다.


contact : kimhun0505@naver.com
