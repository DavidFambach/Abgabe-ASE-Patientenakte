import * as authservice from "@/authservice";

const JWT_USER_ID_KEY = "user_id";

const SESSION_STORAGE_ID_KEY = "session-user-id";
const SESSION_STORAGE_ACCESS_TOKEN_KEY = "session-user-token";
const SESSION_STORAGE_REFRESH_TOKEN_KEY = "session-user-token-refresh";

const SESSION_STORAGE_EMAIL_KEY = "session-user-email";

let USER_ID = null;
let ACCESS_TOKEN = null;
let REFRESH_TOKEN = null;

function getTokenPayload(token) {
	const b64 = token.replace(/^[^.]*\.([^.]*)\.[^.]*/, "$1");
	if(b64 === token)
		return false;
	return JSON.parse(atob(b64));
}

function isTokenValid(token, durationMillis=30000) {
	try {
		const payload = getTokenPayload(token);
		return (Date.now() + durationMillis) / 1000 < payload.exp;
	} catch {
		return false;
	}
}

export function importToken(accessToken, refreshToken) {
	const payload = getTokenPayload(refreshToken);
	const userID = Number(payload[JWT_USER_ID_KEY]);
	if(isNaN(userID)) {
		console.log("Refresh token did not contain \"" + JWT_USER_ID_KEY + "\" key");
		return false;
	}
	return setOwnToken(userID, accessToken, refreshToken);
}

export function setOwnToken(userID, accessToken, refreshToken) {
	if(userID != null && accessToken != null && refreshToken != null) {
        USER_ID = userID;
		ACCESS_TOKEN = accessToken;
		REFRESH_TOKEN = refreshToken;
        return true;
    }
    return false;
}

export function storeToken() {
    if(USER_ID != null && ACCESS_TOKEN != null && REFRESH_TOKEN) {
        window.sessionStorage.setItem(SESSION_STORAGE_ID_KEY, USER_ID);
        window.sessionStorage.setItem(SESSION_STORAGE_ACCESS_TOKEN_KEY, ACCESS_TOKEN);
        window.sessionStorage.setItem(SESSION_STORAGE_REFRESH_TOKEN_KEY, REFRESH_TOKEN);
        return true;
    }
    return false;
}

export function isLoggedIn(durationMillis=30000) {
	return USER_ID != null && isTokenValid(REFRESH_TOKEN, durationMillis) || restoreToken();
}

export function restoreToken() {
    return setOwnToken(window.sessionStorage.getItem(SESSION_STORAGE_ID_KEY),
		window.sessionStorage.getItem(SESSION_STORAGE_ACCESS_TOKEN_KEY),
		window.sessionStorage.getItem(SESSION_STORAGE_REFRESH_TOKEN_KEY))
}

export function clearToken() {
    window.sessionStorage.removeItem(SESSION_STORAGE_ID_KEY);
    window.sessionStorage.removeItem(SESSION_STORAGE_ACCESS_TOKEN_KEY);
    window.sessionStorage.removeItem(SESSION_STORAGE_REFRESH_TOKEN_KEY);
}

export function getUserID() {
	if(USER_ID == null)
		throw {status: 401, message: "No access user ID available"};
	return USER_ID;
}

export function getRefreshToken(durationMillis=30000) {
	if(USER_ID == null || !isTokenValid(REFRESH_TOKEN, durationMillis))
		throw {status: 401, message: "No refresh token available"};
	return REFRESH_TOKEN;
}

export function setExtraUserEMail(email) {
	if(email == null)
		sessionStorage.removeItem(SESSION_STORAGE_EMAIL_KEY);
	else
		sessionStorage.setItem(SESSION_STORAGE_EMAIL_KEY, email);
}

export function getExtraUserEMail() {
	return sessionStorage.getItem(SESSION_STORAGE_EMAIL_KEY);
}

export async function getCurrentAccessToken(durationMillis=30000) {
	if(USER_ID == null)
		throw {status: 401, message: "No access token available"};
	if(isTokenValid(ACCESS_TOKEN, durationMillis))
		return ACCESS_TOKEN;
	const refreshResponse = await authservice.refreshToken(REFRESH_TOKEN);
	if(refreshResponse.access == null)
		throw {status: 400, message: "Got no access token when refreshing token"};
	ACCESS_TOKEN = refreshResponse.access;
	storeToken();
	return ACCESS_TOKEN;
}

export async function logOut() {
	if(USER_ID == null)
		return null;
	await authservice.logOut(REFRESH_TOKEN);
	clearToken();
}
