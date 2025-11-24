import logging
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

# 日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    """秒杀接口 - 带日志版本"""
    start_time = datetime.now()
    
    data = request.get_json() or {}
    product_id = data.get('product_id')
    user_id = data.get('user_id')
    
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
            "response_time": f"{(datetime.now() - start_time).total_seconds()}s"
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
