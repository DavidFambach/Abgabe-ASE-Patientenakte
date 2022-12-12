import Vue from "vue";
import VueRouter from "vue-router";
import * as session from "@/session";

Vue.use(VueRouter);

const routes = [
	{
		path: "/return/google",
		name: "return-google",
		redirect: to => {
			session.setExtraGoogleOAuthInfo(to.query.code);
			return {name: "login"};
		}
	},
	{
		path: "/verify",
		name: "verify",
		redirect: () => ({name: "login"})
	},
	{
		path: "/",
		name: "main",
		component: () => import("@/views/MainView.vue")
	},
	{
		path: "/login",
		name: "login",
		component: () => import("@/views/LoginView.vue")
	}
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes
});

export default router;
