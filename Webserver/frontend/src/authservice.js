import config from "./config"
import { requestAsync } from "./util";

function getDefaultHeaders() {
    return {
        "Content-Type": "application/json"
    };
}

export async function createUser(email, username, password) {
	return await requestAsync(
		"POST",
		config.ENDPOINTS.AUTHENTICATION + "register/",
		getDefaultHeaders(),
		{body: JSON.stringify({email: email, username: username, password: password})}
	);
}

export async function deleteUser(refreshToken) {
	return await requestAsync(
		"POST",
		config.ENDPOINTS.AUTHENTICATION + "delete/",
		getDefaultHeaders(),
		{body: JSON.stringify({token: refreshToken})}
	);
}

export async function logIn(email, password) {
	return await requestAsync(
		"POST",
		config.ENDPOINTS.AUTHENTICATION + "login/",
		getDefaultHeaders(),
		{body: JSON.stringify({email: email, password: password})}
	);
}

export async function refreshToken(refreshToken) {
	return await requestAsync(
		"POST",
		config.ENDPOINTS.AUTHENTICATION + "token/refresh/",
		getDefaultHeaders(),
		{body: JSON.stringify({refresh: refreshToken})}
	);
}

export async function logOut(refreshToken) {
	return await requestAsync(
		"POST",
		config.ENDPOINTS.AUTHENTICATION + "logout/",
		getDefaultHeaders(),
		{body: JSON.stringify({token: refreshToken})}
	);
}
