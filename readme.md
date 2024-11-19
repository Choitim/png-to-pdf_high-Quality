# PNG to PDF 변환기

이 프로젝트는 현재 폴더에 있는 모든 PNG 파일을 하나의 고품질 PDF 파일로 변환하는 간단한 파이썬 스크립트를 제공합니다. 이미지 처리를 위해 `Pillow` 라이브러리를 사용하며, 출력 PDF의 높은 해상도를 보장합니다.

## 주요 기능

- 현재 폴더 내의 모든 PNG 파일을 하나의 PDF 파일로 변환
- 출력 PDF의 고품질 해상도를 유지
- PNG 파일을 알파벳 순서로 정렬하여 병합

## 사전 요구사항

- Python 3.10 이상
- `Pillow` 라이브러리 (Python Imaging Library)

## 설치 방법

1. 이 저장소를 클론하거나 스크립트를 다운로드합니다.
2. `Pillow` 라이브러리를 설치합니다:
   ```bash
   pip install pillow