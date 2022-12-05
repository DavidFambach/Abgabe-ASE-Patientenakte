export async function requestAsync(method, url, headers) {
    const p = new Promise((resolve, reject) => {
        const req = new XMLHttpRequest();
        req.open(method, url);
        for(let key in headers)
            req.setRequestHeader(key, headers[key]);
        req.onload = () => {
            if(200 <= req.status && req.status <= 299) {
                if(req.getResponseHeader("Content-Type") == "application/json")
                    resolve(JSON.parse(req.response));
                else
                    resolve(req.response);
            } else {
                let body;
                if(req.getResponseHeader("Content-Type") == "application/json")
                    body = JSON.parse(req.response);
                else
                    body = req.response;
                reject({status: req.status, message: req.statusText, body: body});
            }
        }
        req.onerror = () => reject({status: req.status, message: req.statusText});
        req.onabort = () => reject({status: -1, message: "aborted"});
        req.send();
    });
    return p
}
