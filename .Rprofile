# .Rprofile for quarto-website-template
# --------------------------------------------

# 1. renv: 프로젝트별 패키지 환경 격리
if (file.exists("renv/activate.R")) {
  source("renv/activate.R")
}

# 2. config.yml에서 로깅 레벨 불러오기
config_file <- file.path("config", "config.yml")
if (file.exists(config_file) && requireNamespace("config", quietly = TRUE)) {
  # config 패키지를 attach하지 않고 네임스페이스를 통해 직접 사용
  cfg <- config::get(file = config_file)
  default_level <- cfg$log_level
} else {
  default_level <- "INFO"
  warning("config.yml이 없거나 config 패키지를 찾을 수 없습니다. 기본 로깅 레벨은 'INFO'로 설정됩니다.")
}

# LOG_LEVEL 환경변수로 오버라이드 가능
final_level <- Sys.getenv("LOG_LEVEL", default_level)

# 3. futile.logger 로깅 레벨 세팅 및 초기화 메시지
if (requireNamespace("futile.logger", quietly = TRUE)) {
  futile.logger::flog.threshold(get(final_level, asNamespace("futile.logger")))
  futile.logger::flog.info(sprintf("futile.logger: 로깅 레벨 %s로 초기화됨", final_level))
} else {
  warning("futile.logger 패키지가 설치되어 있지 않습니다. 로깅이 비활성화됩니다.")
}

# 4. 유틸리티 함수 로드
if (file.exists("R/utils.R")) {
  source("R/utils.R")
  cat("환경변수로 변경: set_log_env('DEBUG'), 일시적 변경: set_log_level('DEBUG'), 확인: get_log_level()\n")
}

