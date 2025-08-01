# example_script.py
# 교육용 예시 Python 스크립트

import sys
import os
import pandas as pd

# 프로젝트 루트를 sys.path에 추가
project_root = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(project_root)

# 로거와 사용자정의 함수 import
from logger.logger import get_logger
from src.python.example_src import say_hello, add_numbers, summarize_data

# 로거 설정
logger = get_logger(__name__)

def test_logger():
    """로거 기능 테스트"""
    print("\n" + "="*50)
    print("로거 테스트 시작")
    print("="*50)
    
    # 다양한 로그 레벨 테스트
    logger.debug("🔍 DEBUG: 디버그 메시지 - 상세한 진단 정보")
    logger.info("ℹ️  INFO: 정보 메시지 - 일반적인 실행 정보")
    logger.warning("⚠️  WARNING: 경고 메시지 - 주의가 필요한 상황")
    logger.error("❌ ERROR: 에러 메시지 - 오류 발생")
    
    print("\n로거 설정 정보:")
    print(f"- 로거 이름: {logger.name}")
    print(f"- 로거 레벨: {logger.level}")
    print(f"- 핸들러 수: {len(logger.handlers)}")
    
    if logger.handlers:
        for i, handler in enumerate(logger.handlers):
            print(f"- 핸들러 {i+1}: {type(handler).__name__}")
    
    print("="*50)
    print("로거 테스트 완료")
    print("="*50 + "\n")

def main():
    """메인 실행 함수"""
    # 로거 테스트 먼저 실행
    test_logger()
    
    logger.info("Python 스크립트 실행 시작")
    
    # 예시 1: 간단한 함수 사용
    logger.info("예시 1: say_hello 함수 테스트")
    message_result = say_hello("학습자")
    print(f"결과: {message_result}")
    
    # 예시 2: 계산 함수 사용
    logger.info("예시 2: add_numbers 함수 테스트")
    sum_result = add_numbers(10, 20)
    print(f"10 + 20 = {sum_result}")
    
    # 로거 레벨별 메시지 테스트
    logger.debug("add_numbers 함수 호출 후 디버그 정보")
    
    # 예시 3: 데이터프레임 생성 및 요약
    logger.info("예시 3: DataFrame 생성 및 분석 시작")
    try:
        sample_data = pd.DataFrame({
            '이름': ['홍길동', '김철수', '이영희'],
            '나이': [25, 30, 28],
            '점수': [85, 92, 88]
        })
        
        print("\n샘플 데이터:")
        print(sample_data)
        
        # 데이터 요약
        summary_result = summarize_data(sample_data)
        print("\n데이터 요약:")
        print(f"행 수: {summary_result['rows']}")
        print(f"열 수: {summary_result['cols']}")
        print(f"열 이름: {', '.join(summary_result['col_names'])}")
        print(f"결측값 수: {summary_result['na_count']}")
        
        logger.info("DataFrame 분석 완료")
        
    except Exception as e:
        logger.error(f"DataFrame 처리 중 오류 발생: {e}")
        print(f"오류: {e}")
    
    # 의도적 경고 메시지 테스트
    logger.warning("이것은 테스트용 경고 메시지입니다")
    
    logger.info("Python 스크립트 실행 완료")

if __name__ == "__main__":
    main()
