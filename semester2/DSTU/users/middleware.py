# middleware.py
import logging
import time

logger = logging.getLogger('users')


class RequestLoggingMiddleware:
    """Middleware для логирования всех запросов"""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Время начала запроса
        start_time = time.time()
        
        # Логируем входящий запрос
        logger.debug(f"Request: {request.method} {request.path} - User: {request.user.username if request.user.is_authenticated else 'Anonymous'}")
        
        response = self.get_response(request)
        
        # Время выполнения
        duration = time.time() - start_time
        
        # Логируем ответ
        logger.debug(f"Response: {response.status_code} - Duration: {duration:.2f}s")
        
        return response