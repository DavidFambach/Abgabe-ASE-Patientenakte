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
    );
}

export async function downloadFile(fileID, proposedName="Datei") {
    const response = await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "file/" + fileID + "?user=" + USER_ID,
        getDefaultHeaders(),
        {responseType: "blob"}
    );
    const url = window.URL.createObjectURL(response);
    const link = document.createElement("a");
    link.href = url;
    link.download = proposedName;
    link.click();
    window.URL.revokeObjectURL(url);
}

export async function uploadFile(file, name, parentDirectoryID) {
    return await requestAsync(
        "POST",
        config.ENDPOINTS.FILE + "file/?user=" + USER_ID + "&name=" + encodeURIComponent(name) + "&parentDirectory=" + parentDirectoryID,
        getDefaultHeaders(),
        {body: file}
    );
}

export async function renameFile(fileID, newName) {
    return await requestAsync(
        "PUT",
        config.ENDPOINTS.FILE + "file/" + fileID + "?user=" + USER_ID + "&name=" + encodeURIComponent(newName),
        getDefaultHeaders()
    );
}

export async function moveFile(fileID, newParentDirectoryID) {
    return await requestAsync(
        "PUT",
        config.ENDPOINTS.FILE + "file/" + fileID + "?user=" + USER_ID + "&parentDirectory=" + newParentDirectoryID,
        getDefaultHeaders()
    );
}

export async function deleteFile(fileID) {
    return await requestAsync(
        "DELETE",
        config.ENDPOINTS.FILE + "file/" + fileID + "?user=" + USER_ID,
        getDefaultHeaders()
    );
}

export async function getDirectory(directoryID) {
    return await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "dir/" + directoryID + "?user=" + USER_ID,
        getDefaultHeaders()
    );
}

export async function createDirectory(parentDirectoryID, name) {
    return await requestAsync(
        "POST",
        config.ENDPOINTS.FILE + "dir/?user=" + USER_ID + "&parentDirectory=" + parentDirectoryID + "&name=" + encodeURIComponent(name),
        getDefaultHeaders()
    );
}

export async function renameDirectory(directoryID, newName) {
    return await requestAsync(
        "PUT",
        config.ENDPOINTS.FILE + "dir/" + directoryID + "?user=" + USER_ID + "&name=" + encodeURIComponent(newName),
        getDefaultHeaders()
    );
}

export async function moveDirectory(directoryID, newParentDirectoryID) {
    return await requestAsync(
        "PUT",
        config.ENDPOINTS.FILE + "dir/" + directoryID + "?user=" + USER_ID + "&parentDirectory=" + newParentDirectoryID,
        getDefaultHeaders()
    );
}

export async function deleteDirectory(directoryID, cascade) {
    return await requestAsync(
        "DELETE",
        config.ENDPOINTS.FILE + "dir/" + directoryID + "?user=" + USER_ID + "&directoryID=" + directoryID + (cascade ? "&cascade" : ""),
        getDefaultHeaders()
    );
}

export async function getShare(shareID) {
    return await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "share/" + shareID + "?user=" + USER_ID,
        getDefaultHeaders()
    );
}

export async function createShare(targetType, targetID, subjectID, writePermission) {
    return await requestAsync(
        "POST",
        config.ENDPOINTS.FILE + "share/?user=" + USER_ID + "&targetType=" + encodeURIComponent(targetType) + "&targetID=" + targetID + "&subject=" + subjectID + (writePermission ? "&canWrite" : ""),
        getDefaultHeaders()
    );
}

export async function deleteShare(shareID) {
    return await requestAsync(
        "DELETE",
        config.ENDPOINTS.FILE + "share/" + shareID + "?user=" + USER_ID,
        getDefaultHeaders()
    );
}

export async function getContactName(contactID) {
    return await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "contact/" + contactID + "?user=" + USER_ID,
        getDefaultHeaders()
    );
}

export async function addContact(contactID) {
    return await requestAsync(
        "POST",
        config.ENDPOINTS.FILE + "contact/" + contactID + "?user=" + USER_ID,
        getDefaultHeaders()
    );
}

export async function removeContact(contactID) {
    return await requestAsync(
        "DELETE",
        config.ENDPOINTS.FILE + "contact/" + contactID + "?user=" + USER_ID,
        getDefaultHeaders()
    );
}
