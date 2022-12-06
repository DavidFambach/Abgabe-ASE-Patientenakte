import config from "./config"
import { requestAsync } from "./util";

let USER_ID = null;
let TOKEN = null;

function getDefaultHeaders() {
    return {
        "Authorization": "Bearer " + TOKEN
    };
}

export function setOwnUserID(userID) {
    USER_ID = userID;
}

export function setOwnToken(token) {
    TOKEN = token;
}

export async function getUserInfo() {
    return await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "userinfo/" + USER_ID,
        getDefaultHeaders()
    )
}

export async function getDirectory(directoryID) {
    return await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "dir/" + directoryID + "?user=" + USER_ID,
        getDefaultHeaders()
    )
}

export async function getShare(shareID) {
    return await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "share/" + shareID + "?user=" + USER_ID,
        getDefaultHeaders()
    )
}
