from flask import Flask, jsonify, request

app = Flask(__name__)

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
    """
    秒杀接口 - 基础版本
    后续可扩展：Redis限流 + MQ削峰 + 数据库扣库存
    """
    data = request.get_json() or {}
    product_id = data.get('product_id')
    user_id = data.get('user_id')
    
    # 基础响应
    return jsonify({
        "status": "success",
        "message": f"User {user_id} seckill product {product_id} successfully!",
        "data": {
            "product_id": product_id,
            "user_id": user_id,
            "order_id": f"ORDER-{user_id}-{product_id}-{hash(str(user_id+product_id))}"
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
