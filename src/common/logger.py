# rpy-quarto-template/src/common/logger.py
import os
import socket
import logging
import logging.config
from pathlib import Path
from datetime import datetime, timezone

import yaml
from dotenv import load_dotenv

# .env 로드 (ENV 우선)
load_dotenv(override=True)

PROJECT_NAME = os.getenv("PROJECT_NAME", "")

VALID_LEVELS = {"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"}


def _get_log_level() -> str:
    level = os.getenv("LOG_LEVEL", "INFO").upper()
    return level if level in VALID_LEVELS else "INFO"


def _expand_env_placeholders(value: str) -> str:
    """
    ${VAR} / $VAR 형태의 환경변수를 실제 값으로 치환.
    """
    if not isinstance(value, str):
        return value
    expanded = os.path.expandvars(value)
    return expanded


def _require_parent_exists_and_writable(path: Path, handler_name: str) -> None:
    """
    법/컴플라이언스 로그 누락 방지를 위해:
    - 디렉토리가 없거나 쓰기 불가면 즉시 예외 발생(자동 생성하지 않음).
    """
    parent = path.parent
    if not parent.exists():
        raise FileNotFoundError(
            f"[{handler_name}] 로그 디렉토리가 존재하지 않습니다: {parent}"
        )
    if not os.access(parent, os.W_OK):
        raise PermissionError(
            f"[{handler_name}] 로그 디렉토리에 쓰기 권한이 없습니다: {parent}"
        )


def _load_logging_config() -> dict:

    # src/common/logger.py 기준 프로젝트 루트의 config/logging.yml 참조
    yaml_path = Path(__file__).parent.parent.parent / "config" / "logging.yml"
    if not yaml_path.exists():
        raise FileNotFoundError(f"logging.yml 파일이 필요합니다: {yaml_path}")

    with open(yaml_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # 1) LOG_LEVEL 환경변수로 루트/서브 로거 레벨 오버라이드
    level = _get_log_level()
    config.setdefault("root", {})["level"] = level
    for _, logger_cfg in config.get("loggers", {}).items():
        logger_cfg["level"] = level

    # 2) 파일 핸들러의 filename에 포함된 ${ENV} 치환 + 경로 유효성 필수 검사
    for handler_name, handler_cfg in config.get("handlers", {}).items():
        if handler_cfg.get("class") == "logging.FileHandler":
            raw_filename = handler_cfg.get("filename", "")
            if not raw_filename:
                raise ValueError(f"[{handler_name}] filename이 지정되어 있지 않습니다.")

            expanded = _expand_env_placeholders(raw_filename)
            # 치환 실패 감지(그대로 남아있다면 ENV 누락 가능성)
            if expanded == raw_filename and ("${" in raw_filename or "$" in raw_filename):
                raise ValueError(
                    f"[{handler_name}] 환경변수 치환 실패: {raw_filename} "
                    f"(해당 환경변수가 .env에 설정되어 있는지 확인하세요)"
                )

            file_path = Path(expanded)
            _require_parent_exists_and_writable(file_path, handler_name)
            handler_cfg["filename"] = str(file_path)

    return config


def setup_logging() -> None:
    config = _load_logging_config()
    logging.config.dictConfig(config)


def get_logger(name: str = PROJECT_NAME) -> logging.Logger:
    root_logger = logging.getLogger()
    if not root_logger.hasHandlers():
        setup_logging()
    return logging.getLogger(name or None)


def audit_log(action: str, detail: dict = None, compliance: str = "개인정보보호법 제28조"):
    audit_logger = get_logger("audit")
    user = os.getenv("USER") or "unknown"
    log = {
        "action": action,
        "user": user,
        "process_id": os.getpid(),
        "server_id": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "compliance_check": compliance,
    }
    if detail:
        log.update(detail)
    audit_logger.info(log)


# convenience wrappers
def log_debug(msg: str) -> None: get_logger().debug(msg)
def log_info(msg: str) -> None: get_logger().info(msg)
def log_warn(msg: str) -> None: get_logger().warning(msg)
def log_error(msg: str) -> None: get_logger().error(msg)
def log_critical(msg: str) -> None: get_logger().critical(msg)
