export async function requestAsync(method, url, headers, config={}) {
    config = {...{responseType: "", body: undefined}, ...config}
    const p = new Promise((resolve, reject) => {
        const req = new XMLHttpRequest();
        req.open(method, url);
        for(let key in headers)
            req.setRequestHeader(key, headers[key]);
        req.responseType = config.responseType;
        req.onload = () => {
            if(200 <= req.status && req.status <= 299) {
                if(req.getResponseHeader("Content-Type") == "application/json")
                    parseJSONResponse(req.response)
                        .then(resolve)
                        .catch(reject);
                else
                    resolve(req.response);
            } else {
                let bodyPromise;
                if(req.getResponseHeader("Content-Type") == "application/json")
                    bodyPromise = parseJSONResponse(req.response);
                else
                    bodyPromise = Promise.resolve(req.response);
                bodyPromise.then((body) => {
                        reject({status: req.status, message: req.statusText, body: body});
                    }).catch(reject);
            }
        }
        req.onerror = () => reject({status: req.status, message: req.statusText});
        req.onabort = () => reject({status: -1, message: "aborted"});
        req.send(config.body);
    });
    return p
}

export async function readFileToBlob(file) {
    return new Promise((resolve, reject) => {
        const fileReader = new FileReader();
        fileReader.onloadend = () => {
            resolve(fileReader.result);
        };
        fileReader.onerror = () => reject({status: fileReader.status, message: fileReader.statusText});
        fileReader.onabort = () => reject({status: -1, message: "aborted"});
        fileReader.readAsArrayBuffer(file);
    });
}

async function parseJSONResponse(response) {
    if(response instanceof Blob)
        return JSON.parse(await response.text());
    else
        return JSON.parse(response);
}
