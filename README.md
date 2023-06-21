## speaker_diarization_for_data.py

수집된 데이터 변환 및 추출을 위한 파일


# 명령어

python3 speaker_diarization_for_data.py --data_in_dir soundDataset/hyeongi --data_out_dir soundDataset/concatData/ --concat_filename test1


config 설정

**data_in_dir** : m4a 확장자를 가진 통화데이터 파일들 디렉토리

**data_out_dir** : 통합 및 추출된 데이터가 저장될 디렉토리

**concat_file_name** : data_out_dir에 저장될 최종 파일의 이름, “(concat_file_name).wav” 로 파일이 저장됨







## speaker_diarization_for_conversation.py

여러명의 대화상황에서 화자분리를 위한 파일


# 명령어 

python3 spearker_diarization_for_conversation.py --data_in /home/hyeongikim/Desktop/음성인식/soundDataset/hyeongi/01045221780_20230330122123.wav


**data_in** : wav 확장자를 가진 회의파일

**data_out_dir** : 화자 분리된 파일들이 저장될 디렉토리
