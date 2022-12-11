import config from "@/config";
import { getUserID, getCurrentAccessToken } from "@/session";
import { requestAsync } from "@/util";

async function getDefaultHeaders() {
    return {
        "Authorization": "Bearer " + await getCurrentAccessToken()
    };
}

export async function getUserInfo() {
    return await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "userinfo/" + getUserID(),
        await getDefaultHeaders()
    );
}

export async function downloadFile(fileID, proposedName="Datei") {
    const response = await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "file/" + fileID + "?user=" + getUserID(),
        await getDefaultHeaders(),
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
        config.ENDPOINTS.FILE + "file/?user=" + getUserID() + "&name=" + encodeURIComponent(name) + "&parentDirectory=" + parentDirectoryID,
        await getDefaultHeaders(),
        {body: file}
    );
}

export async function renameFile(fileID, newName) {
    return await requestAsync(
        "PUT",
        config.ENDPOINTS.FILE + "file/" + fileID + "?user=" + getUserID() + "&name=" + encodeURIComponent(newName),
        await getDefaultHeaders()
    );
}

export async function moveFile(fileID, newParentDirectoryID) {
    return await requestAsync(
        "PUT",
        config.ENDPOINTS.FILE + "file/" + fileID + "?user=" + getUserID() + "&parentDirectory=" + newParentDirectoryID,
		await getDefaultHeaders()
    );
}

export async function deleteFile(fileID) {
    return await requestAsync(
        "DELETE",
        config.ENDPOINTS.FILE + "file/" + fileID + "?user=" + getUserID(),
        await getDefaultHeaders()
    );
}

export async function getDirectory(directoryID) {
    return await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "dir/" + directoryID + "?user=" + getUserID(),
        await getDefaultHeaders()
    );
}

export async function createDirectory(parentDirectoryID, name) {
    return await requestAsync(
        "POST",
        config.ENDPOINTS.FILE + "dir/?user=" + getUserID() + "&parentDirectory=" + parentDirectoryID + "&name=" + encodeURIComponent(name),
        await getDefaultHeaders()
    );
}

export async function renameDirectory(directoryID, newName) {
    return await requestAsync(
        "PUT",
        config.ENDPOINTS.FILE + "dir/" + directoryID + "?user=" + getUserID() + "&name=" + encodeURIComponent(newName),
        await getDefaultHeaders()
    );
}

export async function moveDirectory(directoryID, newParentDirectoryID) {
    return await requestAsync(
        "PUT",
        config.ENDPOINTS.FILE + "dir/" + directoryID + "?user=" + getUserID() + "&parentDirectory=" + newParentDirectoryID,
        await getDefaultHeaders()
    );
}

export async function deleteDirectory(directoryID, cascade) {
    return await requestAsync(
        "DELETE",
        config.ENDPOINTS.FILE + "dir/" + directoryID + "?user=" + getUserID() + "&directoryID=" + directoryID + (cascade ? "&cascade" : ""),
        await getDefaultHeaders()
    );
}

export async function getShare(shareID) {
    return await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "share/" + shareID + "?user=" + getUserID(),
        await getDefaultHeaders()
    );
}

export async function createShare(targetType, targetID, subjectID, writePermission) {
    return await requestAsync(
        "POST",
        config.ENDPOINTS.FILE + "share/?user=" + getUserID() + "&targetType=" + encodeURIComponent(targetType) + "&targetID=" + targetID + "&subject=" + subjectID + (writePermission ? "&canWrite" : ""),
        await getDefaultHeaders()
    );
}

export async function deleteShare(shareID) {
    return await requestAsync(
        "DELETE",
        config.ENDPOINTS.FILE + "share/" + shareID + "?user=" + getUserID(),
        await getDefaultHeaders()
    );
}

export async function getContactName(contactID) {
    return await requestAsync(
        "GET",
        config.ENDPOINTS.FILE + "contact/" + contactID + "?user=" + getUserID(),
        await getDefaultHeaders()
    );
}

export async function addContact(contactID) {
    return await requestAsync(
        "POST",
        config.ENDPOINTS.FILE + "contact/" + contactID + "?user=" + getUserID(),
        await getDefaultHeaders()
    );
}

export async function removeContact(contactID) {
    return await requestAsync(
        "DELETE",
        config.ENDPOINTS.FILE + "contact/" + contactID + "?user=" + getUserID(),
        await getDefaultHeaders()
    );
}
