# Quarto Website Template

R과 Quarto를 사용한 웹사이트 템플릿입니다.

## 프로젝트 구조

### R 환경 관리
- **renv**: 프로젝트별 패키지 환경 격리
- **config.yml**: 로깅 레벨 설정 (`log_level: "INFO"`)
- **futile.logger**: 로깅 시스템

### Quarto 설정
- **프로젝트 타입**: website
- **테마**: cosmo + brand
- **CSS**: `styles.css`

## 개발 가이드

### 로깅 시스템
```r
# 기본값: config/config.yml의 log_level
# 환경변수 오버라이드
Sys.setenv(LOG_LEVEL = "DEBUG")  # 일시적 변경

# 로깅 사용
futile.logger::flog.debug("디버그 메시지")
futile.logger::flog.info("정보 메시지")
futile.logger::flog.warn("경고 메시지")
futile.logger::flog.error("에러 메시지")
```

### 패키지 관리
```r
renv::install("패키지명")  # 패키지 설치
renv::snapshot()          # 변경사항 저장
renv::restore()           # 환경 복원
```

### 빌드 및 실행
```r
quarto::quarto_preview()  # 미리보기
```

```bash
quarto render  # 빌드
```

## 주요 파일
- `.Rprofile`: R 환경 자동 설정
- `_quarto.yml`: Quarto 프로젝트 설정
- `config/config.yml`: 로깅 레벨 설정
- `renv.lock`: 패키지 의존성

## 코딩 스타일
- **R**: snake_case, futile.logger 사용
- **Quarto**: 한국어 콘텐츠 지원