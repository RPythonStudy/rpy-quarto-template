"""
Python 간단 로깅 모듈

교육용 프로젝트를 위한 단순한 로깅 시스템입니다.
config/logger.yml의 LOG_LEVEL 설정을 사용합니다.
"""

import logging
import yaml
from pathlib import Path


def _load_config():
    """config/logger.yml에서 로그 레벨을 읽어옵니다."""
    config_path = Path("config/logger.yml")
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    return config["LOG_LEVEL"]


def _setup_logging():
    """로깅 설정을 초기화합니다."""
    log_level = _load_config()
    
    # 간단한 로깅 설정 (이름 정보는 메시지에 포함)
    logging.basicConfig(
        level=getattr(logging, log_level),
        format="[%(asctime)s] [%(levelname)s] %(message)s"
    )


def get_logger(name: str = "python-logger") -> logging.Logger:
    """
    간단한 로거 인스턴스를 반환합니다.
    
    Args:
        name: 로거 이름 (기본값: "python-logger")
    
    Returns:
        logging.Logger: 설정된 로거 인스턴스
    """
    if not logging.getLogger().handlers:
        _setup_logging()
    
    return logging.getLogger(name)