import hmac
import hashlib
from loguru import logger
import base64

"""
hashlib---散列加密算法
包括 FIPS 安全哈希算法 SHA1、SHA224、SHA256、SHA384 和 SHA512（在 FIPS 180-2 中定义）以及 RSA 的 MD5 算法

消息认证码(MAC)--- 基于密钥的完整性检查
HMAC--基于秘钥的哈希算法
https://docs.python.org/3/library/hmac.html

digest 返回结果二进制
hexdigest以两倍于长度的字符串形式返回，仅包含十六进制数字
"""
data = "1234567890"
hmac_obj = hmac.new(key=b"0", msg=data.encode(), digestmod=hashlib.md5)
encrypt_hmac_md5 = hmac_obj.digest()
logger.info(f"hmac.md5加密结果: {hmac_obj.hexdigest()}")
base64_1 = base64.b64encode(data.encode()).decode()
logger.info(f"b64加密结果: {base64_1}")
logger.info(f"b64解密结果: {base64.b64decode(base64_1.encode()).decode()}")

encrypt_md5 = hashlib.md5(data.encode())
logger.info(f"hashlib.md5加密结果: {encrypt_md5.hexdigest()}")
