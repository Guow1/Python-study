const md5 = require("crypto-js/md5");
const hmac_sha256 = require("crypto-js/hmac-sha256");
const base64 = require("crypto-js/enc-base64");
const CryptoJS = require("crypto-js");
function get_signature(payload) {
    return CryptoJS.enc.Base64.stringify(md5(payload));
}
function get_signature_2(ts, data_sign) {
    var method = 'POST'
    var target_url = 'https://gdtv-api.gdtv.cn/api/search/v1/news'
    var payload = method+ "\n"+ target_url+ "\n"+ ts + "\n" + data_sign
    var hash = hmac_sha256(payload, 'dfkcY1c3sfuw0Cii9DWjOUO3iQy2hqlDxyvDXd1oVMxwYAJSgeB6phO8eW1dfuwX')
    return CryptoJS.enc.Base64.stringify(hash);
}