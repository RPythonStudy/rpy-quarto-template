# example_script.R
# 교육용 예시 R 스크립트

# 로거 로드
source(here::here("logger", "logger.R"))
init_logger()

# 사용자정의 함수 로드
source(here::here("src", "R", "example.R"))

log_info("R 스크립트 실행 시작")

# 예시 1: 간단한 함수 사용
message_result <- say_hello("학습자")
cat("결과:", message_result, "\n")

# 예시 2: 계산 함수 사용
sum_result <- add_numbers(10, 20)
cat("10 + 20 =", sum_result, "\n")

# 예시 3: 데이터프레임 생성 및 요약
sample_data <- data.frame(
  이름 = c("홍길동", "김철수", "이영희"),
  나이 = c(25, 30, 28),
  점수 = c(85, 92, 88)
)

cat("샘플 데이터:\n")
print(sample_data)

# 데이터 요약
summary_result <- summarize_data(sample_data)
cat("\n데이터 요약:\n")
cat("행 수:", summary_result$rows, "\n")
cat("열 수:", summary_result$cols, "\n")
cat("열 이름:", paste(summary_result$col_names, collapse = ", "), "\n")
cat("결측값 수:", summary_result$na_count, "\n")

log_info("R 스크립트 실행 완료")
