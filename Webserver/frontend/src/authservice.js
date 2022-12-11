import config from "./config"
import { requestAsync } from "./util";

const OAUTH_SCHEME = "https";
const OAUTH_AUTHORITY = "accounts.google.com";
const OAUTH_PATH = "/o/oauth2/v2/auth/oauthchooseaccount";
const OAUTH_QUERY_STATIC = Object.freeze({
	access_type: "offline",
	flowName: "GeneralOAuthFlow",
	o2v: "2",
	prompt: "consent",
	response_type: "code",
	scope: "https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile",
	service: "lso"
});
const OATUH_QUERY_KEY_CLIENT_ID = "client_id";
const OATUH_QUERY_KEY_REDIRECT_URI = "redirect_uri";

function getDefaultHeaders() {
    return {
        "Content-Type": "application/json"
    };
}

function getGoogleOAuthURL(clientID) {
	const url = new URL("https://invalid");
	url.protocol = OAUTH_SCHEME + ":";
	url.host = OAUTH_AUTHORITY;
	url.pathname = OAUTH_PATH;
	for(let key of Object.keys(OAUTH_QUERY_STATIC))
		url.searchParams.append(key, OAUTH_QUERY_STATIC[key]);
	url.searchParams.append(OATUH_QUERY_KEY_CLIENT_ID, clientID);
	url.searchParams.append(OATUH_QUERY_KEY_REDIRECT_URI, getGoogleOAuthRedirectURI());
	return url;
}

async function getGoogleOAuthClientID() {
	return await requestAsync(
		"GET",
		config.ENDPOINTS.AUTHENTICATION + "google/client-id",
		getDefaultHeaders()
	);
}

function getGoogleOAuthRedirectURI() {
	return new URL(config.ENDPOINTS.OAUTH_REDIRECT, window.location.origin).toString();
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

export async function logInWithGoogle() {
	const oAuthClientID = await getGoogleOAuthClientID();
	const oAuthURL = getGoogleOAuthURL(oAuthClientID);
	window.location.replace(oAuthURL.toString());
}

export async function finalizeLogInWithGoogle(authCode) {
	return await requestAsync(
		"POST",
		config.ENDPOINTS.AUTHENTICATION + "google/",
		getDefaultHeaders(),
		{body: JSON.stringify({code: authCode, redirect_uri: getGoogleOAuthRedirectURI()})}
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

export async function changePassword(refreshToken, oldPassword, newPassword) {
	return await requestAsync(
		"POST",
		config.ENDPOINTS.AUTHENTICATION + "password-change/",
		getDefaultHeaders(),
		{body: JSON.stringify({token: refreshToken, old_password: oldPassword, password: newPassword})}
	);
}
