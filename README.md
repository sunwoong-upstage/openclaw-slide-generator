# openclaw-slide-generator

Harness Engineering 발표자료와 OpenClaw `slide-creator` 스킬을 담은 저장소입니다.

이 저장소는 단순히 슬라이드를 생성하는 예제가 아니라, **짧은 브리프를 발표 가능한 deck으로 바꾸는 skill 설계 방식**을 함께 보여줍니다.

## Live

- GitHub Pages 메인: `https://sunwoong-upstage.github.io/openclaw-slide-generator/`
- 압축 슬라이드 deck: `https://sunwoong-upstage.github.io/openclaw-slide-generator/slides/`

## 포함 내용

- `slides/` — 10분 발표용 Harness Engineering HTML deck
- `slides/speaker-notes.txt` — 발표용 notes
- `skill/slide-creator/` — deck planning, template selection, quality check가 포함된 OpenClaw skill

## slide-creator skill 특징

- 발표 맥락 수집
- deck type 판단
- story arc planning
- slide-type selection guide
- HTML reveal.js 출력
- speaker notes 생성
- north-star 기반 반복 개선
- readability quality check

## 저장소 구조

- `index.html` — GitHub Pages 진입 페이지
- `slides/` — 발표 deck
- `skill/slide-creator/` — 재사용 가능한 skill source

## 참고 방향

이 skill은 다음과 같은 좋은 패턴들을 참고해 개선되었습니다.

- deck generation 전에 story를 먼저 설계하기
- slide type을 명시적으로 고르기
- 결과물을 quality checklist로 검수하기
- 짧은 발표에서 장수보다 전달력을 우선하기
