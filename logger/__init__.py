# logger/__init__.py
"""
R & Python 학습용 간단한 로깅 시스템

Python에서 간단한 로깅을 위한 패키지입니다.
R의 futile.logger와 비슷한 인터페이스를 제공합니다.
"""

from .logger import get_logger

__all__ = ['get_logger']
__version__ = '0.1.0'