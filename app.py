import logging
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

# 日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 限流：每个用户最多3次请求（核心！）
request_count = {}

@app.route('/')
def index():
    return jsonify({
        "message": "Flash Sale System is running!",
        "endpoints": {
            "health": "/health",
            "seckill": "/seckill"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "code": 200})

@app.route('/seckill', methods=['POST'])
def seckill():
    """秒杀接口 - 带限流和日志版本"""
    start_time = datetime.now()
    
    data = request.get_json() or {}
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    
    # 【核心限流逻辑】检查用户是否已存在
    if user_id in request_count:
        # 检查是否超过3次限制
        if request_count[user_id] >= 3:
            logger.warning(f"[BLOCKED] User:{user_id} exceeded limit")
            return jsonify({
                "status": "error",
                "message": "Request limit exceeded. Try later."
            }), 429  # HTTP 429: Too Many Requests
        request_count[user_id] += 1
    else:
        request_count[user_id] = 1
    
    # 记录请求日志
    logger.info(f"[SECKILL] User:{user_id} Product:{product_id} Time:{start_time}")
    
    # 模拟处理时间
    import time
    time.sleep(0.05)  # 模拟50ms处理
    
    # 记录成功日志
    logger.info(f"[SUCCESS] Order created for user:{user_id}")
    
    return jsonify({
        "status": "success",
        "message": f"User {user_id} seckill product {product_id} successfully!",
        "data": {
            "product_id": product_id,
            "user_id": user_id,
            "order_id": f"ORDER-{user_id}-{product_id}-{int(time.time())}",
            "request_count": request_count[user_id],  # 显示这是第几次请求
            "response_time": f"{(datetime.now() - start_time).total_seconds()}s"
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
